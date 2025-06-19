arr=[12, -14, 11, 91, -3, 10, 7, 15]
def trungbinhcong(arr):
    tong=0
    for i in range(len(arr)):
        tong+=arr[i]
    return tong/len(arr)
print(trungbinhcong(arr))