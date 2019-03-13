
Nome = ''
Idade = -9
'''
while(len(Nome) <= 3 ):
  Nome = (input('Coloque o Nome\n'))
  if(len(Nome) <= 3): 
    print('Vc nao pode ter nome com menos que 4 caracteres')

print('Obrigado, ' + Nome + ' vc conseguiu digitar um nome valido no nosso sistema\n\nAgora esta na hroa de digitar sua idade')

while(Idade < 0 or Idade > 150):
  Idade = int(input('Coloque sua Idade\n'))
  if(Idade < 0 or Idade > 150):
    print('Idade invalida')
  else:
    print('Idade colocada com sucesso')
'''
lista =  ['solteiro', 'casado', 'viuvo', 'divorciado']
estadoCivil = 'a'
while(estadoCivil.lower() not in lista):
  estadoCivil = (input('Qual seu estado civil?\nSolteiro\nCasado\nViuvo\nDivorciado:\n\n'))
  if(estadoCivil.lower() not in lista): 
    print('Seu estado civil deve ser\nSolteiro\nCasado\nViuvo\nDivorciado')




'''
0

contador = 0+1

1

contador = 1+1

2

'''