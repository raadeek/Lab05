liczba = int(input("Podaj liczbe: "))
bin = "start:"
i = 0
while liczba != 0:
    if liczba%2 == 0:
        bin = "0" + bin
    else:
        bin = "1" + bin
    print(f"Operacja nr {i} liczba wynosi {liczba}, a binarna to {bin}")
    i += 1
    liczba = liczba // 2
print(bin)