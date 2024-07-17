import random
import os
import csv
import math

lista_empleados_vacia = []

#empleados sin sueldos asignados
lista_empleados = [
    ["Juan Perez", 0],
    ["Maria Garcia", 0],
    ["Carlos Lopez", 0],
    ["Ana Martinez", 0],
    ["Pedro Rodriguez", 0],
    ["Laura Hernandez", 0],
    ["Miguel Sanchez", 0],
    ["Isabel Gomez", 0],
    ["Francisco Diaz", 0],
    ["Elena Fernandez", 0],
]

#agregar detalles de sueldos a la lista
def emp_detalles(nombre, sueldo):
    lista_empleados_vacia.append([nombre, sueldo])

#guardar los datos en un archivo CSV
def guardar_datos():
    nombre_archivo = 'sueldos.csv'
    with open(nombre_archivo, 'w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Nombre', 'Sueldo', 'Descuento Salud', 'Descuento AFP', 'Sueldo Liquido'])  #encabezados
        for empleado in lista_empleados_vacia:
            nombre, sueldo = empleado
            descuento_salud = round(sueldo * 0.07, 2)
            descuento_afp = round(sueldo * 0.12, 2)
            sueldo_liquido = round(sueldo - descuento_salud - descuento_afp, 2)
            writer.writerow([nombre, sueldo, descuento_salud, descuento_afp, sueldo_liquido])

    print(f'Se ha creado el archivo "{nombre_archivo}" correctamente.')

#cargar datos en lista_empleados_vacia
def cargar_datos():
    lista_empleados_vacia.clear()  # Limpiar la lista antes de cargar nuevos datos
    for empleado in lista_empleados:
        global nombre, sueldo
        nombre = empleado[0]
        sueldo = random.randint(300000, 2500000)
        emp_detalles(nombre, sueldo)
    print("Datos cargados!")

#listas para clasificar sueldos
sueldos_altos = []
sueldos_medios = []
sueldos_bajos = []

def menu_sueldos():
    global nm, ni, nb
    nm = ni = nb = 0
    os.system("cls")
    sueldos_bajos.clear()
    sueldos_medios.clear()
    sueldos_altos.clear()
    for empleados in lista_empleados_vacia:
        sueldo = empleados[1]
        nombre = empleados[0]
        if sueldo >= 2000000:
            nm += 1
            sueldos_altos.append([nombre, sueldo])
        elif 800000 <= sueldo < 2000000:
            ni += 1
            sueldos_medios.append([nombre, sueldo])
        else:
            nb += 1
            sueldos_bajos.append([nombre, sueldo])

    mostrar_sueldos()

def mostrar_sueldos():
    os.system("cls")
    
    # Sueldos menores a $800.000
    print(f"Sueldos Menores a $800.000 Total: {nb}")
    print("Nombre Empleado           Sueldo")
    for empleado in sueldos_bajos:
        if empleado[1] < 800000:
            print(f"{empleado[0]:<25} {empleado[1]}")
    
    # Sueldos entre $800.000 y $2.000.000
    print(f"\nSueldos entre $800.000 y $2.000.000 Total: {ni}")
    print("Nombre Empleado           Sueldo")
    for empleado in sueldos_medios:
        if 800000 <= empleado[1] < 2000000:
            print(f"{empleado[0]:<25} {empleado[1]}")
    
    # Sueldos superiores a $2.000.000
    print(f"\nSueldos Superiores a $2.000.000 Total: {nm}")
    print("Nombre Empleado           Sueldo")
    for empleado in sueldos_altos:
        if empleado[1] >= 2000000:
            print(f"{empleado[0]:<25} {empleado[1]}")

def estadisticas_sueldos():
    promedio = 0
    sueldo_alto = float('-inf')  # Inicializamos con un valor muy bajo
    sueldo_bajo = float('inf')
    empleado_sueldo_alto = empleado_sueldo_bajo = ""
    total_sueldos = 0
    
    for empleado in lista_empleados_vacia:
        sueldo = empleado[1]
        total_sueldos += sueldo
        if sueldo > sueldo_alto:
            sueldo_alto = sueldo
            empleado_sueldo_alto = empleado[0]
        if sueldo < sueldo_bajo:
            sueldo_bajo = sueldo
            empleado_sueldo_bajo = empleado[0]
    
    promedio = total_sueldos / len(lista_empleados_vacia)

    print(f"\nEmpleado con el sueldo más alto: {empleado_sueldo_alto}, Sueldo: {sueldo_alto}")
    print(f"\nEmpleado con el sueldo más bajo: {empleado_sueldo_bajo}, Sueldo: {sueldo_bajo}")
    print(f'El promedio de los sueldos es de: {promedio:.2f}')
    
def calcular_media_geometrica(sueldos):
    producto_total = 1
    for sueldo in sueldos:
        producto_total *= sueldo
    
    n = len(sueldos)
    if n > 0:
        media_geom = producto_total ** (1 / n)
    else:
        media_geom = 0
    
    return media_geom

# Menú principal del programa
opciones_ini = 0

while True:
    os.system("cls")
    print('''
        Menu:
          
    1- Asignar Sueldos.
    2- Clasificar empleados por sueldo
    3- Ver estadisticas
    4- Generar reporte
    5- Salir
    ''')
    
    try:
        opciones_ini = int(input("Ingrese una opción: "))
        if opciones_ini == 1:
            cargar_datos()
            os.system("pause")

        elif opciones_ini == 2:
            menu_sueldos()
            os.system("pause")

        elif opciones_ini == 3:
            estadisticas_sueldos()
            sueldos = [empleado[1] for empleado in lista_empleados_vacia]  # Obtener lista de sueldos
            media_geom = calcular_media_geometrica(sueldos)
            print("La media geométrica de los sueldos es aproximadamente:", round(media_geom, 2))
            os.system("pause")

        elif opciones_ini == 4:
            print("REPORTE SUELDOS")
            menu_sueldos()
            guardar_datos()
            os.system("pause")

        elif opciones_ini == 5:
            print("Saliendo del programa")
            print("Desarrollado por Kevin Gallardo \n RUT 21.619.419-5")
            break

    except Exception as e:
        print("Error de ingreso:", e)
        os.system("pause")