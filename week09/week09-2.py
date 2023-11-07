a =[1,3,5,7,9,11,15,17]
for i in range(5):
  print('i是',i,'这时a[i的值是]',a[i])

print('比较好的写法，这个 range(N)')

N = len(a)
for i in range(N):
  print('i是', i, '这时a[i]的值是', a[i])