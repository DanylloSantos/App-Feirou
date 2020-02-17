from app import app
from flask import jsonify,request

produtos =[
    {
        "id":1,
        "id_vendedor":1,
        "nome":"Camisa sem nome"
    },
    {
        "id":2,
        "id_vendedor":1,
        "nome":"Calça sem nome"
    },
    {
        "id":3,
        "id_vendedor":2,
        "nome":"Bermuda sem nome"
    },
    {
        "id":4,
        "id_vendedor":2,
        "nome":"Meia sem nome"
    }
]
produto_campos_obrigatorios =[]

# Listar todos produtos
@app.route("/produtos",methods = ["GET"])
def todos_produtos():
        dados = produtos
        total = len(dados)

        return jsonify({
                "resposta":dados,
                "total":total,
                "erro":None
            })

# Listar produtos do vendedor
@app.route("/produtos/<int:id_vendedor>",methods = ["GET"])
def produtos_lista(id_vendedor):
    total = 0
    # Buscar produtos do vendedor
    dados = [produto for produto in produtos if produto["id_vendedor"] == id_vendedor]
    total = len(dados)

    # Verificar se retornou algo
    if(dados):
        return jsonify({
                "resposta":dados,
                "total":total,
                "erro":None
            })
    else:
        return jsonify({
                "resposta":None,
                "total":total,
                "erro":"Não foi encontrado nem um produto no estoque!"
            })

# Exibir produto
@app.route("/produto/<int:id_produto>",methods = ["GET"])
def produto(id_produto):
    # Buscar produto
    for produto in produtos:
        if produto["id"] == id_produto:
            return jsonify({
                        "resposta":produto,
                        "erro":None
                    })
    # Caso nao encontre retorna erro
    return jsonify({
                "resposta":None,
                "erro":"Produto não encontrado!"
            })

# Salvar Produto
@app.route("/produto",methods = ["POST"])
def salvar_produto():
    # Recuperar os dados da requisicao
    dados = request.get_json()
    produtos.append(dados)

    return jsonify({
                        "resposta":"Produto salvo com sucesso!",
                        "erro":None
                    })

# Atualizar produto
@app.route("/produto/<int:id_produto>",methods = ["PUT"])
def produto_atualizar(id_produto):
    # Atualizar produto
    for produto in produtos:
        if produto["id"] == id_produto:
            produto["nome"] = request.get_json().get("nome")

            return jsonify({
                        "resposta":"Produto atualizado com sucesso!",
                        "erro":None
                    })
    # Caso nao encontre retorna erro
    return jsonify({
                "resposta":None,
                "erro":"Não atualizado: Produto não encontrado!"
            })

# Deletar produto
@app.route("/produto/<int:id_produto>",methods = ["DELETE"])
def produto_deletar(id_produto):
    # Deletar produto
    for index,produto in enumerate(produtos):
        if produto["id"] == id_produto:
            del(produtos[index])
            return jsonify({
                        "resposta":"Produto deletado com sucesso!",
                        "erro":None
                    })
    # Caso nao encontre retorna erro
    return jsonify({
                "resposta":None,
                "erro":"Não deletado: Produto não encontrado!"
            })   