def findsum(arr):

    hash=dict()

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):

            sum=arr[i]+arr[j]

            if sum in hash:
                prev=hash.get(sum)
                print(str(prev),'and ','({},{})'.format(arr[i],arr[j]))
                return True
            else:
                hash[sum]=(arr[i],arr[j])
    return False
arr = [3, 4, 7, 1, 2, 9, 8]
findsum(arr)

