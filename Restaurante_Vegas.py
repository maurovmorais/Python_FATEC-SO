def estacionamento(ano,mes,dia,hora,minuto):

	v = 0
	if ano > 0:
		v += ano*1500
	if mes > 0:
		 v += mes*500
	if dia > 0:
		v += dia*50
	if hora > 0:
		v += hora*10
	if minuto > 0:
		v += minuto*5
	print("\nValor Cobrado R$ ",v)
	
print("Entrada")
anoe=int(input("Digite o ano: "))
mese=int(input("Digite o mes: "))
diae=int(input("Digite o dia: "))
horae=int(input("Digite o hora: "))
mine=int(input("Digite o minuto: "))

print("Saída")
anos=int(input("Digite o ano: "))
mess=int(input("Digite o mes: "))
dias=int(input("Digite o dia: "))
horas=int(input("Digite o hora: "))
mins=int(input("Digite o minuto: "))

if (anoe < anos):
	ano = anos - anoe
else:
	ano = (anos - anoe)*-1

if (mese <= mess):
	mes = mess - mese
else:
	mes = 12-mese+mess

if (diae <= dias):
	dia = dias - diae
else:
	dia = 30-diae+dias

if (horae <= horas):
	hora = horas - horae
else:
	hora = 24-horae+horas
if (mine <= mins):
	minuto = mins - mine
else:
	minuto = 60-mine+mins

estacionamento(ano,mes,dia,hora,minuto)
print(ano,":ano(s)",mes,":mes(es)",dia,":dia(s)",hora,":hora(s)",minuto,":minuto(s)")
