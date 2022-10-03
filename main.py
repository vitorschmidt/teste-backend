from utils.read_cnba import read_text

FILEPATH = "CNAB.txt"

def main():
    try:
        data = read_text(FILEPATH)

        return data
    except(FileNotFoundError):
        print("file not found")    

if __name__ == "__main__":
    main()    