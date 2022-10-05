from utils.read_cnba import read_text
from utils.create_database import  insert_table
import os

FILEPATH = "uploads/CNAB.txt"



import os

# folder path
# dir_path = r'C:\Users\Schmi\code\kenzie\teste-backend\uploads'

# # list to store files
# res = []
# # Iterate directory
# for file in os.listdir(dir_path):
#     # check only text files
#     if file.endswith('.txt'):
#         res.append(file)
def main():
    try:
        data = read_text(FILEPATH)
        insert_table(data)   
    except(FileNotFoundError):
        print("file not found")    

if __name__ == "__main__":
    main()    