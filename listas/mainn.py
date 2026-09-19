Juegos = ["Fortnite", "Minecraft", "COD", "Valorant", "LOL"]

nuevo_juego = input("ingrese un juego: ")
Juegos.append(nuevo_juego)

print(Juegos[2])
print(Juegos)
print("------------------")

eliminar_juego = input("Desea eliminar algun juego de la lista? (si/no): ").lower()

if eliminar_juego == "si":
    juego_que_eliminar = input("Ingrese el nombre del un juego que desea eliminar: ")

    if juego_que_eliminar in Juegos:
        Juegos.remove(juego_que_eliminar)
        print(f"El juego {juego_que_eliminar} ha sido eliminado de la lista.")
    else:
        print(f"El juego {juego_que_eliminar} no se encuentra en la lista.")

elif eliminar_juego == "no":
    print("No se ha eliminado ningun juego.")

pregunta = input("Quiere ver la lista de juegos? (si/no): ").lower()

if pregunta == "si":
    for juego in Juegos:
        print(juego)

    pregunta_Juego = input("Quieres buscar un juego en especifico? (si/no): ").lower()

    if pregunta_Juego == "si":
        Que_Juego = input("Cual es el juego q quieres buscar?: ")

        if Que_Juego in Juegos:
            print(f"el juego {Que_Juego} Esta en la lista de juegos")
        else:
            print("El juego q buscas no esta en la lista")

pregunta2 = input("Una ultima pregunta, quieres modificar la lista? (Si/No): ").lower()

if pregunta2 == "si":
    Que_juego_sus = input("Que juego quieres sustituir?: ")
    Que_juego_add = input("Que juego quieres añadir?: ")

    if Que_juego_sus in Juegos:
        position = Juegos.index(Que_juego_sus)
        Juegos[position] = Que_juego_add

        print(f"{Que_juego_sus} ha sido correctamente sustituido por: {Que_juego_add}, lista actual: ")

        for juego in Juegos:
            print(juego)
    else:
        print("No hay coincidencias")

else:
    print("ok, hasta luego")