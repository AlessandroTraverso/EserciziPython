

def AggiuntaLibro(lista):
    print("Quanti libri vuoi inserire all'interno della libreria?")
    x = int(input())
    for i in range (x):
        print("Inserisci il titolo del libro numero" ,i+1)
        titolo = input()
        lista.append(titolo)
    lista.sort()
    print("Questa è la tua libreria in ordine alfabetico:")
    print(lista)

def PrestitoLibro(lista,prestati):
    print("Quanti libri vuoi prendere in prestito?")
    x = int(input())
    for i in range(x):
        print("Inserisci il titolo del libro numero" ,i+1, "che vuoi prendere in prestito")
        titolo = input()
        if titolo in lista:
            prestati.append(titolo)
            lista.remove(titolo)
        else:
            print(f"Purtroppo il libro " + titolo + " non è al momento disponibile")
    print(prestati)
    print(lista)

def RestituzioneLibro(lista,prestati):
    print("Quanti libri vuoi restituire?")
    x = int(input())
    y = len(prestati)
    for i in range (x):
        print("Inserisci il titolo del libro numero" ,i+1, "che vuoi restituire")
        titolo = input()
        if titolo in prestati:
            prestati.remove(titolo)
            lista.append(titolo)
        else:
            print("Il libro dal titolo " + titolo + " non risulta prestato")
    lista.sort()
    print(lista)
    print(prestati)

