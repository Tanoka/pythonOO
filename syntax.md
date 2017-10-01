Los bloques de código para clases, funciones o control de flujo se indican con indentación. No existen las llaves {} y el fin de linea de indica con salto de línea.

Python distingue entre mayúsculas y minúsculas.

Las variables no son declaradas y su tipo de deduce del objeto al que apuntan.

Todas las variables son referencias a objeto. En x = 2,  x contiene una referencia a un objeto de tipo entero y valor 2.

Como las variables son referencias no tienen tipo. Una variable puede cambiar de tipo de objeto referenciado y referenciar a objetos de todo tipo, incluido métodos o funciones.

Una variable que esté definida en un fichero fuera de una clase o una función es una variable global.

Una variable global es visible en todo el fichero, y en todos los ficheros que puedan importar ése fichero.

No existen constantes.

No funciona a++, pero sí funciona a += 1.

### Operadores
Matemáticos: +, -, *, / y %, **(exponente).
Comparación: ==, <=, =>, !=, <, >
Booleanos: and, or, not

### Tipos
Los tipos pueden ser mutables o inmutables, dependiendo de si una variable con un valor de ese tipo se puede modificar o no.
Como python es un lenguaje dinámicamente tipado los tipos pertenecen a los valores, no a las variables.

##### Tipos numéricos:
**int** immutable
**float** immutable
**complex** immutable 

##### Tipos secuenciales:
**list** mutable
**tuple** immutable 

##### Cadena de texto:
**str** immutable 

##### Cadenas binarias:
**bytearray** mutable 
**byte** immutable 

##### Tipos set:
**frozenset** immutable 
**set** mutable 

##### Tipo mapping:
**dict** mutable

##### Otros:
**none** El valor nulo

Los string, pueden delimitarse con comillas simples o dobles, el comportamiento el es mismo.
Los tipos booleanos son **True**, o **False**. Empezando por mayúscula.

Existe un módulo Decimal, que proporciona números decimales con la precisión que se desé.

### Sentencias (statements)
Todas las sentencias de bloque terminan en **:** para indicar el comienzo de la indentación.

##### Condicionales

    if True:
        haz()
    elif a == 2:
        hice()
    else:
        hare()
    
##### Bucles
**for, while**:

    for x in [1,2,3,4]:
        haz()

    while ..:
        haz()
    else:
La cláusula else se ejecutará siempre a menos que se salga del bucle con un break, un return si estamos en una función o una excepción.

**continue, break**: mismo comportamiento que en C o PHP.

### Funciones
Definición de una función:

    def nombreFuncion(param1, param2 = 10, *args):
        a = 2
        …..
        return a

##### Parámetros:
Se pueden definir valores por defecto para parámetros asignándoles un valor en la declaración (param2 = 10).

Se puede definir un número de parámetros variable con (*args). *args es accesible desde la función con bucles.

    for x in args:
        haz()

El asterisco cuando se encuentra aislado significa que a partir de ahí los parámetros no son posicionales sino que deben pasarse con nombre.

    def nombreFuncion(param, *, nom=’nombre’, es=False)

En el caso de haber dos ateriscos, ese parámetro contendrá todos las parejas key=value que hayamos puesto en la llamada a la función. callfuncion(1, uno=3, dos=True, cinco=”ho”)

    def nombreFuncion(param, **arg)

No se deben definir parámetros por defecto con tipos mutables, como **def func(lst = [])**, pues solo se crearán la primera vez que se llame a la función y después se reutilizará.
La forma correcta sería **def func(lst = None)** y programar que cada vez que llegue None se crea una lista [].

si el parámtroe param1 es una lista y usamos append() para añadir un valor, este ser verá reflejado en el entorno global, pero sí hacemos una asignación param1 = [1,2], estaremos dando una nueva dirección a la variable param1, por lo que ya no apuntará a la variable global, y será una variable local.

##### Funciones anónimas
Se pueden implementar funciones anónimas, pero no pueden tener más de una línea.

    var = lambda z: 3 * z + 2, 0.1

##### llamadas a funciones
En la llamada a una función podemos indicar el nombre del parámetro lo que permite cambiar el orden.

    nombreFuncion(param2 = 20, param1 = 50)
    
Llamar a una función con unpacking *.

    L = [1,2,3]
    funcion(*L) # Llamará a la función y le pasará 3 parámetros.
    
