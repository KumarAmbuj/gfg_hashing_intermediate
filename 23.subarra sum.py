def subarray(arr):
    s=set()
    sum=0
    for x in arr:
        sum+=x

        if sum==0:
            return True

        elif sum in s:

            return True

        else:
            s.add(sum)
    return False
arr=[4, 2, -3, 1, 6]
print(subarray(arr))

