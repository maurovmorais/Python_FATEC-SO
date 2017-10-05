import random
S=list(random.sample(range(1,25),15))
A=[]
L=[]
n=0
while n<15:
    l=int(input("Digite 15 números: "))
    if l>=1 and l<=25:
        if l not in L:
            L.append(l)
            n+=1
        else:
            print("Você já digitou esse número.")
            continue
    else:
        print("Digite um número entre 1 e 25")
for e in S:
    for x in L:
        if e == x:
            A.append(e)
print(75*"-")
print("Números sorteados: ",sorted(S))
print("Números jogados  : ",sorted(L))
print("Números acertados: ",sorted(A))
print("Você acertou %d números." % len(A))