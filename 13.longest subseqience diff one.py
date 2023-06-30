def subsequence(arr):
    hash=dict()
    len=0

    for x in arr:
        if x-1  in hash:
            hash[x]=hash[x-1]+1
            len=max(len,hash[x])

        elif x+1 in hash:
            hash[x]=hash[x+1]+1
            len=max(len,hash[x])
        else:
            hash[x]=1

    print(len)

arr = [1, 2, 3, 4, 5, 3, 2]
subsequence(arr)