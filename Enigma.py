# Decifra Enigma.
dec = 0
e = []
bin = 0

while True :
	bin = input("Digite o binário ou \"c\" para corrigir ou \"f\" finalizar: ")
	if bin == "f":
		print("Terminou !")
		break
	if bin == "c":
		e.pop(-1)
		print("Enigma: ",''.join(e))
		continue
	dec = int(bin,2)
	letra = chr(dec)
	e.append(letra)
	print("Enigma: ",''.join(e))
