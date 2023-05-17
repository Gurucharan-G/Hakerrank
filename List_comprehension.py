"""
let x,y,z are 3 integers of cuboid print list of all co ordinates such that sum of x,y,z is not equal to integer n

x = 1
y = 1
z = 2
n = 3

expected output 
[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,2]]

"""
#Method 1
x = int(input())
y = int(input())
z = int(input())
n = int(input())

lis=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if(i+j+k!=n):
                li=[]
                li.append(i)
                li.append(j)
                li.append(k)
                lis.append(li)
print(lis)


#Method 2
x = int(input())
y = int(input())
z = int(input())
n = int(input())

lis = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

print(lis)