Las funciones son objetos, por lo que se pueden pasar como parámetros, asignar a variables y ser creadas dentro de otras funciones.

    funcionCaller(funcionparametro) #pasamos una función como parámetro
    var = nombreFuncion #asignamos una función a una variable
    var(5)

##### Variables locales
Si se quiere modificar una variable global en una función hay que declararla en la función como **global var**, sino al hacer var = 1 dentro de la función, se crearía una variable local y dejariamos de tener acceso a la variable global con el mismo nombre.

En caso de funciones anidadas para modificar una variable exterior usar **nolocal var**.

##### Closures
Se definen con una función dentro de otra función y la función interna se refiere a las variables locales de la función externa.

    def derivative(f, dx):
        def function(x):
                return (f(x + dx) - f(x)) / dx
        return function
    
    func1 = derivative(lambda z: 3 * z + 2, 0.1)
    func2 = derivative(lambda z: 3 * z**2 + 2, 0.1)
    res1 = func1(2)
    res2 = func2(3)
    
##### Decorators
Son syntax sugar para los closures.

    def p_decorate(func):
        def func_wrapper(name):
                   return "<p>{0}</p>".format(func(name))
           return func_wrapper
    
    def strong_decorate(func):
            def func_wrapper(name):
                    return "<strong>{0}</strong>".format(func(name))
            return func_wrapper
    
    @p_decorate
    @strong_decorate
    def get_text(name):
       return "lorem ipsum, {0} dolor sit amet".format(name)

Esta línea es la que ahorramos con los decorators, son llamados automáticamente los definidos con @

    get_text =p_decorate(strong_decorate(get_text))

Llamada

    get_text(‘Hola’)

decorators con parámetros...
    
### Generators
Es el mecanismo de lazy evaluation de python. Utiliza el comando **yield**.

Generador finito:

    def genNums():
        n = 0
        while n < 4:
                yield n #esta esta la instrucción  que retorna el valor del generator
                n += 1
    
    for num in genNums(): #El generador tiene un final, es este caso 4 iteraciones
        print(num)
    
Generador infinito:

    def fibGenerator():
        a, b = 0, 1
        while 1:    
                yield a
                a, b = b, a + b

    fib = fibGenerator() #hay que asignar el generador a una variable para operar.
    
    for i in range(5): #Es un generador infinito, le indicamos el número de iteraciones
        print ("fib generator ",i ," : ",next(fib))  
        
### Modulos
Un módulo en python es un fichero .py que puede contener cualquier código python.
También hay módulos en otros lenguajes, como C.
Python busca los módulos a importar en el path indicado en las lista sys,path del módulo sys.
Los módulos compilados en byte-code tienen la extensión .pyo. y los módulos byte-code no optimizados .pyc. Cada vez que se carga un módulo python busca estos ficheros del módulo y si no los encuentra los crea.
Durante el proceso de instalación de python se suelen compliar los módulos estandars as byte-code.

**import** importa librerías para su uso en el código.

    import <modulo1>, <modulo2>
       # Para acceder a las funciones importadas hay que poner modulo1.funcion()
    import <modulo1> as lib

    from <modulo1> import <function1>, <function2>
    from <modulo1> import *
        #Para acceder a las funciones importadas basta con function1()
El asterisco importa todas las funciones menos las comenzadas con **_**.  En caso de que exista la variable global **\_\_all\_\_** en el módulo, se importarán las funciones indicadas en esa variable.

Cada vez que se importa un módulo python crea una variable  **\_\_name\_\_**  en ese módulo con el nombre del módulo.
Si se ejecuta un programa la variable **\_\_name\_\_**  en el fichero que se ejecuta contendrá la cadena **\_\_main\_\_**. Examinando esta variable es fácil saber si el código se está ejecutando o ha sido cargado como un módulo.

### Package
Un package es una colección de módulos dentro de una jerarquía que contiene un fichero **\_\_init\_\_.py**.

    import <package.subpackage.modulo1>
    from <package.subpackage> import modulo1
### Excepciones
    try: 
        //do something
    except: 
        //do something
        pass  #si queremos que no pase nada
        raise #propaga la excepción
    else:
        //sino hay excepción ejecuta esto
    finally:
        //se ejecuta siempre

**raise** exceptions(args)
**raise** exceptions(args)  from original exception
**raise** #propaga la excepción activa y si no hay ninguna lanza TypeException

##### Definir excepciones

    class exceptionName(baseException): pass

### Testing
https://docs.python.org/3.5/tutorial/stdlib.html#quality-control





