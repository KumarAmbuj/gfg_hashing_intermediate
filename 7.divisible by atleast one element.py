def divisibility(arr):
    s=dict()
    mx=0

    for x in arr:
        s[x]=1
        mx=max(mx,x)

    res=dict()

    for i in range(len(arr)):
        if arr[i]!=0:

            for j in range(arr[i]*2,mx+1,arr[i]):

                if j in s:
                    res[j]=1

    for x in res:
        print(x)

arr = [ 2, 3, 8, 6, 9, 10]
n = len(arr)
divisibility(arr)


