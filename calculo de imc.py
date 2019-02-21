while True:
	try:
		Altura = float(input("Digite sua altura em metros e centimetros:\n"))
		break
	except ValueError:
		print('Metros .(ponto) Centimetros')
while True:
	try:
		Peso = float(input("Digite seu peso em kg:\n"))
		break
	except ValueError:
		print('Quilos .(ponto) gramas')
imc = (Peso) / (Altura**2)


if(imc < 16):
	print('----------------------------')
	print("Magreza grave, seu imc é = ", imc)
elif(imc>=16 and imc<=17):
	print('----------------------------')
	print("Magreza moderada, seu imc é = ", imc)
elif(imc>17 and imc<=18.5):
	print('----------------------------')
	print("Magreza leve, seu imc é = ", imc)
elif(imc>18.5 and imc<=25):
	print('----------------------------')
	print("Saudavel, seu imc é = ", imc)
elif(imc>25 and imc<=30):
	print('----------------------------')
	print("Sobrepeso, seu imc é = ", imc)
elif(imc>30 and imc<=35):
	print('----------------------------')
	print("Obesidade grau I, seu imc é = ", imc)
elif(imc>35 and imc<=40):
	print('----------------------------')
	print("Obesidade grau II, seu imc é = ", imc)
elif(imc>40):
	print('----------------------------')
	print("Obesidade grau III, seu imc é = ", imc)
else:
	print('----------------------------')
	print("imc inexistente")

# Ou assim
#print("IMC MODERADO") if(imc>18.5 and imc<25) else print("IMC NAO MODERADO") #se for escrever a condição em uma linha, é obrigado a usar o else



### LOOPS ###
#for
#while
'''
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