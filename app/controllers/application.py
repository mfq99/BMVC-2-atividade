# -*- coding: utf-8 -*-

class Application:
    def __init__(self):
        # O seu banco de dados em memória continua aqui
        self.relogios = [
            {"id": 1, "nome": "Classic Gold Edition", "preco": "2450.00", "icone": "⌚"},
            {"id": 2, "nome": "Chronograph Sport", "preco": "1890.00", "icone": "⏱️"},
            {"id": 3, "nome": "Minimalist Black", "preco": "1200.00", "icone": "🕰️"}
        ]
        self.proximo_id = 4
        
        # CREDENCIAIS EXIGIDAS PARA O CONTROLE DE ACESSO (BMVC III)
        self.usuario_adm = "admin"
        self.senha_adm = "1234"

    def verificar_login(self, usuario, senha):
        """Retorna True se os dados de login estiverem corretos"""
        return usuario == self.usuario_adm and senha == self.senha_adm

    def listar_todos(self):
        return self.relogios

    def adicionar(self, nome, preco, icone):
        novo_relogio = {
            "id": self.proximo_id,
            "nome": nome,
            "preco": preco,
            "icone": icone
        }
        self.relogios.append(novo_relogio)
        self.proximo_id += 1

    def atualizar(self, id_relogio, nome, preco):
        for r in self.relogios:
            if r["id"] == int(id_relogio):
                r["nome"] = nome
                r["preco"] = preco
                break

    def deletar(self, id_relogio):
        self.relogios = [r for r in self.relogios if r["id"] != int(id_relogio)]