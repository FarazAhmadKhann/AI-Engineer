x="""Hello, World my name is faraz ahmad
and i am in 4th semester"""
print(x)
print (x[2:9])
y="hello world"
print(y[-5:1:-1])
y="hello,world"
a=" faraz "
print(a.upper())
print(a.lower())
print(a.strip())   #remove wide space
a=a.strip()
b=a[0:2]
b=b.replace("a","A")  #replace
b=b+a[2:]

print(b)


print(y.split(","))


#f string

x="faraz is a good man and my age is"
d=8
c=f"{x} {d:.5f}"
print(c)


h="MY name is \"faraz\""
print(h)

print(isinstance(h,int))     #check the type true or not

