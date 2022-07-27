1
print("alo mundo")

2
n1=input("digite um numero: \n")
print ("o numero foi informado")

3
n2=input("digite um numero: \n")
num1=int(n1)
num2=int(n2)
soma=num1+num2
print(soma)

4
linha=input("digite as 4 notas separadas por ,:\n")
n1=int(linha.split(",")[0])
n2=int(linha.split(",")[1])
n3=int(linha.split(",")[2])
n4=int(linha.split(",")[3])
media=(n1+n2+n3+n4)/4
print(media)

5
metros=input("digite em metros:\n")
cms=float(metros)
cms=cms*100
print(cms, "centimetros")

6
import math 
raio=input("Digite o raio da circunferência: \n")
area=(int(raio)**2)*math.pi
print(area)

7
medidas=input("Digite as dimensões do quadradro ou retângulo separadas por um x:\n")
lado1=int(medidas.split("x")[0])
lado2=int(medidas.split("x")[1])
area=lado1*lado2
print(area)

8
horas=input("Digite quantas horas que você trabalhou no mês:\n")
pagamento=input("Digite quanto você recebe por hora:\n")
print(int(horas)*float(pagamento))

9
temp=input("Digite a temperatura em Fahrenheit:\n")
celsius=((int(temp)-32)/9)*5
print(celsius)

10
temp=input("Digite a temperatura em Celsius:\n")
fire=(float(temp)*1.8)+32
print(fire)

11
n1=input("Digite o primeiro numero")
n2=input("Digite o segundo numero")
n3=input("Digite o terceiro numero")
a=(2*int(n1))+(int(n2)/2)
b=(3*int(n1))+(float(n3))
c=float(n3)**3

12
altura=input("Digite a altura:")
peso=(float(altura)*72.7)-58
print(peso)

13
altura=input("Digite a altura:")
pesoh=(float(altura)*72.7)-58
pesom=(float(altura)*62.1)-44.7
print("para homem o peso ideal é","{:.2f}".format(pesoh))
print("para mulher o peso ideal é","{:.2f}".format(pesom))

14
peso=input("Digite o peso dos peixes:\n")
excesso=int(peso)-50
if (excesso>0):
    multa=excesso
    print("o valor da multa é:", multa)
else:
    print("o valor da multa é 0")

15

horas=input("Digite quantas horas que você trabalhou no mês:\n")
pagamento=input("Digite quanto você recebe por hora:\n")
salariobruto=(int(horas)*float(pagamento))
ir=11/100*salariobruto
inss=8/100*salariobruto
sindicato=5/100*salariobruto
salario=salariobruto-ir-inss-sindicato
print("+salario bruto:",salariobruto)
print("-ir:",ir)
print("-inss:",inss)
print("-sindicato", sindicato)
print("=salario liquido", salario)

16
import math
metros=input("Digite o numero de metros:\n")
balde=54
metrosF=float(metros)
result=metrosF/balde
---- a função .ceil arredonda o float pra cima, a .floor arredonda pra baixo: elas são importadas da bib math----
---- se quiser arredondar igual notas são arredondadas, use a função nativa round()
print(math.ceil(result))

17
import math
metros=input("Digite o numero de metros:\n")
balde=108
galões=3.6
metrosF=float(metros)
print("o preço ao comprar baldes é:",math.ceil(metrosF/balde)*80)
print("o preço ao comprar em galões é:",math.ceil(metrosF/galões)*25)
latas=math.floor(metrosF/balde)
resto=metrosF/balde-latas
result=resto*balde
valor=(math.ceil(result/galões)*25)+(latas*80)
print("o melhor orçamento, misturando baldes e galões é:",valor)

18
tamanho=input("Digite o tamanho em MB do seu arquivo:\n")
velocidade=input("Digite a velociade da sua inrternet em mbps:\n")

segundos=int(tamanho)/int(velocidade)
minutos=segundos/60
minutos=(int(minutos))
seg1=segundos%60
print("o tempo estimado é {}.{}s".format(minutos,int(seg1)))
