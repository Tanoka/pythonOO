Python tiene un montón de métodos especiales que pueden implementar nuestras clases. <br />

##### Métodos a implementar para usar los operadores de comparación:

* **\_\_eq\_\_(self, other)** implementa objeto == objeto 
* **\_\_ne\_\_(self, other)** implementa objeto != objeto
* **\_\_ge\_\_(self, other)** implementa objeto >= objeto
* **\_\_gt\_\_(self, other)** implementa objeto > objeto
* **\_\_lt\_\_(self, other)** implementa objeto < objeto
* **\_\_le\_\_(self, other)** implementa objeto <= objeto

Nada impide que comparemos objectos de cualquier tipo entre ellos mientras implementen los métodos adecuados,
por lo que se suele comprobar el tipo de instancia del objecto recibido antes de realizar la comparación, y
en caso de no ser el tipo esperado retornar **return NotImplemented** (solo para las comparación anteriores).<br />

	def __eq___(self, other):
		if not isinstance(other, Point): return NotImplemented
		return self.x == other.x and self.y == other.y

##### Métodos fundamentales:

* **\_\_init\_\_(self)** constructor
* **\_\_new\_\_(self)** creación de objecto (no se suele usar)
* **\_\_bool\_\_(self)** Retorna true si hacemos if object:...
* **\_\_format\_\_(self)** implementa str.format()
* **\_\_hash\_\_(self)** si se proporciona objeto puede ser usar como dictionary key

##### Métodos para operaciones matemáticas:
* **\_\_add\_\_(self, other)**  x + y
* **\_\_sub\_\_(self, other)**  x - y
* **\_\_mul\_\_(self, other)**  x * y
* **\_\_mod\_\_(self, other)**  x % y
* **\_\_floordiv\_\_(self, other)**  x // y
* **\_\_truediv\_\_(self, other)**  x / y
* **\_\_divmod\_\_(self, other)** divmod(x, y) 
* **\_\_pow\_\_(self, other)**  x ** y

Para todos estos métodos existe la versión con "i" y con "r" delantes, **\_\_iadd\_\_(self, other)** x += y, **\_\_radd\_\_(self, other)** y + x, todas las versiones con "i" hacen la asignación tras la operación y todas las versiones con "r" cambian el orden de los parámetros.

* **\_\_abs\_\_(self)** abs(x)
* **\_\_int\_\_(self)** int(x)
* **\_\_float\_\_(self)** float(x)
* **\_\_round\_\_(selfi, digitos)** round(x, digitos)
* **\_\_index\_\_(self)** bin(x), oct(x), hex(x)
* **\_\_complex\_\_(self)** complex()
* **\_\_pos\_\_(self)** +x
* **\_\_neg\_\_(self)** -y

##### Métodos para operaciones de bits:

**\_\_and\_\_(self)** x & y, **\_\_or\_\_(self)** x | y, **\_\_xor\_\_(self)** x ^ y, **\_\_lshift\_\_(self)** x << y, **\_\_rshift\_\_(self)** x >> y, **\_\_invert\_\_(self)** ~x

**\_\_iand\_\_(self)** x &= y, **\_\_ior\_\_(self)** x |= y, **\_\_ixor\_\_(self)** x ^= y, **\_\_ilshift\_\_(self)** x <<= y,  **\_\_irshift\_\_(self)** x >>= y 

**\_\_rand\_\_(self)** y & x, **\_\_ror\_\_(self)** y | x,  **\_\_rxor\_\_(self)** y ^ x, **\_\_rlshift\_\_(self)** y << x, **\_\_rrlshift\_\_(self)** y >> x 

##### Métodos para implementar el comportamiento de algunas funciones.

**\_\_repr\_\_(self)**: implementa el comportamiento de la funcion **repr(object)**, está función nos retornará un versión string del objecto, versión que podrá ser evaludada con **eval()**.

**\_\_str\_\_(self)**: funcción **str(objet)**, retorna lo que se imprimiría si hacemos print(object)

##### Atributos especiales:

**\_\_module\_\_** contiene el nombre del módulo del objecto.

