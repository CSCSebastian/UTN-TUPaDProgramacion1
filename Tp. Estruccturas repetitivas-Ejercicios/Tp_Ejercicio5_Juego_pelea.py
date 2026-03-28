#Código de "La Arena del Gladiador"

#PASO 1: CONFIGURACIÓN 

#Validación de nombre
nombre = input("Ingrese nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Ingrese nombre del Gladiador: ")

#PASO 2: INICIALIZACIÓN
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
daño_base_pesado = 15
daño_enemigo = 12
juego_activo = True #Booleano para control

# PASO 3: CICLO DE COMBATE
#Se repite mientras ambos tengan vida
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"\n--- {nombre}: {vida_gladiador} HP | Enemigo: {vida_enemigo} HP | Pociones: {pociones} ---")
    
    # Menú del Jugador
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")
    
    opcion = input("Seleccione su acción: ")

    # Validación estricta de número y rango

    while not (opcion.isdigit() and "1" <= opcion <= "3"):
        print("Error. Ingrese una opción válida (1, 2 o 3).")
        opcion = input("Seleccione su acción: ")
    
    #Logica de las Acciones del Jugador
    if opcion == "1": #Ataque Pesado
        daño_final = float(daño_base_pesado)
        if vida_enemigo < 20: #Golpe Critico
            daño_final = daño_base_pesado * 1.5 #Uso de Float
            print("¡GOLPE CRÍTICO!")

        vida_enemigo -= daño_final
        
        print(f"¡Atacaste al enemigo por {daño_final} puntos de daño!")
        
    elif opcion == "2": #Rafaga Veloz
        print("¡Iniciando ráfaga!")
        for i in range(3): #Se repite 3 veces
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
            
    elif opcion == "3": #Curar
        if pociones > 0:
            vida_gladiador += 30
            if vida_gladiador > 100: vida_gladiador = 100
            pociones -= 1
            print("Te has curado 30 HP.")
        else:
            print("¡No quedan pociones! Pierdes el turno.")

    #Turno del Enemigo (Si sigue vivo)
    if vida_enemigo > 0:
        vida_gladiador -= daño_enemigo
        print(f"¡El enemigo te atacó por {daño_enemigo} puntos de daño!")

#PASO 4: FIN DEL JUEGO
if vida_gladiador > 0:
    print(f"\n¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("\nDERROTA. Has caído en combate.")