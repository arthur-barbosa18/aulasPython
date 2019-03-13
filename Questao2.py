
usuario = None
senha = None
contador = 0
while(usuario == None or senha == None or usuario == senha):
  if(usuario == senha and usuario != None and senha != None):
    print('Burro')
  if(contador == 0):
      usuario = str(input('Coloque o nome de usuario\n'))
      senha = str(input('Coloque a senha\n'))
  else:
      usuario = str(input('Coloque o nome de usuario, DIFERENTE DA SENHA ANIMAL\n'))
      senha = str(input('Coloque a senha\n'))
  contador = contador + 1

print('Conectado com sucesso')
if(contador != 0):
  print('Mas vc errou ' + str(contador) + ' vezes')


'''
0

contador = 0+1

1

contador = 1+1

2

'''