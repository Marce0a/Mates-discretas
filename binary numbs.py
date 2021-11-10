#base 2, if its another base, just change the 2
for pot in range(15):
    print(pot, 2**pot)
#get the number
int('1000000100000',2)
#
a=4830
b=129
bin(a)
bin(b)
c=5
b<<5
bin(b<<c)
n=a&(b<<c)
print(n)
#
x=1
y=1
z=1
print((x or z)and not(not y or not z))
x=True
y=True
z=True
print((x or z)and not(not y or not z))