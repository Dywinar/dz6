def maximum(a, b, c=0):
    if a <0 and b <0 and c == 0:
      return c
    else:
        if a >=b and a >= c:
            return a
        if b >=a and b >= c:
            return b       
        if c >=b and c >= a:
            return c
print(maximum(7,8,-99))
#исправил и доработал (если 2 отрицательных)
