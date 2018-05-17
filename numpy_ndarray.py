import numpy as np
a=[]
i=0
k=0
va=[]
va1=[]
#array=0
ka=0
while True:
    a.append(input("Enter values of the matrix: "))
    if a[i]=='q':
        a.remove('q')
        break;
    else:
        a[i]=int(a[i])
        i=i+1
x=len(a)
print(x//2+1)
for j in range(2,x//2+1):
    if(x%j==0):
        k=k+1
if(k<=0):
    a.append(input("Enter one more value: "))
    p=0

    #print("a length is"+str(x))

p=0
x=len(a)
for i in range (2,x):
    #print(x%i)
    if((x%i)==0):
        #print("inside x%i")
        va.append(int(i))
        va1.append(int(x/i))
        ka=len(va)
#print("ka is"+str(ka))
for i in range(0,ka):
    #print("inside inner for")
    print("Press "+str(i+1)+" for "+str(va[i])+"*"+str(va1[i])+" matrix")
choice=int(input("Enter choice:"))
#print("Choice is"+str(choice))
for i in range(1,ka+1):
    if i==choice:
        array=np.array(a).reshape(int(va[i-1]),int(va1[i-1]))
    else:
        array="Invalid Choice...."
        #print("Invalid Choice....")
        break;

print(array)







'''inp=input("Enter your choice: ")
if(inp=='1'):
    array=np.array(a).reshape(b,dim1)
    print(array)
elif(inp=='2'):
    array=np.array(a).reshape(dim1,b)
    print(array)'''
