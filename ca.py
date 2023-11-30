'''tup=tuple()
n=int(input("enter any no.:"))
for i in range(n):
    a=int(input("enter number:"))
    tup=tup+(a,)
print(tup)
print("maximum value:-",max(tup))
print("minimum value:-",min(tup))'''

'''write a program to check a list of tuples from given list having number and its square in
each tuple?
list1=[1,2,5,6]
res=[(val,val**2)for val in list1]
print(res)

list=list()
n=int(input("enter any no.:"))
for i in range(n):
    a=int(input("enter number:"))
    list=list+[a,]
print(list)
print("minimum value:-",min(list))

list1=[23,45,67,32]
list2=[12,13,14,15]
list=list1+list2
print(list)

numbers=[]
num=int(input("enter any no.:"))
for n in range(num):
    x=int(input('Enter number'))
    numbers.append(x)
print("Sum of numbers in the given list is:",sum(numbers))


def print_string_multiple_times():
    user_string = input("Enter a string: ")
    user_integer = int(input("Enter an integer: "))

    if user_integer < 0:
        print("Please enter a non-negative integer.")
        return

    for i in range(user_integer):
        print(user_string)

if _name_ == "_main_":
    print_string_multiple_times()

n=input("enter any string")

n1=int(input("enter integer"))
for i in range(n1):
    print(n)

inputString="Geeksforgeeks"
newString=inputString.upper()
print(newString)

que--  write a program to take string input from the user and count the no. of
    vowels present?

que--  write a program to accept input from user between 1 to 12 and print month name?    '''
