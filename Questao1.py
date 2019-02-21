nota_invalida = True
while True:
	try:
		nota = int(input('De uma nota entre 0 e 10\n'))
		break
	except ValueError:
		print('Um numero carai')
while(nota_invalida == True):
	if(nota<0):
		print('Nota invalida, tente novamente')
		while True:
			try:
				nota = int(input('De uma nota entre 0 e 10\n'))
				break
			except ValueError:
				print('Um numero carai')
	elif(nota>10):
		print('Nota invalida, tente novamente')
		while True:
			try:
				nota = int(input('De uma nota entre 0 e 10\n'))
				break
			except ValueError:
				print('Um numero carai')
	else:
		nota_invalida = False
		print('Valor valido')