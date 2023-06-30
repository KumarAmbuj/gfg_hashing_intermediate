def longestpair(arr,k):
    dict={}
    sum=0
    le=0

    for i in range(len(arr)):

        sum=sum+arr[i]
        p=sum%k

        if p==0:
            le=max(le,i+1)

        elif p in dict:
            le=max(le,i-dict[p])
        else:
            dict[p]=i

    return le

arr = [2, 7, 6, 1, 4, 5]
k = 3
print(longestpair(arr,k))