# Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0  # Contador para regla anti-spam

# Validación del nombre (Fuente 35, 37)
agente = input("Nombre del agente: ")
while not agente.isalpha():
    agente = input("Error. Use solo letras para el nombre: ")

# Ciclo principal 
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print(f"\n--- ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}/3 ---")
    if alarma: print("¡ALERTA! Sistema de seguridad activo.")
    
    print("1. Forzar cerradura\n2. Hackear panel\n3. Descansar")
    opcion = input("Acción: ")
    
    # Validación de opción
    while not (opcion.isdigit() and "1" <= opcion <= "3"):
        opcion = input("Error. Elija 1, 2 o 3: ")

    if opcion == "1": # FORZAR CERRADURA
        racha_forzar += 1
        energia -= 20
        tiempo -= 2
        
        # Regla Anti-spam
        if racha_forzar == 3:
            alarma = True
            print("¡La cerradura se trabó por forzarla demasiado! Alarma activa.")
        else:
            # Riesgo de alarma por baja energía
            if energia < 40:
                print("RIESGO DE ALARMA (Baja energía)")
                riesgo = input("Elija un número (1-3): ")
                while not (riesgo.isdigit() and "1" <= riesgo <= "3"):
                    riesgo = input("Invalido. Elija 1-3: ")
                if riesgo == "3":
                    alarma = True
            
            if not alarma:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta con éxito!")

    elif opcion == "2": # HACKEAR PANEL
        racha_forzar = 0 # Rompe la racha (Regla anti-spam)
        energia -= 10
        tiempo -= 3
        
        # Ciclo FOR para progreso 
        print("Hackeando...")
        for i in range(1, 5): # 4 pasos
            print(f"Paso {i}...")
            codigo_parcial += "A" # Acumulador de letras
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Código descifrado! Una cerradura se abrió.")

    elif opcion == "3": # DESCANSAR
        racha_forzar = 0 # Rompe la racha
        recuperacion = 15
        if alarma:
            energia -= 10
            print("Descanso difícil por la alarma (-10 energía extra)")
        
        energia += recuperacion
        if energia > 100: energia = 100 # Límite máximo
        tiempo -= 1
        print("Has recuperado algo de energía.")

# CONDICIONES DE FIN 
if cerraduras_abiertas == 3:
    print(f"\n¡VICTORIA! El agente {agente} abrió la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA: Te quedaste sin recursos.")
elif alarma and tiempo <= 3:
    print("\nDERROTA: El sistema se bloqueó por la alarma.")