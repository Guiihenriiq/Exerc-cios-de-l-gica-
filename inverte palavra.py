continuar =1
palavra = str(input("Digite uma palavra: "))
print(" A palavra digitada foi " ,format(palavra))
string = palavra[::-1]
print("A palavra que você inseriu invertida fica: ",format(string))

continuar = int(input("digite 1 para continuar ou 2 para finalizar: "))

if continuar==1:
    
    palavra = str(input("Digite uma palavra: "))
    print(" A palavra digitada foi " ,format(palavra))
    string = palavra[::-1]
    print("A palavra que você inseriu invertida fica: ",format(string))
    continuar = int(input("digite 1 para continuar ou 2 para finalizar: "))

else:
    print("Até logo")





