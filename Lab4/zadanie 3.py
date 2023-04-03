#. Stosując metodę "dziel i zwyciężaj", ułóż algorytm wyznaczania największego elementu wektora.
x = int(input("Podaj długość tablicy: "))
Wektor = []
for a in range(x):
    z = int(input(f"Podaj {a+1} liczbe: "))
    Wektor.append(z)

Lewa = 0
Prawa = len(Wektor)-1

def NajElement(Wektor,Lewa,Prawa):
    if Lewa == Prawa:
        return Wektor[Lewa]  #Jeśli Lewa i Prawa są tej samej długości to musi występować jeden wektor który będzie wynikiem
    Środek = (Lewa+Prawa)//2 #Wyznaczamy środek
    print(Wektor[Środek])


print(NajElement(Wektor,Lewa,Prawa))















'''
vector = [3,2,4,3,1]
left = 0
right = 4
def findMax(vector, left, right):
    if left == right:
        return vector[left]
    mid = (left + right) // 2 #= 1
    maxLeft = findMax(vector, left, mid)
    maxRight = findMax(vector, mid + 1, right)

    return max(maxLeft, maxRight)

max_element = findMax(vector, 0, len(vector) - 1)
print(max_element)

print(findMax(vector, left, right))
max_element = 0

for i in vector:
    if i > max_element:
        max_element = i
print(max_element)
'''

