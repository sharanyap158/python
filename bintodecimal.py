# printing binary to decimal
a=input()
dec=0
for i in range(len(a)):
    dec+=(2**i)
print(dec)

