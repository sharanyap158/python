def isPowerOfTwo(n):
        return n > 0 and (n & (n - 1)) == 0
n=int(input())
print(isPowerOfTwo(n))