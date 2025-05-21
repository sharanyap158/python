n=list(map(int,input().split()))
for i in n:
    if i != 0:
        n.remove(0)
        n.append(0)
print(n)

    