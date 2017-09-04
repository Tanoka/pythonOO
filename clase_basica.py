#declaramos una clase 
class holamundo:

    def dihola(self): #cada método lleva un parametro self,  
                    #el toma el valor por defecto de la instancia al llamar a un metodo
        print("Hola")

    def saluda(self, param):
        print("Hola ", param)

#instanciamos la clase
instancia = holamundo()

#Llamamos a un método
instancia.dihola()

#Llamamos a un método y le pasamos un parámetro
instancia.saluda('david')


