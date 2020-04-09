import string
i=input("Enter the range of upper bound : ")
print("\nsuper 4 number which contains 4 4s together\n")
for n in range(int(i)):
    x=4*n**4
    if (str.find(str(x),'4444')!=-1):
               print(n,x)
               
               
               
"""

Enter the range of upper bound : 1000

super 4 number which contains 4 4s together

deepak@deepak-Lenovo-ideapad-320-15IKB:~/mycglab$ python3 super4.py
Enter the range of upper bound : 10000

super 4 number which contains 4 4s together

1168 7444428488704
4972 2444468646298624
7423 12144449506652164
7752 14444916891992064
8431 20210466987444484


"""
