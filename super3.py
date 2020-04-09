import string
i=input("Enter the range of upper bound : ")
print("\nsuper 3 number which contains 3 3s together\n")
for n in range(int(i)):
    x=3*n**3
    if (str.find(str(x),'333')!=-1):
               print(n,x)


"""
deepak@deepak-Lenovo-ideapad-320-15IKB:~/mycglab$ python3 super3.py
Enter the range of upper bound : 1000

super 3 number which contains 3 3s together

261 53338743
462 295833384
471 313461333
481 333853923
558 521223336
753 1280873331



"""

# same question using while loop

n=0
i=input("Enter the range of upper bound : ")
print("\nsuper 3 number which contains 3 3s together\n")
while n<(int(i)):
    x=3*n**3
    if (str.find(str(x),'333')!=-1):
               print(n,x)
    n+=1
