class Automovil:
    def __init__ (self,color, numero_puertas, matricula):
        self.numero_puertas = numero_puertas
        self.color = color
        self.matricula = matricula

    def imprimir (self):
        print (self.numero_puertas)
        print (self.color)
        print (self.matricula)

    def cambio_color (self, color):
        self.color = color


auto_uno = Automovil ('Amarillo',4,1234)
auto_uno.cambio_color(input('Que color desea que sea su automovil: '))
auto_uno.imprimir()
auto_dos = Automovil ('rojo',5,'0123')
auto_dos.imprimir()
#print(auto_uno)
if (auto_dos.color == 'verde'):
    print ('hola')
else:
    print( 'no es verde')