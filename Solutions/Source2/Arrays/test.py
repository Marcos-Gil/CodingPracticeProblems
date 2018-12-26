def factorLarge(n):
    for i in range(1, n):
        if (n % i == 0):
            if (is_prime_number(i)):
                print(i)

def is_prime_number(x):
    if x >= 2:
        for y in range(2,x):
            if not ( x % y ):
                return False
    else:
	       return False
    return True

#factorLarge(200)


def troll(y, i):

    if (i == y):
        return y

    x = y % i
    i = i + 1
    if (x == 0):
        print(x)
    troll(y, i)

troll(19669134919989708132560396164453242756007298084645615426978507471866647213551536515184093380222629048043023397469449304154698783228191538742245168734371471, 1)
