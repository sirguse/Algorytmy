
def binary(liczba):
    if liczba == 0:
        return 0
    else:
        a =  liczba%2 + 10*binary(liczba//2) # Nie rozumiem do końca
        return a

print(binary(10))
