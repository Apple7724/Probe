import math

def maximum (x,y,z,a,b,c):
    #return x + y + z
    return max (x,y,z,a,b,c)
x = int(input (' введи 6 любых чисел через enter '))
y = int(input ())
z = int(input ())
a = int(input ())
b = int(input ())
c = int(input ())
k = maximum (x,y,z,a,b,c)
print ('maximum =',k)
