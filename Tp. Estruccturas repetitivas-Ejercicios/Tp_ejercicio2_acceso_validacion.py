# ejercicio 2 - Acceso al Campus y Menú Seguro

#usuario correcto: alumno
#clave correcta: python123

usuario_esperado = "alumno"
clave_esperada = "python123"
intento_max = 3
intento = 1
acceso_concedido = False

print(f"intento {intento} ingrese usuario y clave:")
usuario = input("Nombre: ")
clave = input("Clave: ")

while not (usuario_esperado == usuario and clave_esperada == clave) and intento < intento_max :
    print(f"intento {intento + 1}. Credenciales invalidas, ingrese usuario y clave: ")
    usuario = input("Nombre: ")
    clave = input("Clave: ")
    intento += 1

if usuario == usuario_esperado and clave == clave_esperada:
    acceso_concedido = True
    print("Acceso concedido")
else:
    print("Cuenta bloqueada")

if not acceso_concedido:
    print("Intentelo mas tarde")

else:
    opcion = ""

    while opcion != "4":  #ciclo por bandera.
        print("Acceso al Menu")
        print("1. Ver estado de inscripción")
        print("2. Cambiar clave")
        print("3. Mostrar mensaje motivacional")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        while not (opcion.isdigit() and "1" <= opcion <= "4"):
            print("Error. Ingrese un valor entre 1 y 4")
            opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("Estado: Inscripto")

        elif opcion == "2":
            nueva_clave = input("Ingrese su nueva clave: ")
            confirmacion = input("Confirme su nueva clave: ")
            
            if (nueva_clave == confirmacion) and len(nueva_clave) >= 6:
                print("¡Clave cambiada con éxito!")
            else:
                print("Error, minimo seis caracteres")

        elif opcion == "3":
            print("Frase del día: La disciplina es la base del exito")

        else:
            print("Opción no válida. Por favor, intente de nuevo.")

    print("Programa finalizado.")
















