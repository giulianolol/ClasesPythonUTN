from funciones import *

print("Las fechas estan siendo formateadas para el correcto funcionamiento del programa ... ")

proyectos = cargar_y_formatear_fechas('Proyectos.csv')

guardar_datos('Proyectos.csv', proyectos)

time.sleep(2.5)

print("Las fechas fueron formateadas exitosamente.")

time.sleep(1)

tecla = input("Pulse cualquier tecla para continuar :)")

imprimir_menu()

menu_funcional(tecla)