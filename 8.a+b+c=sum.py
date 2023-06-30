def findsum(arr1,arr2,arr3,sum):
    s=set()

    for x in arr1:
        s.add(x)

    for i in range(len(arr2)):
        for j in range(len(arr3)):
            if (sum-arr1[i]-arr2[j]) in s:
                return True

    return False

a1 = [1, 2, 3, 4, 5] 
a2 = [2, 3, 6, 1, 2]
a3 = [3, 24, 5, 6]
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
sum = 9
print(findsum(a1,a2,a3,sum))