def distributing(arr,k):
    hash=dict()

    for x in arr:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1

    for x, y in hash.items():
        if y>2*k:
            return False

    return True
arr = [2, 3, 3, 5, 3, 3]
k=2
print(distributing(arr,k))

