##Construir un programa que reciba números enteros y los sume
#mientras estos sean positivos, si se digita un número negativo el
#programa debe terminar
'''
numerospares =[]
pares=0
suma=0

while(pares>=0):
    pares = int(input("Ingrese un numero Par"))
    numerospares.append(pares)
    suma=sum(numerospares)
    if ( pares <0):
        break
    else:
        print(suma)

print(f'la suma de numeros ingresados es ',suma)

Mostrar los números del 1 al 200 saltando de 12 en 12(1,12,24…)


for num in range(1, 201):
    print(num)
#falta solo el que se muestren cada 12 


Codificar un programa que presente un menú de 4 opciones y
reciba un numero natural para realizar las siguientes operaciones:
0: Salida
1: Encuentre si el número es múltiplo de 2
2: Encuentre la raíz cuadrada del número
3: Sume 100 al número ingresado
4: Eleve a la 2 el número ingresado


import math
numero = 0
opcion=0

print("------>>>>MENU<<<<------")
print("1: Encuentre si el número es múltiplo de 2")
print("2: Encuentre la raíz cuadrada del número")
print("3: Sume 100 al número ingresado")
print("4: Eleve a la 2 el número ingresado")
print("5: Salida")

while(opcion!=5):
    opcion = int(input("de las siguientes opciones, digite el numero a la opcion que corresponde: -->"))
    if(opcion==1):
        numero = int(input("digite un numero para saber si es multiplo de dos: -->"))
        if(numero%2==0):
            print(numero,' es un multiplo de dos')
        else:
            print(numero,' NO es un multiplo de dos')
    elif(opcion == 2):
        numero = int(input("digite un numero para hallar la raiz cuadrada: -->"))
        Raiz = 0
        Raiz = math.sqrt(numero)
        print('del numero',numero,' su raiz cuadrada es= ',Raiz)
    elif(opcion == 3):
        numero = int(input("digite un numero para sumarle 100: -->"))
        suma=0
        suma=numero+100
        print('el resultado de sumar 100 al numero',numero,' es= ',suma)
    elif(opcion == 4):
        numero = int(input("digite un numero para hallar la potencia la cuadrado: -->"))
        potencia=0
        potencia = numero**2   
        print('para el numero',numero,' elevado a la dos es =',potencia)    
    elif(opcion==5):
        print('hasta una proxima oportunidad... programa finalizado')
        break
    else:
        print('ingrese una opcion del menu')
    
Una compañía de software contable, paga a su personal de ventas un salario de
3500000 mensuales, mas una comisión de 1500000 por cada licencia de
software vendida menos el 5 del salario total comisiones de deducciones)
por impuestos Codifica un programa que calcule e imprima el salario mensual
de un vendedor dado recibiendo el numero de ventas realizadas

'''