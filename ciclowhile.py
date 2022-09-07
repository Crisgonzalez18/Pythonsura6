#ciclo mientras

# DECLARAR UNA VARIABLE CENTINELA

#O VARIABLE DE CONTROL PARA EVALUAR LA EJECUCION DE MI CICLO



i = 0
numero1 = 0
numero2 = 0

#menu de opciones

numero1=int(input("Digite el primer numero"))
numero2=int(input("Digite el segundo numero"))
   

print("***MENU***")
print("1. sumar dos numeros")
print("2. restar dos numeros")
print("3. encontrar la raiz cuadrada de un numero")
print("4. multiplicar dos numeros")
print("5. salir")

#Progamar la estructura del ciclo mientras

while(i!=5):

   i=int(input("Digite una opcion del menu"))
    
    if(i==1):
        print("la suma de ",numero1," y ",numero2,"es igual a ",numero1+numero2)
    elif(i==2):
        print("chao amor")
    elif(i==3):
        print("ganador el rojo")
    elif(i==4):
        print("No llueve en medallo")
    elif(i==5):
        break
    else:

        print("Esa no es una opcion valida")