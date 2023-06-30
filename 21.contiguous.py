def contiguous(arr):
    mn=arr[0]
    s=set()
    for x in arr:
        s.add(x)
        mn=min(mn,x)

    for i in range(mn,mn+len(s)):
        if i not in s:
            return False
    return True
arr = [10, 14, 10, 12, 12, 13, 15]
print(contiguous(arr))
