def main():
    name=input("Holaaa de nuevo, ingresa tu nombre: ")
    age=int(input("Ingresa tu edad: "))
    e=input("Ingresa 3 videojuegos separados por comas: ").strip()
    games=e.split(",")
    perfil=[name]
    yob=2025-age
    perfil.append(yob)
    perfil.extend(games)
    perfil.insert(0, True)
    fav_game=perfil.pop(3)

    #* Comprobaciones Logicas
    
    if age>=18:
        mayor_edad=True
    else: mayor_edad=False

    if len(name)>10:
        nombre_largo=True
    else: nombre_largo=False

    if games.count("pacman"):
        gamer_retro=True
    else: gamer_retro=False
    
    #? Impresiones

    print("-"*20)
    print("---Perfil---\n")
    print(f"En linea? {perfil[0]}\nNombre: {perfil[1]}\nAño de nacimiento: {perfil[2]}\nJuegos: {perfil[3:]}")
    print(f"Juego favorito: {fav_game}")
    print("-"*20)
    print("---Comprobaciones logicas---\n")
    print(f"Mayor de edad? {mayor_edad}\nNombre largo? {nombre_largo}\nGamer retro? {gamer_retro}")
    print("-"*20)

main()