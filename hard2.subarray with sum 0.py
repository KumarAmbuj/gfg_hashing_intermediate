def sumzero(arr):
    for i in range(len(arr)):
        if arr[i]==0:
            arr[i]=-1

    print(arr)

    hash={}
    count=0
    start=0
    end=0
    sum=0

    for i in range(len(arr)):

        sum=sum+arr[i]

        if sum==0 and count<(i+1):
            count=i+1
            start=0
            end=i

        elif sum in hash and (count<(i-hash[sum])):
            count=i-hash[sum]
            start=hash[sum]+1
            end=i


        elif sum not in hash:
            hash[sum]=i

    print('{} to {}'.format(start,end))
arr = [1, 0, 1, 1, 1, 0, 0]
sumzero(arr)

