# file = open('numeros','r')

# # #i = 0
# # for linha in file:
# #   if('cachorro' in linha):
# #     print(linha, end='')
# #   #i = i+ 1

# #print(file.read())
# print('=======================')


# #print(file.readline(), file.readline(), file.readline())
# #print(file.readline())

# primeira_linha = file.readline()
# vetor = primeira_linha.split(',')
# print(vetor)

# for i in range(0, len(vetor)):
#   if(i == (len(vetor)-1)):
#     vetor[i] = vetor[i][0]
#   vetor[i] = int(vetor[i])

# print(vetor)
# com o w eu só escrevo e sempre sobescrevo o arquivo caso ele existe
fileEscrita = open('nao_existe', 'a')
fileEscrita.write('\n\nFIL É TOP\n\n')

#print(file.readline(), file.readline())

#if("cachorro" in '21 cahorro')


#Para descomentar só selecionar tudo que quer descomentar e apertar control+shift+/