def palindromic(arr):
    hash={}
    for x in arr:
        if x in hash:
            hash[x]+=1
        else:
            hash[x]=1
    count=0
    for x in hash:
        if hash[x]==1:
            count+=1
    return count-1
s='geeksforgeeks'
print(palindromic(s))
