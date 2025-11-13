from calculos import areatri,areacuadra,areacirculo #Aqui se importar funciones de calculos
from funtions import sumar #Aqui se importa funciones desde funtions
print("Hola Mundo") #Imprime Hola Mundo

menu_interactivo = True
while menu_interactivo:
    print("                                    ")
    print("----------Menu principal-------------")
    print("1 - Area triangular")
    print("2 - Area cuadrada")
    print("3 - Suma")
    print("4 - Area Circular")
    print("5 - Salir")
    print("                     ")
    opcion = input("Elije una opcion: ")

    if opcion =="1":
        base = float(input("Ingrese numero 1: "))
        altura = float(input("Ingrese numero 2: "))
        resultado = areatri(base,altura) 
        print(f"Resultado Area Triangular: {resultado}")
           

    if opcion =="2":
        lado = float(input("ingrese el valor del lado: "))
        resultado = areacuadra(lado) 
        print(f"El area cuadrada es: {resultado}")

    if opcion =="3":
        num1 = float(input("Ingrese numero 1: "))
        num2 = float(input("Ingrese numero 2: "))
        resultado = sumar(num1,num2)
        print(f"Resultado de la suma: {resultado}")
    if opcion =="4":
        radio =float(input("Ingrese el radio del circulo: "))
        resultado = areacirculo(radio)
        print(f"El area del circulo es: {resultado}")

    if opcion =="5":
        print("Saliendo del programa") 
        break

