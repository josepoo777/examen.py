import random 
import csv
import math 

opc= 0

lista_trabajador= ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]

sueldos={}
inventario={}

def asignar_sueldos_cantidades():
    global inventario
    inventario ={}
    for lista_trabajadores in lista_trabajador:
        inventario=[lista_trabajadores]={
        "sueldos": random.randint(300000,2500000),
        "cantidad": random.randint (1,10)
        }
        
    print("sueldos y cantidades asignados aleatoriamente")

def clasificar_sueldos ():
    clasificacion={"menor":[],"moderado":[],"mayores":[]}
    for trabajadores,datos in inventario.items():
        sueldos=datos ["sueldos"]
        if sueldos < 300000:
            clasificacion["menor"].append(trabajadores) 
        if sueldos >= 2500000:
            clasificacion ["moderado"].append(trabajadores)
        else:
            clasificacion["mayores"].append(trabajadores)
    print("clasificacion ")
    for categoria,lista in clasificacion.items():
        print(f"{categoria}: "," .join(lista)")
    print()

def ver_estadisticas():
    sueldos= [datos["sueldo"] for datos in inventario.values()]
    cantidad =[datos["cantidad"] for datos in inventario.values()]

    estadisticas={
        "sueldo_mas_alto":max(inventario,key=lambda k:inventario [k]["sueldo"]),
        "sueldo_mas_bajo":min(inventario,key=lambda k:inventario[k]["sueldo"]),
        "promedio_de_sueldo":sum(sueldos)/ len(sueldos), 
        "media_gemotrica":math.exp(sum(math.log)),
        "valor_total":sum(datos["sueldos"]*datos["cantidad"] for datos in inventario.values() )
        }
    for clave,valor in estadisticas.items():
        print(f"{clave}:{valor}")
    print()

def generar_reporte():
    archivo_csv="datos.scv"
    with open (archivo_csv,mode="w",newline="") as archivo:
        escritor=csv.writer(archivo)
        escritor.writerow(["trabajadores","sueldos","descuento_salud","descuento_afp","valor total"])
        for trabajadores,datos in inventario.items():
            sueldos=datos["sueldos"]
            descuento_afp=sueldos*0.12
            descuento_salud=sueldos*0.7
            descuento_total=sueldos-descuento_afp-descuento_salud
            valor_total=descuento_total*sueldos
            escritor.writerow([trabajadores,sueldos,descuento_salud,descuento_afp])
        print(f"reporte generado:{archivo_csv}")
def menu():
    while True:
        print('''
            1. Asignar sueldos aleatorios
            2. Clasificar sueldos
            3. Ver estadísticas.
            4. Reporte de sueldos
            5. Salir del programa
              ''')
        opc=input("ingrese una opcion: ")

        while not opc.isnumeric():
            print("eso no es un numero")
            opc=input("ingrese una opcion: ")
        opc=int(opc)

        if opc==1:
            inventario=asignar_sueldos_cantidades ()
            print("se asigan sueldos y cantidades aleatoriamente")
        elif opc ==2:
            clasificacion=clasificar_sueldos(inventario)
            for categoria,trabajador in clasificacion.items():
                print(f"{categoria}:{sueldos}")
        elif opc ==3:
            estadisticas= ver_estadisticas (inventario)
            print("estadisticas")
            for clave,valor in estadisticas.items():
                print(f"{clave} {valor}")        
        elif opc ==4:
            archivo_csv="reporte.csv"
            generar_reporte(inventario,archivo_csv)
            print(f"reporte generado: {archivo_csv}")
        elif opc == 5 :
            print("saliendo del programa..................")
            break 
if __name__=="__main__":
   menu()