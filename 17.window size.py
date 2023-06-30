def windowsize(arr,k):
    list=[]
    for i in range(k):
        list.append(arr[i])
    print(len(set(list)))

    for i in range(k,len(arr)):
        list.pop(0)
        list.append(arr[i])
        print(len(set(list)))

arr = [1, 2, 4, 4]
k = 2
windowsize(arr,k)