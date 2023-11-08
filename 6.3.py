def maximum(a, b, c=0):
  if c == 0:
    return b if b >= a else a
  else:
    if a >=b and a >= c:
            return a
    if b >=a and b >= c:
            return b       
    if c >=b and c >= a:
            return c
print(maximum(-8,-9))
# тут если этот пример без условия c ==0, то тогда будет выведенно 0, но зачем он нам, если мы находим максимальное уже среди 2
