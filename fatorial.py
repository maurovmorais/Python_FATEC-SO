n = int(input("Digite o valor de n: "))

fat = 1
contador = 1

while contador <= n:
	fat = fat * contador
	contador = contador + 1
print(fat)