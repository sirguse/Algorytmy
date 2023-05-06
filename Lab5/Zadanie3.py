a = []
n = int(input("Podaj długość ciągu: "))

for b in range(n):
    if n == 0:
        a.append(b)
    elif n == 1:
        a.append(b)
    elif n > 1:
        a.append((2*a[b-1]) + a[b-2])
    
    
        
        
        
        
    