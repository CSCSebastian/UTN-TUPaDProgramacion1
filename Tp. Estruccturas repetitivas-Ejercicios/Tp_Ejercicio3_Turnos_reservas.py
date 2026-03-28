# ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

#Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos:

#Turnos 
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

#Validacion 

operador = input("Ingrese nombre del operador: ")
while not operador.isalpha(): 
    print("Error, ingrese solo letras")
    operador = input("Ingrese nombre del operador: ")

# MENU 

opcion = ""

while opcion != "5":
    print(f"Menu - operador {operador}")
    print("1. Reserva turno")
    print("2. Cancelar Turno")   
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Salir del sistema")

    opcion = input("Ingrese una opcion: ")

# Validacion menu

    while not (opcion.isdigit() and "1" <= opcion <= "5"):
        opcion = input("Error. Ingrese una opcion valida entre 1 y 5: ") 

    if opcion == "1": #reserva turno

        dia = input("elegir dia (1= Lunes o 2= Martes)")
        while dia not in ["1" , "2"]:
            dia = input("Dia invalido. Inrese: 1 para Lunes o 2 para Martes")

        paciente = input("Ingrese nombre del paciente: ")
        while not paciente.isalpha():
                paciente = input("Error. Ingrese el nombre del paciente: ")

        if dia == "1": 
        
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                    print("Error: El paciente ya tiene un turno este día.")
            # Guardar en primer espacio libre
            elif lunes1 == "": lunes1 = paciente; print("Turno reservado en Lunes (Turno 1)")
            elif lunes2 == "": lunes2 = paciente; print("Turno reservado en Lunes (Turno 2)")
            elif lunes3 == "": lunes3 = paciente; print("Turno reservado en Lunes (Turno 3)")
            elif lunes4 == "": lunes4 = paciente; print("Turno reservado en Lunes (Turno 4)")
            else: print("Sin cupos disponibles para el Lunes.")

        else:  #martes
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("Error: El paciente ya tiene un turno este día.")
            elif martes1 == "": martes1 = paciente; print("Turno reservado en Martes (Turno 1)")
            elif martes2 == "": martes2 = paciente; print("Turno reservado en Martes (Turno 2)")
            elif martes3 == "": martes3 = paciente; print("Turno reservado en Martes (Turno 3)")
            else: print("Sin cupos disponibles para el Martes.")

    elif opcion == "2": #cancelar turno
        dia = input("Elegir día (1=Lunes, 2=Martes): ")
        paciente = input("Nombre del paciente a cancelar: ")
        encontrado = False

        if dia == "1":
            if lunes1 == paciente: lunes1 = ""; encontrado = True
            elif lunes2 == paciente: lunes2 = ""; encontrado = True
            elif lunes3 == paciente: lunes3 = ""; encontrado = True
            elif lunes4 == paciente: lunes4 = ""; encontrado = True
        else:
            if martes1 == paciente: martes1 = ""; encontrado = True
            elif martes2 == paciente: martes2 = ""; encontrado = True
            elif martes3 == paciente: martes3 = ""; encontrado = True
        
        if encontrado: 
            print("Turno cancelado exitosamente.")
        else:
            print("No se encontró al paciente en la agenda.")

    elif opcion == "3": # ver agenda
        dia = input("Elegir día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print(f"Lunes - Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
            print(f"Lunes - Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
            print(f"Lunes - Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
            print(f"Lunes - Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
        else:
            print(f"Martes - Turno 1: {martes1 if martes1 != '' else '(libre)'}")
            print(f"Martes - Turno 2: {martes2 if martes2 != '' else '(libre)'}")
            print(f"Martes - Turno 3: {martes3 if martes3 != '' else '(libre)'}")

    elif opcion == "4": # resumen general
        
        oc_l = 0; oc_m = 0  # Contadores,  
        if lunes1 != "": oc_l += 1
        if lunes2 != "": oc_l += 1
        if lunes3 != "": oc_l += 1
        if lunes4 != "": oc_l += 1
        
        if martes1 != "": oc_m += 1
        if martes2 != "": oc_m += 1
        if martes3 != "": oc_m += 1

        print(f"Lunes: {oc_l} ocupados, {4-oc_l} disponibles.")
        print(f"Martes: {oc_m} ocupados, {3-oc_m} disponibles.")
        
        # Comparación de dias ocupados
        if oc_l > oc_m: print("El día con más turnos es el Lunes.")
        elif oc_m > oc_l: print("El día con más turnos es el Martes.")
        else: print("Empate en cantidad de turnos ocupados.")

print("Sistema cerrado correctamente.")

