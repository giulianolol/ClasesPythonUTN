from funciones import *


def menu():
    primer_operando = ""
    segundo_operando = ""
    bandera_calculos_hechos = False
    while(True):
        print("MENU CALCULADORA\n1.Ingresar Primer Operando\n2.Ingresar Segundo Operando\n3.Calcular Todas las operaciones\n4.Informar Resultados\n5.Salir")
            
        opcion = input("Su opcion: ")
        
        if opcion == "1":
            
            primer_operando = input("Ingreso Primer Operando (A): ")
            
            while(primer_operando.isalpha()):
                print("El caracter ingresado no es valido!")
                primer_operando = input("Ingreso Primer Operando (A): ")           
                
            primer_operando = int(primer_operando)
            
        elif opcion == "2":
            
            segundo_operando = input("Ingreso Segundo Operando (B): ")
            
            while(segundo_operando.isalpha()):
                print("El caracter ingresado no es valido!")
                segundo_operando = input("Ingreso Segundo Operando (B): ")          
                
            segundo_operando = int(segundo_operando)
            
        elif opcion == "3":
            
            if(primer_operando == "" or segundo_operando == ""):
                
                print("Ingrese primero los dos valores...")
                
            bandera_calculos_hechos = True 
            suma = calcular_suma(primer_operando, segundo_operando)
            resta = calcular_resta(primer_operando, segundo_operando)
            division = calcular_division(primer_operando, segundo_operando)
            multiplicacion = calcular_multiplicacion(primer_operando, segundo_operando)
            potencia = calcular_potencia(primer_operando, segundo_operando)
            resto = calcular_resto(primer_operando, segundo_operando)
            factorial_A = calcular_factorial_A(primer_operando)
            factorial_B = calcular_factorial_B(segundo_operando)
                 
        elif opcion == "4":
            
            
            if(primer_operando == "" or segundo_operando == ""):
                
                print("Ingrese primero los dos valores...")
            
            if bandera_calculos_hechos == True:
                
                print(f"El resultado de A + B es: {suma}\n-El resultado de A - B es: {resta}\n-El resultado de A/B es: {division}\n-El resultado de A*B es: {multiplicacion}\n-A elevado a la B es: {potencia}\nEl resultado de A % B es: {resto}\nEl factorial de A es: {factorial_A}\nEl factorial de B es: {factorial_B}")
            
            else: print("Primero debe relizar los calculos.")
            
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opcion invalida ingrese números entre 1-5")     
menu()