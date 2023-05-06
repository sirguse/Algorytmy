x = int(input("Podaj długość ciągu: "))
liczba = 0

if x > 0:
    for z in range(x):
        a = int(input(f"Podaj liczbe {z+1}: "))
        if a < 0:
            liczba += 1
    print(f"Tyle liczb ujemnych podałeś: {liczba}")
else:
    print("Podaj liczby większe od 0")
    