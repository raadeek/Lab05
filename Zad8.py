from random import seed
from random import randint

seed()
x = randint(0, 100)


while True:
    liczba = int(input("Podaj liczbe:"))
    if liczba == x:
        print("Gratulacje: ")
        break
    elif liczba > x:
        print("Liczba jest za duza:")
    else:
        print("Liczba jest za mala")
