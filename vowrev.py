def rev(str):
    vowels=('a','e','i','o','u','A','E','I','O','U')
    for i in str:
        if i in vowels:
            str=str.replace(i,"")
    print(str[::-1])
str=input("")
rev(str)