# UTN-TUPaDProgramacion1

TP\_Estructuras\_Sec\_Con\_Rep



Trabajo practico Estructura Repetititvas





\# Ejercicio 1 - Caja del Kisco



\#validacion de nombre str



nombre = input("Por favor ingrese su nombre: ").strip() # strip elimina los espacio adelante y al final

while not (nombre.isalpha()):     #atencion con el AND no se puede poner or, porque el numero tiene que estar entre 1 Y 10. 

&#x20;   nombre = input("ERROR. Por favor ingrese su nombre: ")



\#validacion de cantidad 



cant\_producto = input("Canidad de productos: ").strip()

while not (cant\_producto.isdigit()):

&#x20;   cant\_producto = input("ERROR. Ingrese la canidad de productos: ")

cant\_producto = int(cant\_producto)



\#variables acumuladoras



total\_sin\_descuentos = 0

total\_con\_descuentos = 0

ahorro\_total = 0



for cont in range (1,cant\_producto + 1):

&#x20;   precio = input(f"ingrese el precio del producto {cont}: ")

&#x20;   while not (precio.isdigit()):

&#x20;       precio = input(f"ERROR. Ingrese el precio del producto {cont}: ")

&#x20;   precio = int(precio)



&#x20;   total\_sin\_descuentos += precio # variables acumuladora, hasta aca va acumulando el precio original



&#x20;   tiene\_descuento = input("Si tiene descuento ingrese S/N: ").lower()

&#x20;   while tiene\_descuento not in  \["s", "n"]:

&#x20;       tiene\_descuento = input("ERROR. Ingrese S/N: ").lower()



\#Procesamiento de totales y ahorro



&#x20;   if tiene\_descuento == "s":

&#x20;       descuento\_aplicado = precio \* 0.10 # 10% se obtiene descuento

&#x20;       precio\_final = precio - descuento\_aplicado #precio final es el precio con descuento aplicado



&#x20;       ahorro\_total += descuento\_aplicado #se va acumulando la cantidad de descuentos

&#x20;       total\_con\_descuentos += precio\_final #se acumula al total a pagar

&#x20;   else:

&#x20;       total\_con\_descuentos += precio #Sin descuento, el precio final es el original, se acumula la variable total que debe pagar



\#calculamos promedio 

promedio = float(total\_con\_descuentos / cant\_producto)



\#Mostrar resultados con el formato solicitado (:.2f) 



print(f"Total sin descuentos: ${total\_sin\_descuentos:.2f}")

print(f"Total con descuentos: ${total\_con\_descuentos:.2f}")

print(f"Ahorro total: ${ahorro\_total:.2f}")

print(f"Promedio por producto: ${promedio:.2f}")









print()











\# ejercicio 2 - Acceso al Campus y Menú Seguro



\#usuario correcto: alumno

\#clave correcta: python123



usuario\_esperado = "alumno"

clave\_esperada = "python123"

intento\_max = 3

intento = 1

acceso\_concedido = False



print(f"intento {intento} ingrese usuario y clave:")

usuario = input("Nombre: ")

clave = input("Clave: ")



while not (usuario\_esperado == usuario and clave\_esperada == clave) and intento < intento\_max :

&#x20;   print(f"intento {intento + 1}. Credenciales invalidas, ingrese usuario y clave: ")

&#x20;   usuario = input("Nombre: ")

&#x20;   clave = input("Clave: ")

&#x20;   intento += 1



if usuario == usuario\_esperado and clave == clave\_esperada:

&#x20;   acceso\_concedido = True

&#x20;   print("Acceso concedido")

else:

&#x20;   print("Cuenta bloqueada")



if not acceso\_concedido:

&#x20;   print("Intentelo mas tarde")



else:

&#x20;   opcion = ""



&#x20;   while opcion != "4":  #ciclo por bandera.

&#x20;       print("Acceso al Menu")

&#x20;       print("1. Ver estado de inscripción")

&#x20;       print("2. Cambiar clave")

&#x20;       print("3. Mostrar mensaje motivacional")

&#x20;       print("4. Salir")



&#x20;       opcion = input("Seleccione una opción: ")



&#x20;       while not (opcion.isdigit() and "1" <= opcion <= "4"):

&#x20;           print("Error. Ingrese un valor entre 1 y 4")

&#x20;           opcion = input("Seleccione una opción: ")



&#x20;       if opcion == "1":

&#x20;           print("Estado: Inscripto")



&#x20;       elif opcion == "2":

&#x20;           nueva\_clave = input("Ingrese su nueva clave: ")

