def subsequence(arr):
    hash=dict()
    len=0

    for x in arr:
        if x-1 in hash:
            hash[x]=hash[x-1]+1
            len=max(len,hash[x])
        else:
            hash[x]=1

    print(len)

a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
subsequence(a)

