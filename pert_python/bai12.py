arr=[12, -14, 11, 91, -3, 10, 7, 15]
def doanconDuongmang(arr):
    n1=0
    result=0
    for i in range(len(arr)):
        n2=0
        if arr[i]>0:
            for j in range(i,len(arr)):
                n2+=1
                if arr[j]<0:
                    break
        if n2>n1 :
            n1=n2
            result=i
    return result
print("vi tri :",doanconDuongmang(arr))
    