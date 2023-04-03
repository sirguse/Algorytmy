# Dana jest tablica n liczb całkowitych. Przedstaw algorytm liczący sumę elementów w 
#tablicy z zastosowaniem metody „dziel i zwyciężaj”.



x = int(input("Podaj długość tablicy: "))
Tablica = []
for a in range(x):
    z = int(input(f"Podaj {a+1} liczbe: "))
    Tablica.append(z)


Lewa = 0
Prawa = len(Tablica) -1 

def Suma(Tablica, Lewa, Prawa):
    if Lewa == Prawa: #Sprawdzamy warunek, jeśli zostaje spełniony to suma jest równa jednemu elementowi tablicy.
        return Tablica[Lewa]
    
    Środek = (Lewa+Prawa)//2 #Znajdujemy środek przedziału 2
    SumaLewa = Suma(Tablica, Lewa, Środek) 
    SumaPrawa = Suma(Tablica,Środek+1, Prawa)
    return SumaLewa + SumaPrawa      #Nie do końca rozumiem dlaczego gdy returnujemy samą "SumePrawą", wychodzi ostatnia liczba tablicy.

Total = Suma(Tablica, 0, len(Tablica)-1) # Sumujemy 
print(Total)





