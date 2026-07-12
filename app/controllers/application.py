class Application:
    def __init__(self):
        # Lista em Python servindo como nosso modelo/banco de dados inicial (READ)
        self.relogios = [
            {"id": 1, "nome": "Classic Gold Edition", "preco": "2450.00", "icone": "⌚"},
            {"id": 2, "nome": "Chronograph Sport", "preco": "1890.00", "icone": "⏱️"},
            {"id": 3, "nome": "Minimalist Black", "preco": "1200.00", "icone": "🕰️"}
        ]
        self.proximo_id = 4

    def listar_todos(self):
        return self.relogios

    def adicionar(self, nome, preco, icone):
        # Operação de CREATE
        novo = {"id": self.proximo_id, "nome": nome, "preco": preco, "icone": icone}
        self.relogios.append(novo)
        self.proximo_id += 1

    def atualizar(self, id_relogio, nome, preco):
        # Operação de UPDATE
        for r in self.relogios:
            if r["id"] == int(id_relogio):
                r["nome"] = nome
                r["preco"] = preco
                break

    def deletar(self, id_relogio):
        # Operação de DELETE
        self.relogios = [r for r in self.relogios if r["id"] != int(id_relogio)]