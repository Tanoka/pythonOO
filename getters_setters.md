En python podemos hacer que los metódos de una clase se comporten como propiedades.<br />

Si tenemos una clase:
	
	class A:
		...
		def area(self):
			return self.x * self.y
Obtener el area:

	aObject.area()

Para poder acceder al método area como si de una propiedad se tratara:

	class B:
		@property
		def area(self):
                        return self.x * self.y

Obtener el area:

	bObject.area

En Python el acceso a propiedades se suele hacer de esta forma en lugar de utilizar getters y setters<br />
En el caso de querer un setter, o sea poder pasar un parámetro a un método como si fuera una propiedad:

	class B:
		...
		@area.setter
		def area(self, valor):
			self.__valor = valor

Ahora se podría hacer:

	bObjecto.area = "data"

**@property** es un **decorator**, o sea una función que toma otra función como parámetro y retorna una versión de la función parámetro. [link a explicacion de decorators]()<br />
Para poder implementar getter, setter o deleter, primero hay que poner el decorator **@property** a un método, una vez indicado un método con el decorator, podremos usar **@< metodo>.setter** y **@< metodo>.deleter**.
Los métodos getter y setter se llaman igual, los diferencia el decorator.<br />



