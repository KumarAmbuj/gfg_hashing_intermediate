def countsubset(arr):
    count=0
    s=set()


    for x in arr:
        if x%2==0:
            s.add(x)

    count=len(s)
    print(2**count-1)

arr = [4, 2, 1, 9, 2, 6, 5, 3]
countsubset(arr)