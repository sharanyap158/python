# counting the number of bits using bitwise operator
'''
a=int(input())
count=0
while a:
    a=a>>1
    count+=1
print(count)
'''

# count set bits that is count no. of 1's
'''
a=int(input())
count=0
while a:
    if (a&1==1):
        count+=1
    a=a>>1
print(count)
'''

#count set bits that is count no. of 0's
'''
a=int(input())
count=0
while a:
    if (a&1!=1):
        count+=1
    a=a>>1
print(count)
'''
# another method
'''
a=int(input())
count=0
while a:
    if (a&1==0):
        count+=1
    a=a>>1
print(count)
'''

# print no. of moves until it gets one after and operator
'''
a=int(input())
count=0
while a&1==0:
    a=a>>1
    count+=1
print(count)
'''

# print no. of moves until it gets zero after and operator 
'''
a=int(input())
count=0
while a&1!=0:
    a=a>>1
    count+=1
print(count)
'''
# another method
'''
a=int(input())
count=0
while a&1==1:
    a=a>>1
    count+=1
print(count)
'''

#print no. of moves until it gets one by using left shift operator
'''
a = 8
count=0
temp = a
while a:
    a = a>>1
    count+=1
while temp&1==0:
    temp = temp>>1
    count-=1
print(count)
'''

# print binary number index value digit if it is 0 then print 1 
'''
def fun(a,i):
    mask =1<<i
    mask=~mask
    return a&mask
a=int(input())
i=int(input())
print(fun(a,i))
'''

# print binary number index value digit if it is 1 then print 0 
'''
def fun(a,i):
    mask=1<<i
    return a | mask
a=int(input())
i=int(input())
print(fun(a,i))
'''

# print binary number index value digit 
'''
def fun(a,i):
    mask=1<<i
    return int(mask&a>0)
a=int(input())
i=int(input())
print(fun(a,i))
'''

# power of 2
'''
def fun(a):
    return a&a-1==0
a=int(input())
print(fun(a))
'''

#print unique value in a list by using bitwise operator
'''
a=list(map(int, input().split(",")))
res=0
for i in a:
    res ^= i
print(res)
'''

# count the no. of digits in a number using recurrsion
'''
def count(n):
    if n == 0:
        return 0
    return 1 + count(n//10)
n=int(input()) 
print(count(n))
'''