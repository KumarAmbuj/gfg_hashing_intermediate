def findpairs(arr,k):
    dict={}


    for x in arr:

        if k-(x%k) in dict:
            return True
        else:
            dict[x%k]=1

arr =[9, 7, 5, 3]
print(findpairs(arr,6))