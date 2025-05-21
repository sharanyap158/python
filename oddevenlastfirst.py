'''#odd no.s should come first 
n=list(map(int,input().split()))
odds= [x for x in n if x % 2 != 0]
evens= [x for x in n if x % 2 == 0]
res=odds + evens
print(res)
------------------------------
#even numbers come first
n=list(map(int,input().split()))
evens= [x for x in n if x % 2 == 0]
odds= [x for x in n if x % 2 != 0]
res= evens+odds
print(res) 
------------------------------
#even numbers come first
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    if l[i]%2==0:
        temp = l.pop(i)
        l.insert(k,temp)
        k += 1
print(l)
------------------------------
#odd numbers come first
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    if l[i]%2==0:
        temp = l.pop(i)
        l.insert(k,temp)
        k += 1
print(l) '''
 
