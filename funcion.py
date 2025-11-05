def comprar_entrada_fortificados(stock_entradas,compradores_fortificados):
    nombre=input("Ingrese un nombre: ").strip().title()

    if nombre in compradores_fortificados:
        print("El nombre ya ha sido registrado.")
        return
    
    tipo_entrada=input("Ingrese tipo de entrada (CV/PAL): ")

    if tipo_entrada is not ["G","V"]:
        print("Inválido. Debe ingresar G o V")
        return
    
    while True:
        codigo=input("Ingrese código de confirmación: ").strip()
        if len(codigo) < 6:
            print("Código no válido. Intente otra vez.")
            return
        
        codigo=any(c.upper() for c in codigo)
        codigo=any(c.isdigit() for c in codigo)


def comprar_entrada_iluminados(stock_entradas, compradores_iluminados):
    nombre=input("Ingrese un nombre: ").strip().title()

    if nombre in compradores_iluminados:
        print("El nombre ingresado ya ha sido registrado")
        return
    
    tipo_entrada=input("Ingrese tipo de entrada (CV/PAL): ")

    if tipo_entrada is not ["CV","PAL"]:
        print("Inválido. Debe ingresar CV o PAL.")
        return
    
    while True:
        codigo=input("Ingrese código de confirmación: ").strip()
        if len(codigo) < 5:
            print("Código no válido. Intente otra vez.")
            return
        
        codigo=any(c.upper() for c in codigo)
        codigo=any(c.isdigit() for c in codigo)

def muestra_entradas(stock_entradas):
    stock_actual_fortificados= stock_entradas-1
    stock_actual_iluminados= stock_entradas-1

    print(f"Stock de entradas para 'Los Fortificados': {stock_actual_fortificados}")
    print(f"Stock de entradas para 'Los Iluminados': {stock_actual_iluminados}")


