from utils.read_cnba import read_text
from utils.create_database import create_table, insert_table

FILEPATH = "CNAB.txt"


def main():
    try:
        data = read_text(FILEPATH)
        # print(f"data: {data}")
        insert_table(data)   
        
    except(FileNotFoundError):
        print("file not found")    

if __name__ == "__main__":
    main()    