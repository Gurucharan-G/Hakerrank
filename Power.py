"""Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n , print i^2.

ie if n=3 then [0,1,2] 
o/p :
0
1
4
"""

#Method 1: Using the exponentiation operator (**)
i = 5
square = i ** 2
print(square)

#Method 2: Using the multiplication operator (*)
i = 5
square = i * i
print(square)

#Method 3: Using the pow() function
i = 5
square = pow(i, 2)
print(square)

#Method 4:  Using a custom function
def square_number(i):
    return i * i

i = 5
square = square_number(i)
print(square)

#Method 5 : Using a lambda function
square_number = lambda i: i * i

i = 5
square = square_number(i)
print(square)

