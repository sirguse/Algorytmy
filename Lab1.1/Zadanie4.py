tablica = [1,6,4,-2,1,-6,2,5]
'''
x = int(input("Podaj długość tablicy: "))
for z in range(x):
    a = int(input(f"Podaj {z+1} liczbe: "))
    tablica.append(a)
'''
najmniejsza = tablica[0]
for i in tablica:
    if i < najmniejsza:
        najmniejsza = i
        
print("Najmniejszy element to: ",najmniejsza)

    