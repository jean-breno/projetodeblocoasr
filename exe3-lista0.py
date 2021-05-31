def primo(numero):
    primo = True

    if(numero == 1):
        return False

    for i in range(2,numero):
        if(numero%i == 0):
            primo = False

    if (primo == True):
        return True
    else:
        return False
#Fim da Função

n = int(input("Número: "))

#Loop que printa os números primos excluindo N
for i in range(2,n):
    if(primo(i)):
         print(i)