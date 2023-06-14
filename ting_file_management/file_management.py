import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError("Formato inválido")
        with open(path_file, "r") as file:
            return file.read().split("\n")

    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        return []

    except ValueError:
        print("Formato inválido", file=sys.stderr)
        return []
