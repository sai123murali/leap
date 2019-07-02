def num(a):
    count=0
    while(a!=0):
        a //=10
        count+=1
    return count

a=int(input(""))
num(a)