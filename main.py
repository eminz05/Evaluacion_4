import funcion as fn
compradores_iluminados={}
compradores_fortificados={}

stock_entradas={
    1:{"max": 500, "vendidas": 0},
    2:{"max": 500, "vendidas": 0}
    }

while True:
    print("TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE")
    print("1.- Comprar entrada a “Los Fortificados”.")
    print("2.- Comprar entrada a “Los Iluminados”.")
    print("3.- Stock de entradas para ambos conciertos.")
    print("4.- Salir.")

    try:
        opc=int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe ingresar un número entero.")

    if opc == 1:
        fn.comprar_entrada_fortificados(stock_entradas,compradores_fortificados)
    elif opc == 2:
        fn.comprar_entrada_iluminados(stock_entradas, compradores_iluminados)
    elif opc == 3:
        fn.muestra_entradas(stock_entradas)
    elif opc == 4:
        print("Programa terminado...")
        break
    else:
        print("Debe ingresar una opción válida!!")

