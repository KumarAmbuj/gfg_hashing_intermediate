def subarraysum(arr,k):
    sum=0
    hash=dict()

    for i in range(len(arr)):
        sum=sum+arr[i]

        if sum==k:
            print('{} to {}'.format(0,i))

        elif sum-k in hash:
            print('{} to {}'.format(hash[sum-k]+1,i))
        else:
            hash[sum]=i

arr= [10, 2, -2, -20, 10]
sum = -10
subarraysum(arr,sum)