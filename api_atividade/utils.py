from models import Pessoas

#inserir pessoas na tabela
def insere_pessoas():
    pessoa = Pessoas(nome= "Daniel", idade= 23) #cria uma instancia de uma pessoa usando os parametros da classe
    #mostra a pessoa que foi inserida no banco de dados
    #print(pessoa) 
    
    #adicionando a pessoa no banco de dados
    pessoa.save()


#consultar todas as pessoas que existem na tabela
def consulta_pessoas():

    print("Todas as pessoas que existem na tabela")
    pessoa = Pessoas.query.all()
    print(pessoa)
    
    #para retornar todos os usuários aonde o nome é daniel
    #print("idade de daniel")
    pessoa = Pessoas.query.filter_by(nome="Daniel").first()
    #print(pessoa.idade) 
    """
    for i in pessoa:
        print(i)
    """


#alterar as pessoas que existem na tabela
def alterar_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Daniel").first()

    #idade que quero que a pessoa tenha
    pessoa.idade = 21
    #fazer commit da alteração feita na pessoa
    pessoa.save()

#apagar pessoa da tabela pessoas
def apagar_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Daniel").first()
    pessoa.delete()




#main
if __name__ == "__main__":
    #O crud
    
    
    insere_pessoas()
    
    #alterar_pessoa()
    #apagar_pessoa()
    consulta_pessoas()
