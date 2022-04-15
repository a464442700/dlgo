from dlgo.gotypes import Player, Point
import random
print(Player.other)
# 0x 7fff ffff ffff ffff
# f=16=2^4
# 4*16
print(0xff)
print(2**63-1-0x7fffffffffffffff)
print( random.randint(0, 2))
table={}
table[1,1]=1
table[1,2]=2
print(table[1,2])
# Point.row=1
# Point.col=2
a=Point(3,4)
print(a[1])
print(8^7-6^9)
print("*****************")
table ={}
table[1,1]='a'
table[1,2]='b'
print(table.items())
for (pt,state),hash_code in table.items():
    print(pt,state,hash_code)

def getValue(x,y):
    print('x：',x)
    print('y：',y)
a=(1,2)
print(*a)

point=[]
point.append((1,2))
point.append((3,4))
print(point)
for i in range(3, 21, 6):
    print(i)
