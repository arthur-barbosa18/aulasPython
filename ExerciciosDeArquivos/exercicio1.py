# -*- coding: utf-8 -*-
# # Faça um programa que leia um arquivo texto contendo uma lista 
# de endereços IP e gere um outro arquivo, contendo um relatório dos 
# endereços IP válidos e inválidos.

# #     O arquivo de entrada possui o seguinte formato:

# Exemplo de arquivo de saída:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4

# [Endereços inválidos:]
# 257.32.4.5  
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256


enderecosValidos = ['200.135.80.9', '192.168.1.1', '8.35.67.74', '1.2.3.4']
enderecosInvalidos = ['257.32.4.5', '85.345.1.2', '9.8.234.5', '192.168.0.256']


#abrir arquivo:
fileEntrada = open('IPs.txt','r')
fileEnderecosValidos = open('enderecos_validos', 'a')
fileEnderecosInvalidos = open('enderecos_invalidos', 'a')


for linha in fileEntrada:
  if(linha[0:-1] in enderecosValidos):
    fileEnderecosValidos.write(linha)
  elif(linha[0:-1] in enderecosInvalidos):
    fileEnderecosInvalidos.write(linha)
  elif(linha not in '\n' and linha in enderecosValidos):
    fileEnderecosValidos.write(linha)
  elif(linha not in '\n' and linha in enderecosInvalidos):
    fileEnderecosInvalidos.write(linha)

fileEntrada.close()
fileEnderecosValidos.close()
fileEnderecosInvalidos.close()