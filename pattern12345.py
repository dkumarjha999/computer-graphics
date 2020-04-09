import string
i=input("Enter the range of upper bound : ")
print("\n square of number which contains 1234 together\n")
for n in range(int(i)):
    x=n**2
    if (str.find(str(x),'1234')!=-1):
               print(n,x)
               
               
               
"""

deepak@deepak-Lenovo-ideapad-320-15IKB:~/mycglab$ python3 pattern12345.py
Enter the range of upper bound : 10000

 square of number which contains 1234 together

1111 1234321
3513 12341169
3514 12348196
9013 81234169

"""
