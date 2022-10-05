import sqlite3

connection = sqlite3.connect("cnab.db")
c = connection.cursor()

def create_table():
    
    c.execute("""
        CREATE TABLE IF NOT EXISTS COMPANY (
            tipo INTEGER(1)         NOT NULL,
            data DATE     NOT NULL,
            valor INTEGER(10)       NOT NULL,
            cpf INTEGER(11)         NOT NULL,
            cartao TEXT(12)     NOT NULL,
            hora DATE   NOT NULL,
            dono VARCHAR(14)    NOT NULL,
            nome_loja VARCHAR(19)    NOT NULL
            )""")

create_table()

def insert_table(data_list):
    for data in data_list:
        query = f"""INSERT INTO COMPANY (tipo, data, valor, cpf, cartao, hora, dono, nome_loja) VALUES({data[0]}, {data[1]}, {data[2]}, {data[3]}, "{data[4]}", {data[5]}, "{data[6]}", "{data[7]}")"""
        c.execute(query)
    
    connection.commit()