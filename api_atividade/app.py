from flask import Flask, request

from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)

api = Api(app)

class Pessoa(Resource):
    def get(self, nome):
        try:
            pessoa = Pessoas.query.filter_by(nome=nome).first()

            response = {
                "nome": pessoa.nome,
                "idade": pessoa.idade,
                "id": pessoa.id
            }
        
        except AttributeError:
            response = {
                "status": "error",
                "mensagem": "Pessoa não encontrada"

            }
        
        return response


    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']

        if "idade" in dados:
            pessoa.idade = dados['idade']
        
        pessoa.save()
        response = {

            "id": pessoa.id,
            "nome": pessoa.nome,
            "idade": pessoa.idade
        }

        return response

    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome= nome).first()
        mensagem = f"pessoa {pessoa.nome} excluida com sucesso"

        pessoa.delete()

        return {
                "status": "sucesso",
                "mensagem": mensagem
                }


class ListarPessoas(Resource):
    def get(self):
        pessoas = Pessoas.query.all()
        
        response = [ {'id': i.id, 'nome': i.nome, "idade": i.idade } for i in pessoas]
        return response


    def post(self):
        dados = request.json
        pessoa = Pessoas(nome= dados['nome'], idade=dados['idade'])

        pessoa.save()


        response = {
            "id": pessoa.id,
            'nome': pessoa.nome,
            "idade": pessoa.idade
        }

        return response
        pass


class ListaAtividades(Resource):
    def post(self):
        dados = request.json
        
        # Verifique se a pessoa existe
        pessoa = Pessoas.query.filter_by(nome=dados["pessoa"]).first()
        
        if pessoa is None:
            return {
                "status": "error",
                "mensagem": f"Pessoa '{dados['pessoa']}' não encontrada."
            }, 404

        # Cria a nova atividade se a pessoa for encontrada
        atividade = Atividades(nome=dados["nome"], pessoa=pessoa)
        atividade.save()

        response = {
            "pessoa": atividade.pessoa.nome,
            "nome": atividade.nome,
            "id": atividade.id
        }
    
        return response, 201


    def get(self):
        atividades = Atividades.query.all()
        response = [{
    "id": i.id, 
    "nome": i.nome, 
    "pessoa": i.pessoa.nome if i.pessoa else "Pessoa não associada"
} for i in atividades]

        return response 


#rotas

#rota para o get de pessoas
api.add_resource(Pessoa, "/pessoa/<string:nome>/")
api.add_resource(ListarPessoas, "/pessoa/")
api.add_resource(ListaAtividades, '/atividade/')




if __name__ == "__main__":
    app.run(debug=True)