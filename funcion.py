def comprar_entrada_iluminados(stock_entradas,compradores_iluminados):
    nombre=input("Ingrese un nombre: ").strip().title()

    if nombre in compradores_iluminados:
        print("El nombre ingresado ya ha sido registrado")
        return
    
    tipo_entrada=input("Ingrese tipo de entrada (G/V):")

    if tipo_entrada is not ["G","V"]:
        print("Inválido. Debe ingresar G o V")
        return
    
    codigo_verificador=input("Ingrese código de confirmación: ").strip().upper()

    any(c.upper() for c in codigo_verificador)
    any(c.isdigit() for c in codigo_verificador)

    

