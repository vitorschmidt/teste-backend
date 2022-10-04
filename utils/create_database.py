import sqlite3

connection = sqlite3.connect("cnab.db")
c = connection.cursor()

def create_table():
    
    c.execute("CREATE TABLE Company (tipo, data, valor, cpf, cartao, hora, dono, nome_loja)")

create_table()

def insert_table(data_list):
    for data in data_list:
        query = f"""INSERT INTO Company (tipo, data, valor, cpf, cartao, hora, dono, nome_loja) VALUES({data[0]}, {data[1]}, {data[2]}, {data[3]}, "{data[4]}", {data[5]}, "{data[6]}", "{data[7]}")"""
        c.execute(query)
    
    connection.commit()