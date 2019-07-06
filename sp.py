a=input("")
count=0
for i in a:
    if i.isdigit()==False and i.isalpha()==False:
        count+=1
print(count)