## Constructores y atributos

El constructor de una clase se definen con **\_\_init\_\_()** <br />
Python tiene muchos métodos especiales del tipo **\_\_<nombre método>\_\_** <br />
Los atributos de instancia se definen mediante **self.<atributo>**, y se suele hacer en el constructor. <br />
La visibilidad de los atributos y métodos es pública.

    class holamundo:
        def __init__(self, nombre): 
            self.atributo = nombre
    
        def saluda(self):
            print("Hola ",self.atributo)
    
        def cambia(self, nombre):
            self.atributo = nombre

Instanciar una clase pasandole un parámetro al constructor:

    instancia = holamundo('Tierra')

Si llamamos al método saluda imprimirá el parámetro que hemos pasado al constructor:

    instancia.saluda()

Podemos cambiar el valor del atributo desde un método o directamente accediendo al atributo del objeto:

    instancia.cambia('Marte')
    instancia.atributo = 'Marte'


