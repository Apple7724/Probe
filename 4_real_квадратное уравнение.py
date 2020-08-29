a = float(input ("введите коэффициент а "))
b = float(input ("введите коэффициент b "))
c = float(input ("введите коэффициент c "))
import math
print ("введенное уравнение: ", a,"*x^2 + ", b,"*x + ", c, " = 0")
d = float( b**2-4*a*c)
if d < 0:
    print ("дискриминант D = ", d)
    print("корней нет")
elif d==0:
    print ("дискриминант D = ", d)
    x1 = float((-b + math.sqrt(d))/(2*a))
    print ("1 корень = ", x1)
else:
    print ("дискриминант D = ", d)
    x1 = float((-b + math.sqrt(d))/(2*a))
    x2 = float((-b - math.sqrt(d))/(2*a))
    print ("1 корень = ", x1)
    print ("2 корень = ", x2)