&#x20;           confirmacion = input("Confirme su nueva clave: ")

&#x20;           

&#x20;           if (nueva\_clave == confirmacion) and len(nueva\_clave) >= 6:

&#x20;               print("¡Clave cambiada con éxito!")

&#x20;           else:

&#x20;               print("Error, minimo seis caracteres")



&#x20;       elif opcion == "3":

&#x20;           print("Frase del día: La disciplina es la base del exito")



&#x20;       else:

&#x20;           print("Opción no válida. Por favor, intente de nuevo.")



&#x20;   print("Programa finalizado.")







print()









\# ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”



\#Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos:



\#Turnos 

lunes1 = ""

lunes2 = ""

lunes3 = ""

lunes4 = ""

martes1 = ""

martes2 = ""

martes3 = ""



\#Validacion 



operador = input("Ingrese nombre del operador: ")

while not operador.isalpha(): 

&#x20;   print("Error, ingrese solo letras")

&#x20;   operador = input("Ingrese nombre del operador: ")



\# MENU 



opcion = ""



while opcion != "5":

&#x20;   print(f"Menu - operador {operador}")

&#x20;   print("1. Reserva turno")

&#x20;   print("2. Cancelar Turno")   

&#x20;   print("3. Ver agenda del dia")

&#x20;   print("4. Ver resumen general")

&#x20;   print("5. Salir del sistema")



&#x20;   opcion = input("Ingrese una opcion: ")



\# Validacion menu



&#x20;   while not (opcion.isdigit() and "1" <= opcion <= "5"):

&#x20;       opcion = input("Error. Ingrese una opcion valida entre 1 y 5: ") 



&#x20;   if opcion == "1": #reserva turno



&#x20;       dia = input("elegir dia (1= Lunes o 2= Martes)")

&#x20;       while dia not in \["1" , "2"]:

&#x20;           dia = input("Dia invalido. Inrese: 1 para Lunes o 2 para Martes")



&#x20;       paciente = input("Ingrese nombre del paciente: ")

&#x20;       while not paciente.isalpha():

&#x20;               paciente = input("Error. Ingrese el nombre del paciente: ")



&#x20;       if dia == "1": 

&#x20;       

&#x20;           if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:

&#x20;                   print("Error: El paciente ya tiene un turno este día.")

&#x20;           # Guardar en primer espacio libre

&#x20;           elif lunes1 == "": lunes1 = paciente; print("Turno reservado en Lunes (Turno 1)")

&#x20;           elif lunes2 == "": lunes2 = paciente; print("Turno reservado en Lunes (Turno 2)")

&#x20;           elif lunes3 == "": lunes3 = paciente; print("Turno reservado en Lunes (Turno 3)")

&#x20;           elif lunes4 == "": lunes4 = paciente; print("Turno reservado en Lunes (Turno 4)")

&#x20;           else: print("Sin cupos disponibles para el Lunes.")



&#x20;       else:  #martes

&#x20;           if paciente == martes1 or paciente == martes2 or paciente == martes3:

&#x20;               print("Error: El paciente ya tiene un turno este día.")

&#x20;           elif martes1 == "": martes1 = paciente; print("Turno reservado en Martes (Turno 1)")

&#x20;           elif martes2 == "": martes2 = paciente; print("Turno reservado en Martes (Turno 2)")

&#x20;           elif martes3 == "": martes3 = paciente; print("Turno reservado en Martes (Turno 3)")

&#x20;           else: print("Sin cupos disponibles para el Martes.")



&#x20;   elif opcion == "2": #cancelar turno

&#x20;       dia = input("Elegir día (1=Lunes, 2=Martes): ")

&#x20;       paciente = input("Nombre del paciente a cancelar: ")

&#x20;       encontrado = False



&#x20;       if dia == "1":

&#x20;           if lunes1 == paciente: lunes1 = ""; encontrado = True

&#x20;           elif lunes2 == paciente: lunes2 = ""; encontrado = True

&#x20;           elif lunes3 == paciente: lunes3 = ""; encontrado = True

&#x20;           elif lunes4 == paciente: lunes4 = ""; encontrado = True

&#x20;       else:

&#x20;           if martes1 == paciente: martes1 = ""; encontrado = True

&#x20;           elif martes2 == paciente: martes2 = ""; encontrado = True

&#x20;           elif martes3 == paciente: martes3 = ""; encontrado = True

&#x20;       

&#x20;       if encontrado: 

&#x20;           print("Turno cancelado exitosamente.")

&#x20;       else:

&#x20;           print("No se encontró al paciente en la agenda.")



