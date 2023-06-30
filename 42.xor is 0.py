# xor having value 0 of same element
def findxor(arr):
    hash={}
    count=0

    for x in arr:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x in hash:
        if hash[x]==2:
            count+=1

    print(count)

A = [1, 3, 4, 1, 4]
findxor(A)