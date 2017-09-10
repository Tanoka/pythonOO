## Atributos de clase
Vienen a ser como las variables estáticas de clase. <br />
Los atributos de clase se declaran fuera de los métodos.  En el cuerpo de la clase.<br />
Para acceder desde un método a un atributo de clase se utiliza **<nombre clase>.<nombre atributo>**

    class miclase
        contador = 1
        
    def getContador(self)
        return miclase.contador
        
    def getSelfContador(self)
        return self.contador
        
Podemos cambiar el valor de clase de "contador" y el cambio se verá reflejado en todas sus instancias:

    objeto1 = miclase()
    objeto2 = miclase()
    **miclase.contador = 3**
    objeto1.getcontador() # retornará 3
    objeto2.getcontador() # retornará 3    
    
El método "getSelfContador", que accede con "self.", también ve reflejado el cambio:
    
    objeto1.getSelfContador() # retornará 3
    objeto2.getSelfContador() # retornará 3 
    
Pero si modificamos el valor de "self.contador" en una instancia, "self.contador" pasa a ser una variable de instancia y oculta la variable de clase, por lo que solo podremos acceder al valor de clase de "contador" con "miclase.contador":
    
    objeto1.contador = 5
    objeto1.getSelfContador() # retornará 5
    objeto2.getSelfContador() # retornará 3
    objeto1.getcontador() # retornará 3
    objeto2.getcontador() # retornará 3     
    
Si el atributo de clase en lugar de ser un tipo inmutable, como un tipo **int**, es un tipo mutable, como un tipo **list**, se podría modificar la variable de clase desde una instancia y que el cambio se propagara al resto de instancias.

    class miclase
        **lista = [1,2,3,4]**
        ....
        
    objeto1 = miclase()
    objeto2 = miclase()    
    
    **objeto1.lista.append(6)**
    
    print(objeto1.lista) # Muestra [1,2,3,4,6]
    print(objeto2.lista) # Muestra [1,2,3,4,6]
    
Esto es así porque en Python las variables son punteros a objectos, **lista.append** no cambia la dirección a la que apunta "lista", por lo que todas las instancias sigue viendo la misma lista, pero si hicieramos **lista = [1,2,3,4,6]**, estaríamos cambiando la dirección y pasaría lo mismo que ha pasado anteriormente al cambiar el valor del atributo "contador" en una instancia.
