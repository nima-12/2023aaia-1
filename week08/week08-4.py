a = 1234
ans = 0
while a>0:
  ans = ans * 10 + a%10
  print('现在的a是', a, '剥出来的皮a%10是', a%10,'现在的 ans 就变成', ans)
  a = a // 10