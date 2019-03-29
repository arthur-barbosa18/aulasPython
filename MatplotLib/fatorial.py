import time
import matplotlib.pyplot as plt

def fatRecursivo(n):
  if((n == 1) or (n == 0)):
    return 1;
  else:
    return n *fatRecursivo(n-1)

def fatIterativo(n):
  res = 1
  for i in range (0, n+1):
    if(i != 0):
      res = res*i;
  return res

listaTemposRecursivo = []
listaTemposIterativo = []
eixoX = []

for i in range(1, 990):
  inicio = time.time()
  resultRecursivo = fatRecursivo(i)
  fim = time.time()
  tempoRecursivo = fim - inicio
  listaTemposRecursivo.append(tempoRecursivo)
  eixoX.append(i)

for i in range(1, 990):
  inicio = time.time()
  ResultIterativo = fatIterativo(i)
  fim = time.time()

  tempoIterativo = fim - inicio
  listaTemposIterativo.append(tempoIterativo)


for i in range(0,889):
  print(listaTemposIterativo[i], listaTemposRecursivo[i])
  print(listaTemposIterativo[i] > listaTemposRecursivo[i])



plt.plot(eixoX, listaTemposIterativo, 'r', label='fatIterativo')
plt.plot(eixoX, listaTemposRecursivo, 'b', label='Recursivo')
plt.title('Iterativo Vs Recursivo')
plt.show()