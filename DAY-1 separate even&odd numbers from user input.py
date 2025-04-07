#separating even and odd numbers from a user input.
odd=[]
even=[]
a=tuple(map(int, input('enter numbers with comma separated:').split(",")))
for i in a:
    if i %2==0:
        even.append(i)
    else:
        odd.append(i)
print("odd numbers:")
print(*odd,sep=",")
print("even numbers:")
print(*even,sep=",")
#output
"""
enter numbers with comma separated:1,2,3,4,5,6,7,8,9,10
odd numbers:
1,3,5,7,9
even numbers:
2,4,6,8,10
"""




    
