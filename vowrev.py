def rev(str1):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    for i in str1:
        if i in vowels:
            str1=str1.replace(i,"")
    print(str1[::-1])
a=int(input(""))
str1=input("")
rev(str1)
