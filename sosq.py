a=int(input(""))
count=0
while((a!=0)and(a<=1000000000000000000)):
    r=a%10
    count+=pow(r,2)
    a//=10
print(count)
