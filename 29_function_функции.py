import math

def func (x,y,z):
    #return x + y + z
    return (math.sqrt(x)+x)/2 + (math.sqrt(y)+y)/2 + (math.sqrt(z)+z)/2
x = int(input ())
y = int(input ())
z = int(input ())
k = func (x,y,z)
print (k)
