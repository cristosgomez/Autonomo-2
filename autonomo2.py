#importar librerias
import random
import string

#Tipos de datos a usar en contraseña
LETRAS      = string.ascii_letters        
NUMEROS     = string.digits           
ESPECIALES  = "!@#$%^&*()-_=+[]{}|;:,.<>?" 

TODOS       = LETRAS + NUMEROS + ESPECIALES

#obtencion de datos
print(" ##Trabajo Autonomo 2##")
print(" GENERADOR DE CONTRASEÑAS SEGURAS")
nombre = input("\nHola! ¿Cuál es tu nombre? ").strip()

#asignación de usuario en caso de que no desee ingresar su nmbre
if nombre == "":
    nombre = "Usuario"

print(f"\nBienvenido, {nombre}!")

##Obtencion largo de contraseña con bucle para multiples intentos
while True:
    try:
        largo = int(input("\n¿Cuántos caracteres quieres para tu contraseña? (mínimo 8): "))

        if largo < 8:
            print("La contraseña debe tener al menos 8 caracteres. Intenta de nuevo.")
        else:
            break

    except ValueError:
        print("Por favor ingresa un número válido.")

#Se obtiene cada caracter obligatorios
obligatorios = [
    random.choice(LETRAS),
    random.choice(NUMEROS),
    random.choice(ESPECIALES),
]
##generacion de cadena nueva para contraseña
resto = [random.choice(TODOS) for _ in range(largo - len(obligatorios))]

## creacion de contraseña final
contrasena_lista = obligatorios + resto
random.shuffle(contrasena_lista)

##limpiesza de espacios
contrasena = "".join(contrasena_lista)

##impresion de información
print("\n" + "=" * 45)
print(f"  Tu contraseña nueva es:")
print(f"\n  {contrasena}")
print("\n" + "=" * 45)
print(f"Con un largo    : {largo} caracteres")
print(f"  Contiene : letras, números y símbolos")
print("=" * 45)
print("\n¡Guárdala en un lugar seguro!")
