"""
Leap year ?
"""

#Method 1:
def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year%4==0 and (year%400!=0 or year%100!=0)):
        leap =True
    
    return leap

year = int(input())
print(is_leap(year))

#Method 2: Lambda
is_leap_year = lambda year: year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = 2024

if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

