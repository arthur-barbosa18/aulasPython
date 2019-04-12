naturais = []
for i in range(1, 11):
  naturais.append(i)

print(naturais)

n = int(input("Digite n\n"))

result = []
for i in naturais:
  result.append(i*n)

# print(result)
# print('1 x', n,'=' )
# print


for i in range(0, len(result)):
  la = "{} X {} = {}".format( i+1 ,n, result[i])
  print(la)