def exists_word(word, instance, includeContent=False):
    result = []

    for i in range(len(instance)):
        search = instance.search(i)
        data = {
            "palavra": word,
            "arquivo": search["nome_do_arquivo"],
            "ocorrencias": [],
        }
        for text in search["linhas_do_arquivo"]:
            if word.lower() in text.lower():
                if includeContent:
                    data["ocorrencias"].append(
                        {
                            "linha": search["linhas_do_arquivo"].index(text)
                            + 1,
                            "conteudo": text,
                        }
                    )
                else:
                    data["ocorrencias"].append(
                        {"linha": search["linhas_do_arquivo"].index(text) + 1}
                    )

        if len(data["ocorrencias"]) > 0:
            result.append(data)
    return result


def search_by_word(word, instance):
    return exists_word(word, instance, includeContent=True)
