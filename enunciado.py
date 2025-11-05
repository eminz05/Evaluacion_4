""" Haga un programa que permita generar un menú de gestión de entradas para el Concierto de Rock “los Fortificados” y al concierto “Los Iluminados”. El menú principal debe permitir mostrar 4 opciones:
TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE
1.- Comprar entrada a “los Fortificados”.
2.- Comprar entrada a “los Iluminados”.
3.- Stock de entradas para ambos conciertos.
4.- Salir.
Todas las opciones del menú deben estar implementadas mediante funciones se-paradas del código principal (main).
Al ingresar a la opción 1.- Comprar entrada a “los Fortificados” se debe permitir ingresar nombre de comprador, tipo de entrada y código de confirmación por separado. Para que la compra sea exitosa se debe cumplir lo siguiente: a) el nombre de comprador no debe estar repetido, b) el tipo de entrada solo permite “G” (General) o “V” (VIP), c) el código de confirmación debe tener largo mínimo de 6 caracteres, 
debe tener al menos 1 letra mayúscula, al menos 1 número y no puede tener espacio en blanco.
En caso de cumplir todas las condiciones, la entrada se registra exitosamente.
Al ingresar la opción 2.- Comprar entrada a “los Iluminados”, se debe permitir ingresar nombre de comprador, tipo de entrada y código de confirmación por separado. 
Para que la compra sea exitosa se debe cumplir lo siguiente: 
a) el nombre de comprador no debe estar repetido, b) el tipo de entrada solo permite “CV” (Cancha VIP) o “Palco” (PAL),

2
c) el código de confirmación debe tener largo mínimo de 5 caracteres, debe tener al menos 3 letra mayúscula, al menos 1 número y no puede tener espacio en blanco.
Al ingresar la opción 3.- Stock de entradas, el menú debe permitir mostrar todas las entradas disponibles para cada uno de los conciertos. Para esto, se dispondrá de un stock de 500 entradas para para cada uno de los conciertos.
Al ingresar la opción 4.- Salir, el programa debe terminar mostrando:
Programa terminado...
Si se ingresa una opción distinta (que no sea 1, 2, 3 o 4), debe mostrarse:
Debe ingresar una opción válida!! """