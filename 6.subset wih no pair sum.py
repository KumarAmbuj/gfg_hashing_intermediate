def nopairsum(arr,k):
    freq=[0 for i in range(k)]
    res=0

    sum=0

    for x in arr:
        sum=sum+x
        p=sum%k
        freq[p]+=1

    res=min(freq[0],1)

    for i in range(1,(k//2)+1):
        res+=max(freq[i],freq[k-i])

    print(res)

arr=[2, 4, 4, 3]
nopairsum(arr,4)
