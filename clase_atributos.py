class miclase:
    i = 1 #Atributos de clase... vendrían a ser como variables estáticas, aunque tienen alguna
          # diferencia, por como se sobreescribe a variable de instancia al cambiar el apuntador
    li = [1,2,3,4]

    def nada(self):
        pass #este comando no hace nada..

    def getVar(self):
        return miclase.i #Para acceder a los atributos de clase desde dentro de una instancia:
                        # miclase.[atributo]

    def getSelf(self):
        return self.i  #Para acceder a los atributos de clase tambien se puede utilizar
                      # self.[atributo], PERO si la modificamos self.i = 14, pasa a ser 
                      # una variable de instancia, self.i ya no contendrá lo mismo que 
                      # miclase.i en esa instancia

mic1 = miclase()
mic2 = miclase()

print("Valores de inicio: \ninstancia mic1.i: ", mic1.i)
print("instancia mic2.i: ", mic2.i)
print("instancia mic1.li: ", mic1.li)
print("instancia mic2.li: ", mic2.li,"\n")

miclase.i = 2 #Cambia el valor de i en todas las instancias


print("\nTras miclase.i = 2")
print("instancia mic1.i: ", mic1.i, "mic1.i con self: ", mic1.getSelf())
print("instancia mic2.i: ", mic2.i, "mic2.i con self: ", mic2.getSelf())
print("clase.i: ",miclase.i," mic1.getVar:",mic1.getVar()," mic2.getVar: ", mic2.getVar())


mic1.i = "A" #Cambio i en una instancia, por lo que pasa a ser una variable de instancia. 
            # como self.i = "A" dentro de la instancia.

print("\nTras mic1.i = A")
print("instancia mic1.i: ", mic1.i, "mic1.i con self: ", mic1.getSelf())
print("instancia mic2.i: ", mic2.i, "mic2.i con self: ", mic2.getSelf())
print("clase.i: ",miclase.i," mic1.getVar:",mic1.getVar()," mic2.getVar: ", mic2.getVar())

mic1.li.append(5) #modificamos la lista, pero sigue siendo la misma, no hemos cambiado la dirección
                # apuntada por li, por lo que li en las dos instancias siguen apuntando al atributo
                # de clase miclase.li.


print("tras mic1.li.append(5):")
print("instancia mic1.li: ", mic1.li)
print("instancia mic2.li: ", mic2.li,' !!!!')

