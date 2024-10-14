# Importando a função de criar um banco de dados do sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

# Importando algumas funções para fazer a sessão do banco de dados
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

from sqlalchemy.ext.declarative import declarative_base

# Criando o banco de dados
engine = create_engine("sqlite:///atividades.db")
db_session = scoped_session(sessionmaker(autocommit=False, 
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = "pessoa"
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True) 
    idade = Column(Integer)

    def __repr__(self):
        return f'<Pessoa {self.nome}>'

    def save(self):
        db_session.add(self)
        db_session.commit()


    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Atividades(Base):
    __tablename__ = "atividades"  # Corrigido o nome da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship("Pessoas")  # Corrigido para "Pessoas"

    def save(self):
        db_session.add(self)
        db_session.commit()


    def delete(self):
        db_session.delete(self)
        db_session.commit()

def init_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
