from Libro import AggiuntaLibro
from Libro import PrestitoLibro
from Libro import RestituzioneLibro

print("Benvenuto nella libreria!")
listalibri = []
libriprestati = []
AggiuntaLibro(listalibri)
PrestitoLibro(listalibri,libriprestati)
RestituzioneLibro(listalibri,libriprestati)