import sqlite3

def buscar_resultados_sqlite(banco_dados, tabela):
    resultados = []

    con = sqlite3.connect(banco_dados)

    cursor = con.cursor()

    cursor.execute(f'SELECT DISTINCT "Descrição dos alimentos" FROM {tabela}')
    

    resultados = cursor.fetchall()
    for resultado in resultados:
        print(resultado)

    con.close()


buscar_resultados_sqlite('TACO.db', 'alimentos')
