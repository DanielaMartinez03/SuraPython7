#Menu
x=0
empanadas=[]


print("1.Agregar empanadas")
print("2.Agregar empanadas")
print("3.Salir")

while(x!=3):
    Ingredientes=[]
    empanada={}

    x=int(input("Digite la opción"))
    if(x==1):
        empanada['Nombre']=input("Ingrese nombre empanada")
        Ingredientes.append(input("Ingrese el ingrediente 1"))
        Ingredientes.append(input("Ingrese el ingrediente 2"))
        Ingredientes.append(input("Ingrese el ingrediente 3"))
        empanada['Ingredientes']=Ingredientes
        empanada['precio']=int(input("Ingrese el precio"))
        empanadas.append(empanada)
        print("Agregando empanada")
    elif(x==2):
        print("Mostrando empanada")
        print(empanadas)
    elif(x==3):
        print(" Salir ")
        break
    else:
        print("Opcion no valida")