def fat(n):
	if((n == 1) or (n == 0)):
		return 1;
	else:
		return n *fat(n-1)

def digite_novamente(msg):
    if(msg != ''):
      print(msg)
    numero_a_calcular = None
    while True:
        try:
            numero_a_calcular = int(input('Coloque o numero que voce quer ver o fatorial aqui:\n'))
            break
        except ValueError:
            print('Um numero, por favor')
    return numero_a_calcular

numero_invalido = True
numero_a_calcular = digite_novamente('Calculo de Fatorial')

while(numero_invalido == True):
	if(numero_a_calcular < 0):
		numero_a_calcular = digite_novamente('Um numero positivo, por favor')
	elif(numero_a_calcular > 997):
		numero_a_calcular = digite_novamente('Um numero abaixo de 997, por favor')
	else:
		numero_invalido = False
		print(fat(numero_a_calcular))

'''
res = 1
for i in range (0, 5 +1):
	if(i != 0):
		res = res*i;

print(res)
'''


#TENTAR FAZER A QUESTAO DO FIBONACCI RECURSIVO, TALVEZ ATE SEQUENCIAL E a QUESTAO 42 e 47