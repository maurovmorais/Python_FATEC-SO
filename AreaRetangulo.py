class retangulo:
	lado_a = None
	lado_b = None
	def __init__(self,lado_a,lado_b):
		self.lado_a = lado_a
		self.lado_b = lado_b
		print("Retangulo Criado")
	def area(self):
		return self.lado_a * self.lado_b
	def perimetro(self):
		return 2* self.lado_a + 2*self.lado_b

class quadrado(retangulo):
	def __init__(self, lado):
		retangulo.__init__(self,lado,lado)
		print("Quadrado criado")


r = retangulo(3,5)

print("Área: ",r.area())
print("Perimetro: ",r.perimetro())

q = quadrado(2)

print("Área: ",q.area())
print("Perimetro",q.perimetro())