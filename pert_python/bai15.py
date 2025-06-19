# Bài 15: Viết chương trình Perl hoặc Python 
# chuyển các phần tử dương của danh 
# sách lên đầu danh sách và in danh sách ra màn hình. 


    
def checkDuong (a):
    if a>=0:
        return True
    else:
        return False

def ChuyenPTDuong(arr):
    for i in range(len(arr)):
        save=0;
        if(checkDuong(arr[i])):
            save=arr[i]
            arr.remove(arr[i])
            arr.insert(0,save)
    return arr

a=[12, -14, 11, 91, -3, 10, 7, 15]

ChuyenPTDuong(a)
print(a)


            



