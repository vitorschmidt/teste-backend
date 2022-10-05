def read_text(filepath: str) -> list[dict]:
    with open(filepath, 'r',  encoding="utf-8") as file:

            list_data = []

            teste = file.readlines()                
            for content in teste:
                tipo = content[0]
                date = content[1:9]
                valor = content[9:19]
                converted_value = int(valor) * 100 
                cpf = content[19:30]
                cartao = content[30:42]  
                hora = content[42:48]
                dono = content[48:62]
                loja = content[62:81]

                data = (tipo, date, converted_value, cpf, cartao, hora, dono, loja)
                list_data.append(data)
                print(f"tipo: {tipo} - data: {date} - valor: {converted_value} - cpf: {cpf} - cartao: {cartao} - hora: {hora} - dono: {dono} - loja: {loja}")        

            return list_data
                    
