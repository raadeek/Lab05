liczba = int(input("Podaj liczbe dodatnia:"))
suma = 0
i = 1
suma_temp = 0
while suma <= liczba:
     suma_temp += i
     if suma_temp <= liczba:
         suma = suma_temp
         print(i, end = " ")
     else:
         break
     i = i + 1
print(suma)



