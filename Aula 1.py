

Altura = float(input("Digite sua altura em metros e centimetros:\n"))
Peso = float(input("Digite seu peso em kg:\n"))
imc = (Peso) / (Altura**2)
print(imc)


if(imc < 16):
	print("Magreza grave, seu imc é = ", imc)
elif(imc>16 and imc<17):
	print("Magreza moderada, seu imc é = ", imc)
elif(imc>17 and imc<18.5):
	print("Magreza leve, seu imc é = ", imc)
elif(imc>18.5 and imc<25):
	print("Saudavel, seu imc e = ", imc)
elif(imc)

else:
	print("nao caiuu em nada")


print("IMC MODERADO") if(imc>18.5 and imc<25) else print("IMC NAO MODERADO") #se for escrever a condição em uma linha, é obrigado a usar o else



### LOOPS ###
#for
#while

Lista = ['a','b',2.4232,'acaa']
for i in Lista:
	if(i=='a' or i=='b'):
		print(i)

print("---------------------\n")
for i in range(0,len(Lista)):
	if(Lista[i]=='a' or Lista[i]=='b'):
		print(Lista[i])

print(Lista[2])
#vc pode iterar sob tupla
#vc pode fazer no dicionario (dict e sempre par chave:valor)
print("---------------------\n")

numeros = {'a': 1, 'b': 2, 'acaa': 3}
for i in numeros.values():
	print(i)

'''

< 16
	

Magreza grave
	Insuficiência cardíaca, anemia grave, enfraquecimento do sistema imunológico

16 a < 17
	

Magreza moderada
	Infertilidade, queda de cabelo, falta da menstruação

17 a < 18,5
	

Magreza leve
	Estresse, ansiedade, fadiga

18,5 < 25
	

Saudável
	

Menor risco para doenças

25 a < 30
	

Sobrepeso
	

Fadiga, varizes, má circulação

30 a < 35
	

Obesidade Grau I
	

Diabetes, infarto, angina, aterosclerose

35 a < 40
	

Obesidade Grau II (Severa)
	

Apneia do sono, falta de ar

> 40
	

Obesidade Grau III (Mórbida)
	

Refluxo, infarto, AVC, dificuldade de locomoção, escaras


'''