# -*- coding: utf-8 -*-
from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file, redirect, template, response

app = Bottle()
ctl = Application()

# Chave secreta para criptografar os cookies de login e evitar fraudes
CHAVE_COOKIE = "legacy_secret_secure_key_2026"

# Rota para arquivos estáticos (CSS e JS)
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')


# ====================================================
# CONTROLE DE ACESSO & AUTENTICAÇÃO (BMVC III)
# ====================================================

# 1. Tela de Login (Acessível por qualquer um)
@app.route('/login')
def login_page():
    return template('login', erro=None)

# 2. Recebimento dos dados de Login (POST)
@app.route('/login', method='POST')
def do_login():
    usuario = request.forms.get('username')
    senha = request.forms.get('password')
    
    if ctl.verificar_login(usuario, senha):
        # Se os dados estiverem certos, gera o cookie de acesso restrito
        response.set_cookie("usuario_logado", usuario, secret=CHAVE_COOKIE, path='/')
        redirect('/admin')
    else:
        # Se errar, recarrega a página mostrando o erro na tela
        return template('login', erro="Usuário ou senha incorretos!")

# 3. Rota de Logout (Sair do sistema)
@app.route('/logout')
def do_logout():
    # Apaga o cookie do navegador e manda de volta para a vitrine pública
    response.delete_cookie("usuario_logado", path='/')
    redirect('/')


# ====================================================
# ROTAS DO SISTEMA (PÚBLICA VS RESTRITA)
# ====================================================

# ROTA PÚBLICA: Qualquer visitante vê os relógios (Apenas leitura)
@app.route('/')
def index():
    lista = ctl.listar_todos()
    return template('loja_publica', relogios=lista)


# ROTA RESTRITA: Exige validação de Cookies. Só o administrador acessa.
@app.route('/admin')
def admin_panel():
    # Verifica se o cookie válido existe no navegador do usuário
    usuario = request.get_cookie("usuario_logado", secret=CHAVE_COOKIE)
    if not usuario:
        redirect('/login') # BLOQUEIA O ACESSO E REDIRECIONA
        
    lista = ctl.listar_todos()
    return template('loja', relogios=lista)


# ====================================================
# ROTAS DO CRUD (TODAS PROTEGIDAS POR LOGIN)
# ====================================================

@app.route('/novo', method='POST')
def novo_relogio():
    if not request.get_cookie("usuario_logado", secret=CHAVE_COOKIE):
        redirect('/login')
    
    nome = request.forms.get('nome')
    preco = request.forms.get('preco')
    icone = request.forms.get('icone', '⌚')
    ctl.adicionar(nome, preco, icone)
    redirect('/admin')

@app.route('/editar', method='POST')
def editar_relogio():
    if not request.get_cookie("usuario_logado", secret=CHAVE_COOKIE):
        redirect('/login')
        
    id_relogio = request.forms.get('id')
    nome = request.forms.get('nome')
    preco = request.forms.get('preco')
    ctl.atualizar(id_relogio, nome, preco)
    redirect('/admin')

@app.route('/deletar/<id_relogio:int>')
def deletar_relogio(id_relogio):
    if not request.get_cookie("usuario_logado", secret=CHAVE_COOKIE):
        redirect('/login')
        
    ctl.deletar(id_relogio)
    redirect('/admin')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, reloader=True)