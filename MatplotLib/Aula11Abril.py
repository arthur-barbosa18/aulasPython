# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
#import math
import pylab
import random
import numpy
from datetime import datetime
import pandas as pd

#print('Hello World')


# K k k k
# k k k C
# k k c k 


def desvio_padrao(vetor):
  numerador = 0
  for i in vetor:
    numerador = (numerador + (i - 0.375)**2)

  denominador = len(vetor)
  result = (numerador/denominador)**0.5
  return result

# em 6 eventos, vai ter 2 caras exatamente (ou duas coroas) 
# numero de eventos totais é 16 (2**4)
#6/16 = 3/8 = 0.375 = 37.5%

universo = ['cara', 'coroa']
eventos = []
amostras = []
eixo_x = []
vetor_de_probabilidades = []
for k in range(0, 5000):
  eixo_x.append(k)
  for j in range(0, 16):
    eventos = []
    for i in range(0, 4):
      evento = universo[(random.randint(0,1))]
      eventos.append(evento)
    amostras.append(eventos.count('cara'))

  #print(eventos)
  #print(eventos.count('cara'))

  vezes_que_caiu_cara_igual_a_2 = amostras.count(2)

  probabilidade = float(vezes_que_caiu_cara_igual_a_2)/float(len(amostras))
  vetor_de_probabilidades.append(probabilidade)
  #print('probabilidade = ', probabilidade)

#print(vetor_de_probabilidades)
print(sum(vetor_de_probabilidades)/len(vetor_de_probabilidades)*100)

#vetor_probabilidade_pandas = pd.DataFrame(vetor_de_probabilidades)
#desvio_padrao = vetor_probabilidade_pandas.std()
print('desvio padrao = ', desvio_padrao(vetor_de_probabilidades))

##plotagem do gráfico de amostras por porcentagem de eventos com 2 caras precisamente
plt.title('Amostras por Eventos com Duas Caras')
plt.xlabel('evento')
plt.ylabel('amostras')

# plt.plot(eixo_x, vetor_de_probabilidades,color='red', label='evento vs amostras')
# pylab.savefig('figure salva em: '+str(datetime.now())+'.png')
plt.arrow(x=eixo_x, y=vetor_de_probabilidades, dx=eixo_x, dy= eixo_x, label='probabilidades')

plt.show()


# eu to comparando o quao distante na media está cada media da 