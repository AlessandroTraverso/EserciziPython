from Libro import AggiuntaLibro
from Libro import PrestitoLibro
from Libro import RestituzioneLibro
from Libro import DispLibro
from Libro import DispLibreria
from Libro import LibriPrestati

print("Benvenuto nella libreria!")
listalibri = []
libriprestati = []
continua="si"
while(continua=="si"):
    print("Scegli quale azione vuoi eseguire:")
    print("1. Aggiungere libri alla libreria\n2. Prendere in prestito libri\n3. Restituire dei libri\n4. Verificare disponibilità di specifici libri\n5. Verificare libri nella libreria\n6. Verificare libri in prestito")
    scelta = int(input())
    match scelta:
        case 1:
            AggiuntaLibro(listalibri)
        case 2:
            PrestitoLibro(listalibri,libriprestati)
        case 3:
            RestituzioneLibro(listalibri,libriprestati)
        case 4:
            DispLibro(listalibri,libriprestati)
        case 5:
            DispLibreria(listalibri)
        case 6:
            LibriPrestati(libriprestati)
        case _:
            print("Azione non prevista")
    print("Vuoi eseguire una nuova azione? Inserisci si o no")
    continua = input()

    