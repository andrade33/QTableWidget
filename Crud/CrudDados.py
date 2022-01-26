# -*- coding: utf-8 -*-

from sqlalchemy.exc import IntegrityError
from sqlalchemy import desc

from Crud.Models import Dados
from Crud.core import Conexao

class CrudDados(object):

    def __init__(self, id="", a="", b="", query=""):
        self.id = id
        self.a = a
        self.b = b
        self.query = query

    # Recebendo última id inserido

    def removeR(self):
        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando ID
            self.query = (sessao.query(Dados).get(self.id))
            if self.query:
                # add query na sessao
                sessao.delete(self.query)
                # Executando a query
                sessao.commit()

            # # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)

        pass


    def lastIdDado(self):
        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            ultimo = sessao.query(Dados).order_by(
                desc(Dados.id)).limit(1).first()

            self.id = ultimo.id + 1

            # Fechando Conexao
            sessao.close()

            pass

        except:

            self.id = 1

        return self.id

    #  Cadastro Cliente
    def inserirDado(self):

        try:
            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            row = Dados(
                #id=self.id,
                a=self.a,
                b=self.b,
            )

            # Execurando a Query
            sessao.add(row)
            sessao.commit()

            # Fechando a Sesao
            sessao.close()

            pass

        except IntegrityError:

            self.updateDado()

            pass

    #  Update Cliente
    def updateDado(self):
        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Selecionando id
            query = sessao.query(Dados).get(self.id)

            # Novos valores
            query.a = self.a
            query.b = self.b




            # Execurando a Query
            sessao.commit()

            # Fechando a Sesao
            sessao.close()

            pass

        except IntegrityError as err:

            print(err)

            pass

    # Buscando cliente por ID
    def selectDadoId(self):
        try:
            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()
            # Query
            busca = sessao.query(Dados).get(self.id)

            # Salvando resultado da Query
            self.id = busca.id
            self.a = busca.a
            self.b = busca.b


            # Fechando Conexao
            sessao.close()

            pass

        except:

            pass

        pass

    # Buscando Cliente por nome
    def listaDados(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            query = sessao.query(Dados).filter(
                Dados.a.contains(self.a))
            query.all()

            # # Convertendo variaveis em lista
            self.id = []
            self.a = []
            self.b = []

            # # Salvando resultado da query e suas listas
            for row in query:
                self.id.append(row.id)
                self.a.append(row.a)
                self.b.append(row.b)

            # fechando a conexao
            sessao.close()

            pass

        except IntegrityError as err:
            print(err)

            pass

    # Lista AutoComplete Cliente

    def autoCompleteDados(self):

        try:

            # Abrindo Sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Dados).filter(
                Dados.a.contains(self.a))
            self.query.all()

            # Convertendo variavel em lista
            self.id=[]
            self.a = []
            self.b = []


            # salvando resultado em lista
            for row in self.query:
                self.id.append(row.id)
                self.a.append(row.a)
                self.b.append(row.b)


            # Fechando Conexao
            sessao.close()

            pass

        except IntegrityError as err:

            print(err)

            pass

    # Busca CLiente por nome
    def buscaDadoNome(self):

        try:

            # Abrindo sessao
            conecta = Conexao()
            sessao = conecta.Session()

            # Query
            self.query = sessao.query(Dados).filter(
                Dados.a == self.a).first()

            # Salvando Resultado
            self.id = self.query.id
            self.a = self.query.a
            self.b = self.query.b

            # Fechando Conexao
            sessao.close()

        except IntegrityError as err:
            print(err)
