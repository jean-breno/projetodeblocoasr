def numeros_primos(qtd_rang):
    for i in range(qtd_rang):
        numero_qualquer = int(input("Digite um numero: "))
        if numero_qualquer == 0 and numero_qualquer == 1 and numero_qualquer % 2 == 1:
            print("O número não é primo! ")
        elif numero_qualquer == 2:
            print("O número é primo! ")
        #elif numero_qualquer % 2 == 1:
        #    print("O número não é primo! ")    
        else:
            print("O número é primo! ")    

qtd_rang = int(input("Quantas consultas você deseja fazer? "))
numeros_primos(qtd_rang)