def converte_lista_elementos_para_texto(lista_elementos):
    lista_convertida = []
    for elemento in lista_elementos:
        lista_convertida.append(elemento.text)
    return lista_convertida