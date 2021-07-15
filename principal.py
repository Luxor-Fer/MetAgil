def logicaFibonacci (op):
    numUno = 0
    numDos = 1
    numSop = 0
    detener = True
    print(numUno)
    print(numDos)
    while detener:
        numSop = numUno + numDos
        print(numSop)
        numUno = numDos
        numDos = numSop
        if ( op <= numSop ):
            detener = False
print("Gracias por utilizar nuestro Programa")
num = int (input("Puedes ingresar un número para mostrar la serie de fibonacci del número?\n"))
logicaFibonacci (num)