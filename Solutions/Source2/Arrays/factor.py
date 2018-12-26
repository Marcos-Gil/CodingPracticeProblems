def gcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b

number = 24278798670875549659981735976091279176024663505836043038483415110810062302568532734851979300333688164376781271484466733970328174247254114959470790444707384088000718622214769882473291009765712586444722537696334092164852221452017002677912097285224511532768357251409905732193580666355482072287853848103948014144341803820469928773613313328468819812395530971035074926251393059675847433139932224844932770996520984598135557600932706955232076643556346589232002918694744577113016094993550043792195417293939848222296313651785308602569052934944556663795257329273665298347924018002032188877909122207077778192986839363939867020801
x_fixed = 2
cycle_size = 2
x = 2
factor = 1

while factor == 1:
    count = 1
    while count <= cycle_size and factor <= 1:
        x = (x*x + 1) % number
        factor = gcd(x - x_fixed, number)
        count += 1
    cycle_size *= 2
    x_fixed = x

print(factor)
