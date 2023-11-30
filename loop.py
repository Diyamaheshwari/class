'''n=int(input("no. of terms: "))
n1,n2=0,1
count=0
print("Fabonacci Series" )
while(count<n):
    print(n1)
    nth=n1+n2
    n1=n2
    n2=nth
    count=count+1'''
num=int(input("enter ony no."))
sum=0
while(num!=0):
    digit=int(num%10)
    sum=sum+digit
    num=num/10
    print(sum)
    
