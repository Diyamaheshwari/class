print("Multiple Table")
print("|",end='')
for j in range(1,11):
    print("",j,end='')
print()
print("________________________________________________________________")

for i in range(1,11):
    print(i,"|",end='')
    for j in range(1,11):
        print(format(i*j,"4d"),end='')
    print()
      
