
def digite_novamente(msg):
    if(msg != ''):
      print(msg)
    nota = None
    while True:
        try:
            nota = int(input('De uma nota entre 0 e 10\n'))
            break
        except ValueError:
            print('Um numero, por favor')
    return nota


nota_invalida = True
nota = digite_novamente()

while(nota_invalida == True):
    if(nota < 0):
        nota = digite_novamente('Nota invalida, tente novamente, vc digitou algo menor que 0')
    elif(nota > 10):
        nota = digite_novamente('Nota invalida, tente novamente, vc digitou algo maior que 10')
    else:
        nota_invalida = False
        print('Valor valido')

