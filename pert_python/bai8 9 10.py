arr=[12, -14, 11, 91, -3, 10, 7, 15]

def tongChuoiDuongLonNhat(arr):
    max_sum = 0
    current_sum = 0
    
    for i in range(len(arr)):
        if arr[i] > 0:
            current_sum += arr[i]
        else:
            current_sum = 0
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
def dayDanDauDaiNhat(arr):
    if len(arr) < 2:
        return 0  
    max_length = 0
    current_length = 1   
    for i in range(1, len(arr)):
        if arr[i] * arr[i-1] < 0:
            current_length += 1
        else:
            current_length = 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length

def dayKhongTangDaiNhat(arr):
    if len(arr) == 0:
        return 0
        
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            current_length += 1
        else:
            current_length = 1
        if current_length > max_length:
            max_length = current_length
    
    return max_length

print("Tổng chuỗi dương lớn nhất:", tongChuoiDuongLonNhat(arr))
print("Số lượng phần tử liên tiếp đan dấu nhiều nhất:", dayDanDauDaiNhat(arr))
print("Số lượng phần tử không tăng nhiều nhất:", dayKhongTangDaiNhat(arr))