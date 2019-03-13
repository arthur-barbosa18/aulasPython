vetor = [1, 2, 3, 68, 34]
max = 0
print(max)

for i in range(0, len(vetor)):
	print(i)
	if(vetor[i] > max):
		max = vetor[i]

print(max)

'''
max = 0

vetor[0] #1
1 > 0 ? 
se sim, max = 1

vetor[1] #2

2 > 1? ...
se 2 > 1? max = 2

'''

#Como eu descobriria qual e o menor elemnto do vetor?