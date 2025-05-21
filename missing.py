n=list(map(int,input().split()))
for i in range(1,len(n)+2):
    if i not in n:
        n.append(i)
        n.sort()
print(n)