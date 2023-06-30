def printsubarray(arr):
    sum=0

    hash=dict()

    for i in range(len(arr)):
        sum=sum+arr[i]

        if sum==0:
            print('{} to {}'.format(0,i))
        elif sum in hash:
            print('{} to {}'.format(hash[sum]+1,i))
        elif sum not in hash:
            hash[sum]=i

arr = [6, 3, -1, -3, 4, -2, 2,
             4, 6, -12, -7]
printsubarray(arr)