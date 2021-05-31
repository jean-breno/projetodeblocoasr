def pares_impares(qtd_rang):
    qtdd_pares = 0
    qtdd_impares = 0
    for i in range(qtd_rang):
        n1 =  int(input(f"n{i+1}: "))
        if n1 % 2 == 0 :
            qtdd_pares +=1
        else : 
            qtdd_impares +=1
    print(f"{qtdd_pares} pares e {qtdd_impares} impares")

qtd_rang = int(input("Quantos números você quer introduzir? "))
pares_impares(qtd_rang)