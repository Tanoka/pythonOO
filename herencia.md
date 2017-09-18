## Herencia

Python tiene herencia múltiple. Forma de declararla:

    class A(padre1, padre2):

Además del polimorfismo proporcionado por la herencia, en Python cualquier clase pude tener un comportamiento polimórfico gracias al duck typing. <br />
No tiene interfaces. <br />
No hay sobrecarga de métodos. <br />
No hay clases abstractas. Se pueden implementar con librerías.<br />_

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
la clase A porque será el primero que encuentre, tanto si lo llamamos con **super().** como con **self.**. 
https://makina-corpus.com/blog/metier/2014/python-tutorial-understanding-python-mro-class-search-path
Para acceder el método en la clase B podríamos llamar a B.metodocomun(self), hay que pasar explicitamente **self.**
pues no estamos llamando a la misma instancia, sino al objecto clase. Parece que si le pasaramos el objecto a 
un método estático.

### Clase abstracta
Para implementar una clase abstracta hay que importar y heredar la libreria ABC del módulo abc.
También hay que importar el decorator @abstractmethod para implementar métodos abstractos.<br />

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






