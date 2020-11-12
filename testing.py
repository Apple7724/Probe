#x, y, z = input().split()
#h, a, b = input().split()
#print('{:.0f}'.format(int(h)/(int(a)-int(b))))

"""u = int(input())
if u%2 == 0:
    t = u * 45 + 5 * (u / 2) + 15 * (u - u // 2 -1 )
else:
    t = u * 45 + 20 * (u //2 )
print('{:.0f} {:.0f}'.format(9+(t // 60), t % 60)) """
x, y, z = input().split()
print(max(int(x),int(y),int(z))-min(int(x),int(y),int(z)))
"""if int(x)>int(z) and int(x)>int(y):
    print('YES')
else:
    print('NO')"""

