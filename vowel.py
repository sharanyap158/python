n=input()
w="aeiouAEIOU"
c=0
for i in n:
    if i in w:
        c += 1
print(c)