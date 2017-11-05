import MySQLdb

class bancoDeDados(object):
    @staticmethod
    def newUserTable():
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='users')
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (Nome text, email text, senha text)")
        conn.commit()

    @staticmethod
    def signUpUser(nome,email,senha):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='users')
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM users WHERE email = '"+ email +"'")
        emailDB = cursor.fetchone()
        if emailDB == None:
            cursor.execute("INSERT INTO users (Nome, email, senha) VALUES (?,?,?)",(nome,email,senha))
            conn.commit()
            return True
        else:
            return False

    @staticmethod
    def signInUser(email,senha):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='users')
        cursor = conn.cursor()
        cursor.execute("SELECT senha FROM users WHERE email = '"+ email +"'")
        senhaDB = cursor.fetchone()
        if str(senhaDB[0]) == senha:
            return True
        else:
            return False

    @staticmethod
    def horarios(tabela, linha, diaSemana):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        cursor.execute("SELECT Horario FROM "+ tabela +" WHERE Linha = '"+ linha +"' AND DiaSemana = '"+ diaSemana +"'")
        return cursor.fetchall()

    @staticmethod
    def addPassageiro(tabela, linha, diaSemana, horario):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        cursor.execute("SELECT Passageiros FROM "+ tabela +" WHERE Linha = '"+ linha +"' AND DiaSemana = '"+ diaSemana
                       +"' AND Horario = '"+ horario +"'")
        Passageiros = cursor.fetchone()
        newPassageiros = Passageiros + 1
        cursor.execute("UPDATE "+ tabela +" WHERE Linha = '"+ linha +"' AND DiaSemana = '"+ diaSemana +"'"
                        " SET Passageiros = "+ newPassageiros[0] +"")
        conn.commit()

    @staticmethod
    def subtPassageiro(tabela, linha, diaSemana, horario):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT Passageiros FROM " + tabela + " WHERE Linha = '" + linha + "' AND DiaSemana = '" + diaSemana
            + "' AND Horario = '"+ horario +"'")
        Passageiros = cursor.fetchone()
        newPassageiros = Passageiros - 1
        cursor.execute(
            "UPDATE " + tabela + " WHERE Linha = '" + linha + "' AND DiaSemana = '" + diaSemana + "'"
            " SET Passageiros = " + newPassageiros[0] + "")
        conn.commit()

    @staticmethod
    def setPosition(tabela, linha, diaSemana, latitude, longitude, horario):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        if tabela =='UfsmCentro':
            cursor.execute("UPDATE UfsmCentro SET Latitude="+str(latitude)+", Longitude="+str(longitude)+" WHERE Linha='"+linha+"' AND "
                           "DiaSemana='"+diaSemana+"' AND Horario='"+horario+"';")
        if tabela == 'CentroUFSM':
            cursor.execute("UPDATE CentroUFSM SET Latitude="+str(latitude)+", Longitude="+str(longitude)+" WHERE Linha='"+linha+"' AND "
                           "DiaSemana='"+diaSemana+"' AND Horario='"+horario+"';")
        conn.commit()

    @staticmethod
    def getPosition(tabela, linha, diaSemana, horario):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        cursor.execute("SELECT Latitude FROM " + tabela + " WHERE Linha = '" + linha + "' AND DiaSemana = '" + diaSemana
                       + "' AND Horario = '"+ horario +"'")
        Latitude = cursor.fetchone()
        cursor.execute("SELECT Longitude FROM " + tabela + " WHERE Linha = '" + linha + "' AND DiaSemana = '" + diaSemana
                       + "' AND Horario = '"+ horario +"'")
        Longitude = cursor.fetchone()
        Posicao = [Latitude[0],Longitude[0]]
        return Posicao

    @staticmethod
    def updateAdaptado(tabela, linha, diaSemana, horario, Adapt):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        cursor.execute("UPDATE "+ tabela +" WHERE Linha = '" + linha + "' AND DiaSemana = '" + diaSemana
            + "' AND Horario = '"+ horario +"' SET Adaptado = '"+ Adapt +"'")
        conn.commit()

    @staticmethod
    def getAdaptado(tabela, linha, diaSemana, horario):
        conn = MySQLdb.connect(host='192.168.15.4', user='user', passwd='102030', db='linhas')
        cursor = conn.cursor()
        cursor.execute("SELECT Adaptado FROM " + tabela + " WHERE Linha = '" + linha + "' AND DiaSemana = '" + diaSemana
                       + "' AND Horario = '"+ horario +"'")
        Adaptado = cursor.fetchone()
        if str(Adaptado[0]) == 'SIM':
            return 'YEP'
        if str(Adaptado[0]) == 'NAO':
            return 'NOP'
        else:
            return 'DONT KNOW'
