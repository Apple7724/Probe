x = float(input('ведите х '))
import math
if x > 0:
    y = (math.sin(x))**2
    print (y)
else:
    y = 1 - 2*math.sin(x**2)
    print (y)
