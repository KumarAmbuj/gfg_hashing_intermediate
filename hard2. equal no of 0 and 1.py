def subarray(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=-1

    hash=dict()
    count=0
    sum=0
    hash[sum]=1
    print(arr)

    for x in arr:
        sum=sum+x

        if sum==0:
            count+=hash[sum]
            hash[sum]+=1

        elif sum in hash:
            count+=hash[sum]
            hash[sum]+=1
        elif sum not in hash:
            hash[sum]=1

    print(count)

arr=[1, 0, 0, 1, 0, 1, 1]
subarray(arr)
