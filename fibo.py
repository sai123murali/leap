ntg=int(input(""))
n1=1
n2=1
c=0
if(ntg==1):
    print(n1)
while(c<ntg):
    print(n1,end=' ')
    nt=n1+n2
    n1=n2
    n2=nt
    c+=1
