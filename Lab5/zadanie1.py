#Korzystając z techniki programowania dynamicznego napisz program obliczania
#elementów ciągu Fibonacciego:

fibL =[]
n = int(input("Podaj rozmiar ciągu "))
for i in range(n):
    if i == 0:
        fibL.append(i)
    elif i == 1:
        fibL.append(i)
    else:
        fibL.append(fibL[i-1] + fibL[i-2])

print(fibL)