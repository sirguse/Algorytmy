# Zaproponuj rekurencyjny algorytm obliczania silni dla liczby całkowitej dodatniej n.

def silnia(n):
    if n == 0:
        return 1
    elif n >= 1:
       n = n * silnia(n-1)
       return n
       
print(silnia(5))