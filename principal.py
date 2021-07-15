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

logicaFibonacci (6)