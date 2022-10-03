def read_text(filepath: str) -> list[dict]:
    with open(filepath, 'r') as file:

        data = file.read()

        print(data)