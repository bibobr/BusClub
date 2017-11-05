import _sqlite3

conn = _sqlite3.connect('linhas.db')

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS UfsmCentro (Linha TEXT, DiaSemana TEXT, Horario TEXT, PosicaoAtual TEXT,"
               " UltimaAtualizacao TEXT)")

DiaSemana = 'Domingo_Feriado'
Linha = 'Universidade_FN'

while(1):
    horarios = input("Digite o horario para "+ Linha +":")
    cursor.execute("INSERT INTO UfsmCentro (Linha, DiaSemana, Horario) VALUES ('"+ Linha +"', '"+ DiaSemana +"', '"
                   + horarios +"')")

    conn.commit()
    print ("Valor inserido com sucesso!\n")