main.py

# Ejercicio 1 - Caja del Kisco

#validacion de nombre str

nombre = input("Por favor ingrese su nombre: ").strip() # strip elimina los espacio adelante y al final
while not (nombre.isalpha()):     #atencion con el AND no se puede poner or, porque el numero tiene que estar entre 1 Y 10. 
    nombre = input("ERROR. Por favor ingrese su nombre: ")

#validacion de cantidad 

cant_producto = input("Canidad de productos: ").strip()
while not (cant_producto.isdigit()):
    cant_producto = input("ERROR. Ingrese la canidad de productos: ")
cant_producto = int(cant_producto)

#variables acumuladoras

total_sin_descuentos = 0
total_con_descuentos = 0
ahorro_total = 0

for cont in range (1,cant_producto + 1):
    precio = input(f"ingrese el precio del producto {cont}: ")
    while not (precio.isdigit()):
        precio = input(f"ERROR. Ingrese el precio del producto {cont}: ")
    precio = int(precio)

    total_sin_descuentos += precio # variables acumuladora, hasta aca va acumulando el precio original

    tiene_descuento = input("Si tiene descuento ingrese S/N: ").lower()
    while tiene_descuento not in  ["s", "n"]:
        tiene_descuento = input("ERROR. Ingrese S/N: ").lower()

#Procesamiento de totales y ahorro

    if tiene_descuento == "s":
        descuento_aplicado = precio * 0.10 # 10% se obtiene descuento
        precio_final = precio - descuento_aplicado #precio final es el precio con descuento aplicado

        ahorro_total += descuento_aplicado #se va acumulando la cantidad de descuentos
        total_con_descuentos += precio_final #se acumula al total a pagar
    else:
        total_con_descuentos += precio #Sin descuento, el precio final es el original, se acumula la variable total que debe pagar

#calculamos promedio 
promedio = float(total_con_descuentos / cant_producto)

#Mostrar resultados con el formato solicitado (:.2f) 

print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro total: ${ahorro_total:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


