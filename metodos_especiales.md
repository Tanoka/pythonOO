Python tiene un montón de métodos especiales que pueden implementar nuestras clases. <br />

##### Métodos a implementar para usar los operadores de comparación:

* **\_\_eq\_\_(self, other)** implementa objeto == objeto 
* **\_\_ne\_\_(self, other)** implementa objeto != objeto
* **\_\_ge\_\_(self, other)** implementa objeto >= objeto
* **\_\_gt\_\_(self, other)** implementa objeto > objeto
* **\_\_lt\_\_(self, other)** implementa objeto < objeto
* **\_\_le\_\_(self, other)** implementa objeto <= objeto

Nada impide que comparemos objectos de cualquier tipo entre ello mientras implementen los métodos adecuados,
Por lo que se suele comprobar el tipo de instancia del objecto recibido antes de realizar la comparación, y
en caso de no ser el tipo esperado retornar **return NotImplemented** (solo para las comparación anteriores).<br />

	def \_\_eq\_\__(self, other):
		if not isinstance(other, Point): return NotImplemented
		return self.x == other.x and self.y == other.y

##### Métodos para implementar el comportamiento de algunas funciones.

**\_\_repr\_\_(self)**: implementa el comportamiento de la funcion **repr(object)**, está función nos retornará un versión string del objecto, versión que podrá ser evaludada con **eval()**.

**\_\_str\_\_(self)**: funcción **str(objet)**, retorna lo que se imprimiría si hacemos print(object)

##### Atributos especiales:

**\_\_module\_\_** contiene el nombre del módulo del objecto.

