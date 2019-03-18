
Nome = ''

while(len(Nome) <= 3 ):
  Nome = (input('Coloque o Nome\n'))
  if(len(Nome) <= 3): 
    print('Vc nao pode ter nome com menos que 4 caracteres')

print('Obrigado, ' + Nome + ' vc conseguiu digitar um nome valido no nosso sistema\n\nAgora esta na hora de digitar sua idade')

Idade = -9

while(Idade < 0 or Idade > 150):
  Idade = int(input('Coloque sua Idade\n'))
  if(Idade < 0 or Idade > 150):
    print('Idade invalida, coloque uma idade entre 0 e 150\n')
  else:
    print(Nome + ', sua idade foi adicionada com sucesso\n')

Salario = -1

while(Salario < 0):
  Salario = int(input('Coloque o salario que vc recebe\n'))
  if(Salario < 0):
    print('Salario tem que ser maior que 0')
  else:
    print(Nome + ', seu salario foi adicionado com sucesso')

lista_sexo = ['feminino', 'masculino', 'outros']
sexo = 'x'

while(sexo.lower() not in lista_sexo):
  sexo = (input('Qual seu genero?\nFeminino\nMasculino\nOutros:\n\n'))
  if(sexo.lower() not in lista_sexo):
    print('Digite um genero entre:\nFeminino\nMasculino\nOutros:\n\n')
  else:
    print(Nome + ', seu genero foi adicionado com sucesso\n')

lista_estadocivil =  ['solteiro', 'casado', 'viuvo', 'divorciado']
estadoCivil = 'a'

while(estadoCivil.lower() not in lista_estadocivil):
  estadoCivil = (input('Qual seu estado civil?\nSolteiro\nCasado\nViuvo\nDivorciado:\n\n'))
  if(estadoCivil.lower() not in lista_estadocivil): 
    print('Seu estado civil deve ser\nSolteiro\nCasado\nViuvo\nDivorciado')
  else:
    print(Nome + ', seu Estado Civil foi adicionado com sucesso\n')

print('Cadastro feito com sucesso\n')


'''
0

contador = 0+1

1

contador = 1+1

2

'''