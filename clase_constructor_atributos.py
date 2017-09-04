class holamundo:

    def __init__(self, nombre): #el constructor, creamos atributos con self.[variable]
        self.atributo = nombre

    def saluda(self):
        print("Hola ",self.atributo)

    def cambia(self, nombre):
        self.atributo = nombre

#instanciamos la clase pasandole in parámetro al constructor
instancia = holamundo('David')

#llamamos a un métod que muestra el atributo pasado en el constructor
instancia.saluda()

#cambiamos el valor del atributo de la instancia
instancia.cambia('Mercedes')

#llamamos a un método que muestra el nuevo atributo cambiado
instancia.saluda()
