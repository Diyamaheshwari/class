'''list1=[1,2,3,4,5]
def squares(x):
    return x**2
print(list(map(squares,list1)))


list2=[5,7,9,8,9]
def squares(x):
    return x**2
print(list(map(lambda x:x**2,list1)))

print([x**2 for x in list2])

def addition(n):
    return n+n
numbers=(1,2,3,4)
number1=(4,5,6)

result=map(addition,numbers)
print(list(result))

result1=map(lambda x:x+x,numbers)
print(list(result1))

result2=map(lambda x,y:x+y,numbers,number1)
print(list(result2))

number1=[1,2,3,4]
number2=[4,5,6,7]
number3=[2,3,4,9]
result=map(lambda x,y,z:x+y-z,number1,number2,number3)
print(list(result))

a=[1,2,3,5,7,9]
b=[2,3,6,7,9,8]
print(list(filter(lambda x:x not in a,b)))
print([x for x in a if x not in b])

def square(x):
    x=x*x
    return x
def double(x):
    x=x*2
    return x
num=int(input("num: "))
print("double,squaring the value: ",square(double(num)))'''

def recurfact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*recurfact(n-1)
num=int(input("num: "))
if num<0:
    print("factorial not exist for negative number")
else:
    print("factorial:",recurfact(num))
