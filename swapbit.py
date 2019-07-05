x,y=map(int,input("").split())
x=x ^ y
y=x ^ y
x=y ^ x
print(x,y)