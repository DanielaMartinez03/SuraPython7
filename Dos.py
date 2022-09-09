#Variables con elementos del mismo tipo
#Lista de numeros pares

numerosPares = [] 
#Generar un ciclo while que de 10 vueltas 

x=0
while(x<10):
    numero=(int(input("Digite un número par")))
    if(numero % 2 ==0 ):
        numerosPares.append(numero) #El appen se utiliza para guardar los datos a la lista vacia
        x=x+1
#Para recorrer una lista se hace con un for   
for i in numerosPares:
    print(i)

    #Las listas se llenan con elementos
    #Los Diccionarios se llenan con atributos (Palabras)



