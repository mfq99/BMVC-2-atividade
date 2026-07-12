from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file, redirect, template, response


app = Bottle()
ctl = Application()

# Rota para arquivos estáticos (CSS e JS)
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

# 1. READ (Listar os relógios do objeto Python no HTML)
@app.route('/')
def index():
    lista = ctl.listar_todos()
    return template('loja', relogios=lista)

# 2. CREATE (Adicionar relógio através do formulário)
@app.route('/novo', method='POST')
def novo_relogio():
    nome = request.forms.get('nome')
    preco = request.forms.get('preco')
    icone = request.forms.get('icone', '⌚')
    ctl.adicionar(nome, preco, icone)
    redirect('/')

# 3. UPDATE (Atualizar os dados do relógio)
@app.route('/editar', method='POST')
def editar_relogio():
    id_relogio = request.forms.get('id')
    nome = request.forms.get('nome')
    preco = request.forms.get('preco')
    ctl.atualizar(id_relogio, nome, preco)
    redirect('/')

# 4. DELETE (Remover o relógio da lista)
@app.route('/deletar/<id_relogio:int>')
def deletar_relogio(id_relogio):
    ctl.deletar(id_relogio)
    redirect('/')

# --- ESTA É A LINHA QUE FALTAVA PARA O WINDOWS NÃO RECUSAR A CONEXÃO ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True, reloader=True)