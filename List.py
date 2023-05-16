"""
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

"""
Input:

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

output:
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

"""

N = int(input())
lst=[]
for i in range(0,N):
    instr=input()
    if "ins" in instr:
        a,b,c= instr.split(" ")
        lst.insert(int(b) ,int(c))
    elif "prin" in instr:
        print(lst)
    elif "rem" in instr:
        a,b = instr.split(" ")
        lst.remove(int(b))
    elif "app" in instr:
        a,b = instr.split(" ")
        lst.append(int(b))
    elif "pop" in instr:
        lst.pop()
    elif "sort" in instr:
        lst.sort()
    elif "reverse" in instr:
        lst.reverse()
    