&#x20;   elif opcion == "3": # ver agenda

&#x20;       dia = input("Elegir día (1=Lunes, 2=Martes): ")



&#x20;       if dia == "1":

&#x20;           print(f"Lunes - Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")

&#x20;           print(f"Lunes - Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")

&#x20;           print(f"Lunes - Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")

&#x20;           print(f"Lunes - Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")

&#x20;       else:

&#x20;           print(f"Martes - Turno 1: {martes1 if martes1 != '' else '(libre)'}")

&#x20;           print(f"Martes - Turno 2: {martes2 if martes2 != '' else '(libre)'}")

&#x20;           print(f"Martes - Turno 3: {martes3 if martes3 != '' else '(libre)'}")



&#x20;   elif opcion == "4": # resumen general

&#x20;       

&#x20;       oc\_l = 0; oc\_m = 0  # Contadores,  

&#x20;       if lunes1 != "": oc\_l += 1

&#x20;       if lunes2 != "": oc\_l += 1

&#x20;       if lunes3 != "": oc\_l += 1

&#x20;       if lunes4 != "": oc\_l += 1

&#x20;       

&#x20;       if martes1 != "": oc\_m += 1

&#x20;       if martes2 != "": oc\_m += 1

&#x20;       if martes3 != "": oc\_m += 1



&#x20;       print(f"Lunes: {oc\_l} ocupados, {4-oc\_l} disponibles.")

&#x20;       print(f"Martes: {oc\_m} ocupados, {3-oc\_m} disponibles.")

&#x20;       

&#x20;       # Comparación de dias ocupados

&#x20;       if oc\_l > oc\_m: print("El día con más turnos es el Lunes.")

&#x20;       elif oc\_m > oc\_l: print("El día con más turnos es el Martes.")

&#x20;       else: print("Empate en cantidad de turnos ocupados.")



print("Sistema cerrado correctamente.")







print()







\# Variables iniciales

energia = 100

tiempo = 12

cerraduras\_abiertas = 0

alarma = False

codigo\_parcial = ""

racha\_forzar = 0  # Contador para regla anti-spam



\# Validación del nombre (Fuente 35, 37)

agente = input("Nombre del agente: ")

while not agente.isalpha():

&#x20;   agente = input("Error. Use solo letras para el nombre: ")



\# Ciclo principal 

while energia > 0 and tiempo > 0 and cerraduras\_abiertas < 3 and not (alarma and tiempo <= 3):

&#x20;   print(f"\\n--- ESTADO: Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras\_abiertas}/3 ---")

&#x20;   if alarma: print("¡ALERTA! Sistema de seguridad activo.")

&#x20;   

&#x20;   print("1. Forzar cerradura\\n2. Hackear panel\\n3. Descansar")

&#x20;   opcion = input("Acción: ")

&#x20;   

&#x20;   # Validación de opción

&#x20;   while not (opcion.isdigit() and "1" <= opcion <= "3"):

&#x20;       opcion = input("Error. Elija 1, 2 o 3: ")



&#x20;   if opcion == "1": # FORZAR CERRADURA

&#x20;       racha\_forzar += 1

&#x20;       energia -= 20

&#x20;       tiempo -= 2

&#x20;       

&#x20;       # Regla Anti-spam

&#x20;       if racha\_forzar == 3:

&#x20;           alarma = True

&#x20;           print("¡La cerradura se trabó por forzarla demasiado! Alarma activa.")

&#x20;       else:

&#x20;           # Riesgo de alarma por baja energía

&#x20;           if energia < 40:

&#x20;               print("RIESGO DE ALARMA (Baja energía)")

&#x20;               riesgo = input("Elija un número (1-3): ")

&#x20;               while not (riesgo.isdigit() and "1" <= riesgo <= "3"):

&#x20;                   riesgo = input("Invalido. Elija 1-3: ")

&#x20;               if riesgo == "3":

&#x20;                   alarma = True

&#x20;           

&#x20;           if not alarma:

&#x20;               cerraduras\_abiertas += 1

&#x20;               print("¡Cerradura abierta con éxito!")



&#x20;   elif opcion == "2": # HACKEAR PANEL

&#x20;       racha\_forzar = 0 # Rompe la racha (Regla anti-spam)

&#x20;       energia -= 10

&#x20;       tiempo -= 3

&#x20;       

&#x20;       # Ciclo FOR para progreso 

&#x20;       print("Hackeando...")

&#x20;       for i in range(1, 5): # 4 pasos

&#x20;           print(f"Paso {i}...")

&#x20;           codigo\_parcial += "A" # Acumulador de letras

