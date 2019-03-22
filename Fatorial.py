result = 1
for i in range(4,0, -1):
  print(i)
  result = result*i

print(result)

def fat(n):
  if((n==1) or (n==0)):
    return 1
  else:
    return fat(n-1)*n

print(fat(998))
#fazer o 42, 43, 7