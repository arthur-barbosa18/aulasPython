def calculaIMC():
  while True:
    try:
      Altura = float(input("Digite sua altura em metros e centimetros:\n"))
      break
    except ValueError:
      print('Metros .(ponto) Centimetros')
  while True:
    try:
      Peso = float(input("Digite seu peso em kg:\n"))
      break
    except ValueError:
      print('Quilos .(ponto) gramas')
  imc = (Peso) / (Altura**2)


  if(imc < 16):
    print('----------------------------')
    print("Magreza grave, seu imc é = ", imc)
  elif(imc>=16 and imc<=17):
    print('----------------------------')
    print("Magreza moderada, seu imc é = ", imc)
  elif(imc>17 and imc<=18.5):
    print('----------------------------')
    print("Magreza leve, seu imc é = ", imc)
  elif(imc>18.5 and imc<=25):
    print('----------------------------')
    print("Saudavel, seu imc é = ", imc)
  elif(imc>25 and imc<=30):
    print('----------------------------')
    print("Sobrepeso, seu imc é = ", imc)
  elif(imc>30 and imc<=35):
    print('----------------------------')
    print("Obesidade grau I, seu imc é = ", imc)
  elif(imc>35 and imc<=40):
    print('----------------------------')
    print("Obesidade grau II, seu imc é = ", imc)
  elif(imc>40):
    print('----------------------------')
    print("Obesidade grau III, seu imc é = ", imc)
  else:
    print('----------------------------')
    print("imc inexistente")