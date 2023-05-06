'''
def func(i,j):
    if i>0 and j == 0:
        return 0
    elif i == 0 and j>0:
        return 1
    elif i == 0 and j == 0:
        return 0
    else:
        x = func(i -1,j)
        y = func(i, j-1)
        wynik = (x + y) / 2
        return wynik

print(func(0,0))
'''

n = int(input("Podaj rozmiar ciągu Fibonacciego: "))
fibL = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i >0 and j == 0:
            fibL[i][j] = 0
        elif i == 0 and j>0:
            fibL[i][j] = 1
        else:
            fibL[i][j] = (fibL[i-1][j]+fibL[i][j-1]) / 2

for row in fibL:
    print("   ".join([str(round(elem,2)) for elem in row]))