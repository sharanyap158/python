# printing the letters according to the before mentionrd number like 3a=aaa
'''str="3a4b6c"
res=""
for i in range(0,len(str),2):
    res+=int(str[i]) * str[i+1]
print(res)'''

# 31a4b111c
'''str="31a4b111c"
res=""
num=""
for i in str:
    if i.isdigit():
        num += i
    else:
        res += int(num) * i
        num=""
print(res)'''

# 31ab1c
str="31abc1h"
res=""
num=""
alp=""
i=0
while(i<len(str)):
    while str[i].isdigit():
        num += str[i]
        i+=1
    while i<len(str) and str[i].isalpha():
        alp+=str[i]
        i+=1
    res+=int(num)*alp 
    num=alp=""
print(res)