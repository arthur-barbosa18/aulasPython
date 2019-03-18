print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
while True:
	try:
		n = int(input("Quantos numeros da sequecia voce quer mostrar? "))
		break
	except ValueError:
		print('Digite um numero')
e1 = 0
e2 = 1
print('-_-'*15)
print({e1}, '->', {e2}, end='')
cont = 3
while cont <= n:
	e3 = e1 + e2
	print('->', {e3}, end='')
	e1 = e2
	e2 = e3
	cont += 1
print(' -> FIM')