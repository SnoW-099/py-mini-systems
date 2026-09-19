import random
import pyperclip
import json

# ==========================================
# 1. CARGAR DATOS PREVIOS
# ==========================================
try:
    with open("Contraseñas.json", "r") as archivo:
        contraseñas = json.load(archivo)
except FileNotFoundError:
    contraseñas = []
    print("Creando archivo nuevo... ")


# ==========================================
# 2. ENTRADA DE DATOS (CONFIGURACIÓN)
# ==========================================
while True:
    longitud = input("¿Que tan larga quieres que sea la clave? ")

    try:
        longitud = int(longitud)

        if longitud <= 0:
            print("La longitud debe ser mayor que 0 ")
        else:
            break

    except ValueError:
        print("La longitud debe ser un numero ")

mayus = input("Quieres usar mayusculas? (s/n) ").lower()
nums = input("Quieres usar numeros? (s/n) ").lower()
simbolos = input("Quieres usar simbolos? (s/n) ").lower()
copiar = input("Quieres copiar la contraseña al portapapeles? (s/n) ").lower()


# ==========================================
# 3. LÓGICA DE GENERACIÓN
# ==========================================
mayusG = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numsG = "1234567890"
simbolosG = "@%&#$"
minusG = "abcdefghijklmnopqrstuvwxyz"

caracteres = minusG

if mayus == "s":
    caracteres += mayusG

if nums == "s":
    caracteres += numsG

if simbolos == "s":
    caracteres += simbolosG

contraseña = ""
for i in range(longitud):
    contraseña += random.choice(caracteres)


# ==========================================
# 4. GUARDAR Y MOSTRAR RESULTADOS
# ==========================================
if contraseña not in contraseñas:
    contraseñas.append(contraseña)
    with open("Contraseñas.json", "w") as archivo:
        json.dump(contraseñas, archivo, indent=4)
else:
    print("Contraseña ya existente ")

print("\nTu contraseña final es: ", contraseña)


# ==========================================
# 5. OPCIONES ADICIONALES
# ==========================================
ver = input("Quieres ver las contraseñas guardadas? (s/n) ").lower()

if ver == "s":
    print("\nContraseñas guardadas:")
    for c in contraseñas:
        print("-", c)

if copiar == "s":   
    pyperclip.copy(contraseña)
    print("Contraseña copiada al portapapeles correctamente!! ")