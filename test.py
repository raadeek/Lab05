x = int(input("podaj liczbe:"))
ile = 0
for i in range(1, x+1):
    if x % i == 0:
        ile = ile + 1

if ile > 2:
    print("liczba nie pierwsza")
else:
    print("liczba pierwsza")