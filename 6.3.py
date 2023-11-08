def maximum(a, b, c=0):
    if  (a < 0 or b <0) and c == 0:
        return a if a > b else b
    else:
        if a >=b and a >= c:
            return a
        if b >=a and b >= c:
            return b       
        if c >=b and c >= a:
            return c
print(maximum(-3, -548989546,-1))
#исправил и доработал (если 2 отрицательных)
