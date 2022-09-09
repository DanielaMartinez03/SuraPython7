#Menu de dos opciones
x=0

print("***Menu***")
print("1.Mostrar Pueblo")
print("2.Mostrar Ruta")
print("3. Poblacion")
print("4. Salir")

pueblos=[]
while(x!=4):
    pueblo={}

    x=int(input("Digite la opcion del menú"))
    if(x==1):
        print("Mostrando Pueblo")
        pueblo['Nombre']=input("Ingrese el nombre del pueblo a visitar ")
        pueblo['Distancia']=input("Ingrese la distancia ")
        pueblo['Poblacion']=input("Ingrese la poblacion del pueblo ")
        pueblos.append(pueblo)
    elif(x==2):
        print("Mostrando Ruta")
        print(pueblos)
    elif(x==3):
        print("Mostrando Poblacion")
        print(pueblos)
    elif(x==4):
        print("Saliendo")
        break
    else:
        print("Opcion no valida")   
    