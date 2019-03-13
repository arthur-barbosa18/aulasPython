def fat(n):
	if((n == 1) or (n == 0)):
		return 1;
	else:
		return n *fat(n-1)

#'Coloque o numero aqui'


#print(fat(2000))

res = 1
for i in range (0, 5 +1):
	if(i != 0):
		res = res*i;

print(res)



#TENTAR FAZER A QUESTAO DO FIBONACCI RECURSIVO, TALVEZ ATE SEQUENCIAL E a QUESTAO 42 e 47