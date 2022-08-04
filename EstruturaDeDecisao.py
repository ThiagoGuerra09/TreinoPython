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
  
6
numero1=input("Digite um numero:\n")
numero2=input("Digite um numero:\n")
numero3=input("Digite um numero:\n")
def maior(n,m):
    if(n>=m):
        return n
    else:
        return m
fim=maior(maior(numero1,numero2),numero3)
print(fim)

7
numero1=input("Digite um numero:\n")
numero2=input("Digite um numero:\n")
numero3=input("Digite um numero:\n")
def maior(n,m):
    if(n>=m):
        return n
    else:
        return m
def menor(n,m):
    if(n<=m):
        return n
    else:
        return m
Big=maior(maior(numero1,numero2),numero3)
Small=menor(menor(numero1,numero2),numero3)
print("O maior é:",Big)
print("O menor é:",Small)

8
def menor(n,m):
    if(n<=m):
        return n
    else:
        return m

numero1=input("Digite um preço:\n")
numero2=input("Digite um preço:\n")
numero3=input("Digite um preço:\n")


Small=menor(menor(numero1,numero2),numero3)
print("O menor é:",Small)

9
numero1=input("Digite um numero:\n")
numero2=input("Digite um numero:\n")
numero3=input("Digite um numero:\n")
def maior(n,m):
    if(n>=m):
        return n
    else:
        return m
def menor(n,m):
    if(n<=m):
        return n
    else:
        return m
    


Big=maior(maior(numero1,numero2),numero3)
Small=menor(menor(numero1,numero2),numero3)


if(numero1!=Big and numero1!=Small):
    medio=numero1
else:
    if(numero2!=Big and numero2!=Small):
        medio=numero2
    else: 
        medio=numero3

print("O maior é:",Big)
print("O medio é:",medio)
print("O menor é:",Small)

10
turno=input("Em qual turno você está? Digite M-matutino, V-Vespertino ou N- Noturno\n")
if(turno=="M"):
    print("Bom dia")
else:
    if(turno=="V"):
        print("Boa tarde")
    else:
        if(turno=="N"):
            print("Boa Noite")
        else:
            print("Valor inválido")
11
salario=input("Digite o seu salario atual:\n")
salario=float(salario)

if(salario<=280):
    newsalario=salario+salario*2/10
    percent="20%"
if(salario>280 and salario<=700):
    newsalario=salario+salario*15/100
    percent="15%"
if(salario>700 and salario<=1500):
    newsalario=salario+salario*1/10
    percent="10%"
if(salario>1500):
    newsalario=salario+salario*5/100
    percent="5%"
print("salario antigo\n", salario)
print("percentual de aumento\n", percent)
print("O valor do aumento é:\n", round(newsalario-salario,2))
print("O novo salario é:\n", round(newsalario,2))    

12
horas=input("Quantas horas você trabalhou esse mês?\n")
valor=input("Qual o valor da sua hora de serviço?\n")
bruto=int(horas)*int(valor)
if(bruto<=900):
    liquido=bruto-(bruto*21/100)
if(bruto>900 and bruto<=1500):
    liquido=bruto-(bruto*26/100)
if(bruto>1500 and bruto <=2500):
    liquido=bruto-(bruto*31/100)
if(bruto>2500):
    liquido=bruto-(bruto*41/100)

print("Total de descontos:\n", bruto-liquido)
print("Salario liquido:\n", liquido) 
