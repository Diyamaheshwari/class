'''def add(num1,num2):
    num3=num1+num2
    return num3
a=int(input("a: "))
b=int(input("b: "))
ans=add(a,b)
print(f"results {ans}.")

def add(num1,num2):
    num3=num1+num2
    return num3

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
 
print(f"The addition of {num1} and {num2} results {add(num1,num2)}.")

def factorial(a):
    f=1
    for i in range(a,0,-1):
        f=f*i
    return f
a=int(input("a: "))
g=factorial(a)
print(g)'''

def myFun(**Kwargs):
    for Key,value in Kwargs.items():
        print("%s==%s"%(key,value))

myFun(first='Geeks',mid='for',last='Geeks')
            
        

        
        
  