&#x20;       

&#x20;       if len(codigo\_parcial) >= 8 and cerraduras\_abiertas < 3:

&#x20;           cerraduras\_abiertas += 1

&#x20;           print("¡Código descifrado! Una cerradura se abrió.")



&#x20;   elif opcion == "3": # DESCANSAR

&#x20;       racha\_forzar = 0 # Rompe la racha

&#x20;       recuperacion = 15

&#x20;       if alarma:

&#x20;           energia -= 10

&#x20;           print("Descanso difícil por la alarma (-10 energía extra)")

&#x20;       

&#x20;       energia += recuperacion

&#x20;       if energia > 100: energia = 100 # Límite máximo

&#x20;       tiempo -= 1

&#x20;       print("Has recuperado algo de energía.")



\# CONDICIONES DE FIN 

if cerraduras\_abiertas == 3:

&#x20;   print(f"\\n¡VICTORIA! El agente {agente} abrió la bóveda.")

elif energia <= 0 or tiempo <= 0:

&#x20;   print("\\nDERROTA: Te quedaste sin recursos.")

elif alarma and tiempo <= 3:

&#x20;   print("\\nDERROTA: El sistema se bloqueó por la alarma.")





print()







\#Código de "La Arena del Gladiador"



\#PASO 1: CONFIGURACIÓN 



\#Validación de nombre

nombre = input("Ingrese nombre del Gladiador: ")



while not nombre.isalpha():

&#x20;   print("Error: Solo se permiten letras")

&#x20;   nombre = input("Ingrese nombre del Gladiador: ")



\#PASO 2: INICIALIZACIÓN

vida\_gladiador = 100

vida\_enemigo = 100

pociones = 3

daño\_base\_pesado = 15

daño\_enemigo = 12

juego\_activo = True #Booleano para control



\# PASO 3: CICLO DE COMBATE

\#Se repite mientras ambos tengan vida

while vida\_gladiador > 0 and vida\_enemigo > 0:

&#x20;   print(f"\\n--- {nombre}: {vida\_gladiador} HP | Enemigo: {vida\_enemigo} HP | Pociones: {pociones} ---")

&#x20;   

&#x20;   # Menú del Jugador

&#x20;   print("1. Ataque Pesado")

&#x20;   print("2. Ráfaga Veloz")

&#x20;   print("3. Curar")

&#x20;   

&#x20;   opcion = input("Seleccione su acción: ")



&#x20;   # Validación estricta de número y rango



&#x20;   while not (opcion.isdigit() and "1" <= opcion <= "3"):

&#x20;       print("Error. Ingrese una opción válida (1, 2 o 3).")

&#x20;       opcion = input("Seleccione su acción: ")

&#x20;   

&#x20;   #Logica de las Acciones del Jugador

&#x20;   if opcion == "1": #Ataque Pesado

&#x20;       daño\_final = float(daño\_base\_pesado)

&#x20;       if vida\_enemigo < 20: #Golpe Critico

&#x20;           daño\_final = daño\_base\_pesado \* 1.5 #Uso de Float

&#x20;           print("¡GOLPE CRÍTICO!")



&#x20;       vida\_enemigo -= daño\_final

&#x20;       

&#x20;       print(f"¡Atacaste al enemigo por {daño\_final} puntos de daño!")

&#x20;       

&#x20;   elif opcion == "2": #Rafaga Veloz

&#x20;       print("¡Iniciando ráfaga!")

&#x20;       for i in range(3): #Se repite 3 veces

&#x20;           vida\_enemigo -= 5

&#x20;           print(" > Golpe conectado por 5 de daño")

&#x20;           

&#x20;   elif opcion == "3": #Curar

&#x20;       if pociones > 0:

&#x20;           vida\_gladiador += 30

&#x20;           if vida\_gladiador > 100: vida\_gladiador = 100

&#x20;           pociones -= 1

&#x20;           print("Te has curado 30 HP.")

&#x20;       else:

&#x20;           print("¡No quedan pociones! Pierdes el turno.")



&#x20;   #Turno del Enemigo (Si sigue vivo)

&#x20;   if vida\_enemigo > 0:

&#x20;       vida\_gladiador -= daño\_enemigo

&#x20;       print(f"¡El enemigo te atacó por {daño\_enemigo} puntos de daño!")



\#PASO 4: FIN DEL JUEGO

if vida\_gladiador > 0:

&#x20;   print(f"\\n¡VICTORIA! {nombre} ha ganado la batalla.")

else:

&#x20;   print("\\nDERROTA. Has caído en combate.")



