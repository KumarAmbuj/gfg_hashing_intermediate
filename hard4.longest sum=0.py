def longestsum(arr):
    count=0
    hash={}
    sum=0
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=-1

    for i in range(len(arr)):
        sum=sum+arr[i]

        if sum==1:
            count=i+1
        elif sum-1 in hash and count<i-hash[sum-1]:
            count=i-hash[sum-1]

        elif sum not in hash:
            hash[sum]=i

    print(count)

arr=[0, 1, 1, 0, 0, 1]
longestsum(arr)
