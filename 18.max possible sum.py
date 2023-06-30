def maxsum(arr1,arr2):
    hash=dict()
    maxsum=0

    sum=0

    for i in range(len(arr1)):
        if arr1[i] not in hash:
            sum=sum+arr2[i]
            maxsum=max(maxsum,sum)
            hash[arr1[i]]=i
        elif arr1[i] in hash:
            sum=sum-arr2[hash[arr1[i]]]
            sum=sum+arr2[i]
            maxsum=max(maxsum,sum)
            hash[arr1[i]]=i


    print(maxsum)

A = [0, 1, 2, 3, 0, 1, 4]
B = [9, 8, 1, 2, 3, 4, 5]
maxsum(A,B)