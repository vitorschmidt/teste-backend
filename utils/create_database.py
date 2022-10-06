import sqlite3

connection = sqlite3.connect("db.sqlite3")
c = connection.cursor()

def insert_table(data_list):
    for data in data_list:
        query = f"""INSERT INTO manage_files_manage_file (tipo, data, valor, cpf, cartao, hora, dono, nome_loja) VALUES({data[0]}, {data[1]}, {data[2]}, {data[3]}, "{data[4]}", {data[5]}, "{data[6]}", "{data[7]}")"""
        c.execute(query)
    
    connection.commit()