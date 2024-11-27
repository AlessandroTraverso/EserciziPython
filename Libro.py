

def AggiuntaLibro(lista):
    print("Quanti libri vuoi inserire all'interno della libreria?")
    x = input()
    for i in x:
        titolo = (input(print(f"Inserisci il titolo del libro numero")))
        lista.append(titolo)
    lista.sort()
    print("Questa è la tua libreria in ordine alfabetico:")
    print(lista)
