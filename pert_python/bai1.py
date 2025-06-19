def tong(arr):
    tong =0
    for i in range(len(arr)):
        tong += arr[i]
    return tong
List=[12, -14, 11, 91, -3, 10, 7, 15]
print (tong(List))   