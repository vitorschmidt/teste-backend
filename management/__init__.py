from utils.create_database import insert_table
from utils.read_cnba import read_text



import os.path


pythonfile = 'db.sqlite3'
 
file_path = os.path.isfile(pythonfile)

FILEPATH = "uploads/CNAB.txt"


if file_path == True:

    try:
        data = read_text(FILEPATH)
        insert_table(data)
        print("arquivo encontrado")   
    except(FileNotFoundError):
            print("file not found")

