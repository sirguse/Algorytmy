tablica=[-3,-2,-1,3,5]
najmniejsza=tablica[0]
for x in tablica:
    if x<=najmniejsza:
        najmniejsza=tablica[x]

print("najmniejsza liczba w liście to :", tablica)