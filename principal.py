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

def validarValor (valor):
    try:
        return int (valor)
    except ValueError:
        print ("Debe ingresar solo números")
        return "errorNumeros"

print("Gracias por utilizar nuestro Programa")
num = validarValor ( input ("Ingrese un valor para mostrar la serie de Fibonacci:\n"))

if ( num != "errorNumeros"):
    if ( num <= 0):
        print ("La suseccion de Fibonacci empieza desde el 0 por ejemplo:")
        logicaFibonacci(2)
    else:
        logicaFibonacci (num)