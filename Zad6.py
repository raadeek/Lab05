def czy_pierwsza(x):
    ile = 0
    for i in range(1, x + 1):
        if x % i == 0:
            ile = ile + 1

    if ile > 2:
        return 0
    else:
        return 1

liczba = int(input("Podaj liczbe:"))

i = 2
suma = 0
while i < liczba:
    if czy_pierwsza(i):
        print(i, end = " ")
        suma = suma + 1
    i += 1
print(f"Wynik to {suma}")