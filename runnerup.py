"""
Runnerup
"""

n = int(input())
arr = map(int, input().split())
ar=(list(set(list(arr))))
a=ar.sort(reverse=True)
print(ar[1])