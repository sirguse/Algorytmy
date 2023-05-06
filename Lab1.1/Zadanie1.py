import math

a = int(input("Podaj A: "))
b = int(input("Podaj B: "))
c = int(input("Podaj C: "))
delta = (b**2) - (4*a*c)
if a!=0:
    if delta > 0:
        x1 = (b*(-1) - math.sqrt(delta))/ 2*a
        x2 = (b*(-1) + math.sqrt(delta))/ 2*a
        print(f"x1 wynosi: {x1}")
        print(f"x2 wynosi: {x2}")
    else:
        if delta == 0:
            x0 = (b*(-1)) / 2*a
            print(f"x0 wynosi: {x0}")
        else:
            print("Brak rozwiązań.")

else:
    print("Koniec")

