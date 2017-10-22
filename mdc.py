def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

a = int(input("Digite numero 1: "))
b = int(input("Digite numero 2: "))

print("MDC : %d" % mdc(a,b))
