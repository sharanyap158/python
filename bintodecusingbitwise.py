# print decimal to binary using bitwise operator
'''
a=8
rem=""
while a:
    rem += str(a&1)
    a=a>>1
print(rem[::-1])
'''
# print binary to decimal using bitwise operator
'''
a=input()
dec=0
for i in a:
    dec = (dec<<1) | int(i)
print(dec)
'''
