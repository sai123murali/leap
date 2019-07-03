m,n=map(int,input("").split())
for i in range(m,n):
    count=0
    s=i
    while(s!=0):
        s//=10
        count+=1
    s=i
    x=0
    while((s!=0)and(s<=100000)):
        r=s%10
        x+=pow(r,count)
        s//=10
    if(x==i):
        print(x)
  