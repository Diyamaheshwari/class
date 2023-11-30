'''x=[a*7 for a in range(1,11) if(not a*7==42)]
print(x)

y=[a for a in range(1,26) if((a%2==0)and(a%3==0))]
print(y)

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello','welcome','to','GeeksforGeeks')

def sum(*argv):
    for arg in argv:
        print(arg)

sum(6+4+5+6+54+3+32+43+22++44+55+67+87++44+66+88++78)

sum=lambda a,b,c,d:a+b+c+d
a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))
d=int(input("d: "))
print("sum=",sum(a,b,c,d))

def increment(y):
    return(lambda x:x+1)(y)
a=100
print("a=",a)
print("a after incrementing=")
b=increment(a)
print(b)

def func(f,n):
    print(f(n))
twice=lambda x:x*2
thrice=lambda x:x*3
func(twice,4)
func(thrice,3)

program to find sum of first n natural no.
x=lambda:sum(range(1,11))
print(x())

list1=[1,2,3,4,5]
x=lambda:sum(list1)
print(x())'''

add=lambda x,y:x+y
multiply_and_add=lambda x,y,z:x*add(y,z)
print(multiply_and_add(3,4,5))


