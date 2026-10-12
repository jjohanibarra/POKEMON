from clases.pokemon import Pokemon

def menu():
    lista_pokes = []
    
    while True:
        print("MENU DE POKEMON")
        print("1. capturar pokemon")
        print("2. entrenar pokemonn")
        print("3. ver todos")
        print("4. ver total de pokemons")
        print("5. liberar pokemonn")
        print("6. salir")
        
        op = input("elije una opcion: ")
        
        if op == "1":
            nom = input("nombre del pokemon: ")
            tip = input("tipo: ")
            atq = int(input("ataque: "))
            dfn = int(input("defensa: "))
            sld = int(input("salud: "))
            p = Pokemon(nom, tip, atq, dfn, sld)
            lista_pokes.append(p)
            print("pokemonn guardao con exito")
            
        elif op == "2":
            if len(lista_pokes) == 0:
                print("no hay pokemons para entrenar")
            else:
                print("elije cual pokemon entrenar:")
                for i in range(len(lista_pokes)):
                    print(str(i) + " - " + lista_pokes[i].nombre)
                idx = int(input("numero de la lista: "))
                if idx >= 0 and idx < len(lista_pokes):
                    extra = input("quieres entrenar algo especifico? (escribe ataque, defensa o salud, o enter para todo): ")
                    if extra == "":
                        lista_pokes[idx].entrenar()
                    else:
                        lista_pokes[idx].entrenar(extra)
                else:
                    print("numero invalido")
                    
        elif op == "3":
            if len(lista_pokes) == 0:
                print("no hay pokemones registrados")
            else:
                for p in lista_pokes:
                    p.mostrar_info()
                    
        elif op == "4":
            Pokemon.total_pokemons()
            
        elif op == "5":
            if len(lista_pokes) == 0:
                print("no hay pokemons pa liberar")
            else:
                for i in range(len(lista_pokes)):
                    print(str(i) + " - " + lista_pokes[i].nombre)
                idx = int(input("cual vas a borrar?: "))
                if idx >= 0 and idx < len(lista_pokes):
                    del lista_pokes[idx]
                    print("pokemon borrao")
                else:
                    print("opcion mal")
                    
        elif op == "6":
            print("saliendo...")
            break
        else:
            print("opcion no valida")

if __name__ == "__main__":
    menu()