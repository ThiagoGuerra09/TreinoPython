1
numero1=input("Digite um numero:\n")
numero2=input("Digite um numero:\n")
result=int(numero1)-int(numero2) #positivo n1 é maior, negativo n2 é maior
if(result!=0):
    if(result>0):
        print(numero1)
    else:
        print(numero2)
else:
    print("São iguais")

2
numero1=input("Digite um numero:\n")
if(int(numero1)>=0):
    print("Número positivo")
else:
    print("Número negativo")

3
sexo=input("Digite seu sexo F ou M:\n")
if(sexo=="F"):
    print("Feminino")
else:
    if(sexo=="M"):
        print("Masculino")
    else:
        print("Sexo inválido")

4
def vogal(letra):
    if(letra=="a"or letra=="A" or letra=="b" or letra=="B"or letra=="c"or letra=="C"or letra=="d"or letra=="D"or letra=="e"or letra=="E"):
        print("vogal")
    else:
        print("consoante")
entrada=input("Digite uma letra\n")
vogal(entrada)

5
nota1=input("Digite a primeira nota:\n")
nota2=input("Digite a segunda nota:\n")
media=(int(nota1)+int(nota2))/2
if(media>=7):
    if(media==10):
        print("Aprovado com Distinção")
    else:
        print("Aprovado")
else:
    print("Reprovado")
