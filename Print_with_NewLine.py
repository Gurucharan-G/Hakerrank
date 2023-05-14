"""Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
Example
a=3
b=5
Print the following:
8
-2
15

"""

#Read Input

a=int(input())
b=int(input())

def function(a,b):
    i=a+b
    j=a-b
    k=a*b
    return i,j,k


i,j,k=function(a,b)

#Method 1 -- Using multiple arguments and the newline character (\n) separator:
print(i, j, k, sep='\n')

#Method 2 -- Using a single print statement with newline characters (\n):
print(i, '\n', j, '\n', k)

#Method 3 -- Using f-string formatting:
print(f"{i}\n{j}\n{k}")

#Method 4 -- Using the newline character with the end parameter:
print(i, end='\n')
print(j, end='\n')
print(k, end='\n')

#Method 5 -- Using multiple print statements:
print(i)
print(j)
print(k)


