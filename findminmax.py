def find_min_max(arr):
    if not arr:
        return []
    return (min(arr), max(arr))
arr=list(map(int, input().split()))
print(find_min_max(arr))