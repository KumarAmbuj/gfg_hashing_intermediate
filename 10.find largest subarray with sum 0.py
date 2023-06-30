def findsubarray(arr):
    sum=0
    hash={}
    length=0

    for i in range(len(arr)):

        sum=sum+arr[i]

        if sum ==0:
            length=max(length,i+1)
        elif sum in hash:
            length=max(length,i-hash[sum])

        else:
            hash[sum]=i

    print(length)

arr=[15, -2, 2, -8, 1, 7, 10, 13]
findsubarray(arr)