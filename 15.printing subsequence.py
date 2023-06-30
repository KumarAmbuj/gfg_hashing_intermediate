def subsequence(arr):
    hash=dict()
    last=0
    len=0

    for x in arr:

        if x-1 in hash:
            hash[x]=hash[x-1]+1
            len=max(len,hash[x])
            last=x
        else:
            hash[x]=1

    for i in range(last-len+1,last+1):
        print(i,end=' ')
arr = [5, 7, 6, 7, 8]
subsequence(arr)



