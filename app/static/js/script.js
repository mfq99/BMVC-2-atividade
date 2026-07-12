// Função chamada ao clicar no botão "Editar" de um relógio
function prepararEdicao(id, nome, preco) {
    document.getElementById('edit-id').value = id;
    document.getElementById('edit-nome').value = nome;
    document.getElementById('edit-preco').value = preco;
    
    // Mostra o modal de edição na tela
    document.getElementById('modal-edicao').style.display = 'flex';
}

function fecharEdicao() {
    document.getElementById('modal-edicao').style.display = 'none';
}