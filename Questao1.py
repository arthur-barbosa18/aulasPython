nota_invalida = True
nota = int(input('De uma nota entre 0 e 10\n'))
while(nota_invalida == True):
	if(nota<0):
		print('Nota invalida, tente novamente')
		nota = int(input('De uma nota entre 0 e 10\n'))
	elif(nota>10):
		print('Nota invalida, tente novamente')
		nota = int(input('De uma nota entre 0 e 10\n'))
	else:
		nota_invalida = False
		print('Valor valido')