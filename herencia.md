## Herencia

Hay Herencia múltiple

    class A(padre1, padre2):

Hay polimorfismo. 
No hay interfaces.
No hay sobrecarga de métodos.
No hay clases abstractas. Se pueden implementar con librerías.

Ejemplo de herencia múltiple:

    class A:
        def meta(self):
            return "from clase A"

        def metrepe(self):
            return "metodo repe A"

    class B:
        def metb(selft):
            return "from clase B"
        
    class C(A, B):
        def metc(self):
            return "from clase C"

        def metrepe(self):
            return "A sobreescrito en C"

Para llamar a un método de A o B desde C:

    class C(A, B):
        .....
        def metodo(self)
            return self.meta()
        
Si queremos invocar un método de la clase padre A o B desde C, pero lo hemos sobreescrito en C, podemos
utilizar __super()__, 
            
    class C(A, B):
        .....            
        def llamaMetrepeEnA(self):
            return super().metrepe()

Que pasa si un método está tanto en la clase A como la clase B, pues que siempre cogerá el de 
la clase A porque será el primero que encuentre. 
https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path
Se puede acceder al método de B, pero como siempre en python con hacks y formas extrañas....

### Clase abstracta
Para implementar una librería abstracta hay que importar y heredar la clase ABC del módulo abc.
También hay que importar el decorator @abstractmethod para implementar métodos abstractos.

Ejemplo de implementación y uso de una clase abstracta. Python 3.4+

    from abc import ABC, abstractmethod
    
    class abst(ABC):
        def hazalgo(self):
            print("método clase abstracta")
            
        @abstractmethod
        def metodoabs(self):
            pass
    
    class B(abst):
        def haciendo(self):
            print("método clase B")
    
        def metodoabs(self):
            print("método abstracto implementado")

### Teoría
Toda clase hereda en última instancia y de forma implícita de la clase genérica 'object'.
Las clase 'object' tiene los métodos: \_\_new\_\_(), \_\_init\_\_()_, \_\_eq\_\_(), etc..
Al instanciar una clase primero se crea un objeto vacio con el método \_\_new\_\_() de la 
clase 'object' de la que hereda la clase a instanciar, después se llama a \_\_init\_\_()
para inicializar el nuevo objecto recien creado. De estos dos métodos \_\_init\_\_() es el
único que se suele sobreescribir.





