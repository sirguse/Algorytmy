lista = [1,2,3,11,21,111,231]
lista_posortowana = []

for i in range(len(lista)):
    najmniejszy = min(lista, key=lambda a: str(a)) # Nie do konca rozumiem parametru key=lambda x: str(x)
    lista_posortowana.append(najmniejszy)
    lista.remove(najmniejszy)

print(lista_posortowana)