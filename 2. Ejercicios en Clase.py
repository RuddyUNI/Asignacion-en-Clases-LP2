# Leer un numero entero y determinar cuantos dígitos tiene

numero = int(input("Ingresa un número entero: "))

# Determinar la cantidad de dígitos
cantidad_digitos = len(str(abs(numero)))

print(f"El número tiene {cantidad_digitos} dígitos.")

print("")
print("--------------------------------------------------------------------")
print("")

# Leer un numero entero y determinar si es primo

numero = int(input("Ingresa un número entero: "))

if numero > 1:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")
else:
    print("El número no es primo.")

print("")
print("--------------------------------------------------------------------")
print("")

# Leer 4 enteros, almacenarlos en una lista y determinar en que posición de la lista esta el mayor numero leido

numeros = []
for i in range(4):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

mayor = max(numeros)
posicion = numeros.index(mayor) + 1

print(f"El mayor número es {mayor} y está en la posición {posicion}.")

print("")
print("--------------------------------------------------------------------")
print("")

# Del siguiente listado, eliminar cualquier numero duplicado: 
# numeros = [1,1,2,3,3,2,5,6,2,7,8,4,3,1]

numeros = [1, 1, 2, 3, 3, 2, 5, 6, 2, 7, 8, 4, 3, 1]

# Eliminar duplicados y mantener el orden
numeros_sin_duplicados = list(dict.fromkeys(numeros))

print(f"Lista sin duplicados: {numeros_sin_duplicados}")