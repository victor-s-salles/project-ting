from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(len(instance)):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None
    file = txt_importer(path_file)

    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(file),
        "linhas_do_arquivo": file,
    }

    instance.enqueue(data)
    print(data)

    return data


def remove(instance):
    if not instance or len(instance) == 0:
        print("Não há elementos")
        return None
    delete_file = instance.dequeue()

    path_file = delete_file["nome_do_arquivo"]

    print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        data_info = instance.search(position)

        print(data_info)
        return str(data_info)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
        return None
