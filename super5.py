import string
i=input("Enter the range of upper bound : ")
print("\nsuper5 number which contains 5 5s together\n")
for n in range(int(i)):
    x=5*n**5
    if (str.find(str(x),'55555')!=-1):
               print(n,x)

"""

deepak@deepak-Lenovo-ideapad-320-15IKB:~/mycglab$ python3 super5.py
Enter the range of upper bound : 10000

super5 number which contains 5 5s together

4602 10320555555665840160
5517 25555531873653736785
7539 121769555550158808495
deepak@deepak-Lenovo-ideapad-320-15IKB:~/mycglab$ python3 super5.py
Enter the range of upper bound : 1000

super5 number which contains 5 5s together

deepak@deepak-Lenovo-ideapad-320-15IKB:~/mycglab$ 


"""
