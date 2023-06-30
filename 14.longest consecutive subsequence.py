def subsequence(arr):
    s=set()
    for x in arr:
        s.add(x)

    len=0

    for x in arr:
        if x-1 not in s:
            j=x
            while(j in s):
                j+=1

            len=max(len,j-x)
    print(len)

arr = [1, 9, 3, 10, 4, 20, 2]
subsequence(arr)



