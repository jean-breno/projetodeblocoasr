
n = int(input("Tabuada do número...: "))
inicio = int(input("De..: "))
fim = int(input("Até...:"))
for i in range(inicio, fim + 1):
    print(f"{n} x {i} = {n*i}")