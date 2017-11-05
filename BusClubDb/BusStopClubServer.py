# -*- coding: utf-8 -*-
import DataBase




class BusStopClubServer(object):
    @staticmethod
    def build():
        DataBase.bancoDeDados.newUserTable();

    @staticmethod
    def cadastro(Nome, Email, Senha):
        if DataBase.bancoDeDados.signUpUser(Nome, Email, Senha):
            print("Cadastro realizado com sucesso!")
        else:
            print("Email já cadastrado, tente novamente.")

    @staticmethod
    def login(Email, Senha):
        if DataBase.bancoDeDados.signInUser(Email, Senha):
            print ("Login realizado com sucesso!")
            return True
        else:
            print ("Senha incorreta.")
            return False

    @staticmethod
    def get_horario(Destino, Linha, faixa, DiaSemana):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa

        return DataBase.bancoDeDados.horarios(tabela, newLinha, DiaSemana)

    @staticmethod
    def addPass(Destino, Linha, faixa, DiaSemana, hr):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa

        DataBase.bancoDeDados.addPassageiro(tabela, newLinha, DiaSemana, hr)

    @staticmethod
    def subtrPass(Destino, Linha, faixa, DiaSemana, hr):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa

        DataBase.bancoDeDados.subtPassageiro(tabela, newLinha, DiaSemana, hr)

    @staticmethod
    def setPos(Destino, Linha, faixa, DiaSemana, Latitude, Longitude, hr):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa
        DataBase.bancoDeDados.setPosition(tabela, newLinha, DiaSemana, Latitude, Longitude, hr)

    @staticmethod
    def getPos(Destino, Linha, faixa, DiaSemana, hr):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa
        return DataBase.bancoDeDados.getPosition(tabela, newLinha, DiaSemana, hr)

    @staticmethod
    def setAdapt(Destino, Linha, faixa, DiaSemana, hr, Adapt):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa
        if (Adapt):
            newAdapt = 'SIM'
        else:
            newAdapt = 'NAO'
        DataBase.bancoDeDados.updateAdaptado(tabela, newLinha, DiaSemana, hr, newAdapt)

    @staticmethod
    def getAdapt(Destino, Linha, faixa, DiaSemana, hr):
        if Destino == 'UFSM':
            tabela = 'CentroUFSM'
        if Destino == 'Centro':
            tabela = 'UfsmCentro'

        newLinha = Linha + "_" + faixa
        if (DataBase.bancoDeDados.getAdaptado(tabela, newLinha, DiaSemana, hr) == 'YEP'):
            return 'É adaptado.'
        if (DataBase.bancoDeDados.getAdaptado(tabela, newLinha, DiaSemana, hr) == 'NOP'):
            return 'Não é adaptado.'
        if (DataBase.bancoDeDados.getAdaptado(tabela, newLinha, DiaSemana, hr) == 'DONT KNOW'):
            return 'Não se sabe.'
