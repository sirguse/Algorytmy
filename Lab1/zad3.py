lista = []
for x in range(5):
    a = int(input("Podaj liczby: "))
    lista.append(a)
szukana = int(input("Podaj szukaną liczbę: "))
if szukana in lista:
    print("Liczba znajduje się w zbiorze.")
else: 
    print("Liczba nie znajduje się w zbiorze.")

    
