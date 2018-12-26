a = 19669134919989708132560396164453242756007298084645615426978507471866647213551536515184093380222629048043023397469449304154698783228191538742245168734371471
# b = 19669134919989708132560396164453242756007298084645615426978507471866647213551536515184093380222629048043023397469449304154698783228191538742245168734371471
# i = 1
# while b > 0:
# 	if a % i == 0:
# 		print i
# 	b = b - 1
# 	i = i + 1

def isqrt(n):
  x = n
  y = (x + n // x) // 2
  while y < x:
    x = y
    y = (x + n // x) // 2
  return x

def fermat(n, verbose=False):
    a = isqrt(n) # int(ceil(n**0.5))
    b2 = a*a - n
    b = isqrt(n) # int(b2**0.5)
    count = 0
    while b*b != b2:
        if verbose:
            print('Trying: a=%s b2=%s b=%s' % (a, b2, b))
        a = a + 1
        b2 = a*a - n
        b = isqrt(b2) # int(b2**0.5)
        count += 1
    p=a+b
    q=a-b
    assert n == p * q
    print('a=',a)
    print('b=',b)
    print('p=',p)
    print('q=',q)
    print('pq=',p*q)
    return p, q

fermat(a)