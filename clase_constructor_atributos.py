class holamundo:

    def __init__(self, nombre): #el constructor, creamos atributos con self.atributo
        """ El contructor siempre es __init__ .los métodos con __[nombre]__ son especiales
            Los atributos de instancia se declaran con self.[atributo]"""
        self.atributo = nombre

    def saluda(self):
        print("Hola ",self.atributo)

    def cambia(self, nombre):
        "Modifico un atributo de instancia"
        self.atributo = nombre


#instanciamos la clase pasandole un parámetro al constructor
instancia1 = holamundo('David')
instancia2 = holamundo('Pedro')

#llamamos al método saluda de cada instancia, muestra el atributo pasado en el constructor
instancia1.saluda()
instancia2.saluda()

#cambiamos el valor del atributo de la instancia
instancia1.cambia('Mercedes')

#llamamos a un método que muestra el nuevo atributo cambiado
#El cambio solo se produce en el atributo de la primera instancia
instancia1.saluda()
instancia2.saluda()


