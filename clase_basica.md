## Clase básica

Creación de una clase

    class <nombre clase>:

Los métodos de una clase se definen como las funciones, con la diferencia de que el primer parámetro siempre es una referencia al propio objecto, viene a ser el 'this.' de Java, solo que en python se declara explícitamente en cada método.

    def <nombre método>(self, <parametros>):

Ejemplo completo:

    class holamundo:
        def diHola(self):
            print("Hola")

        def saluda(self, param):
            print("Hola ", param)

Instanciar una clase:

    objeto = holamundo()

Al llamar a un método de una instancia no hace falta pasarle el primer parámetro de la definicion, self, lo hace python implícitamente:

    objeto.diHola()

Llamar a un método de una instancia y pasarle un parámetro:

    objeto .saluda('Python')

