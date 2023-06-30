def smallestsubarray(arr,k):
    start=0
    end=0
    count=0
    hash={}

    for i in range(len(arr)):

        if arr[i] not in hash:
            count+=1
            end=i
            hash[arr[i]]=i
            if count==k:
                print('{} to {}'.format(start,end))
        elif arr[i] in hash:
            hash[arr[i]]=i
            count=1
            start=i

arr= [ 1, 2, 2, 3]
k = 2
smallestsubarray(arr,k)
