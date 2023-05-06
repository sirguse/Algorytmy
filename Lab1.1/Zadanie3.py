x = int(input("Podaj długość tablicy: "))
lista = []
for z in range(x):
    a = int(input(f"Podaj {z+1} liczbe: "))
    lista.append(a)

szukana = int(input("Podaj szukaną liczbe: "))
if szukana in lista:
    print("Liczba znajduje się w tablicy.")
else:
    print("Liczba nie znajduje się w tablicy.")