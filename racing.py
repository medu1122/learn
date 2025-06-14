def tinh_thoi_gian(quang_duong, van_toc):
    return quang_duong / van_toc

def kiem_tra_chiec_thang(N, X, Y, V, Z):
    # Tìm thời gian nhanh nhất của người chơi khác
    thoi_gian_nhanh_nhat = float('inf')
    for i in range(N-1):
        thoi_gian = tinh_thoi_gian(X, V[i])
        thoi_gian_nhanh_nhat = min(thoi_gian_nhanh_nhat, thoi_gian)
    
    # Tính thời gian của bạn
    if Z == 0:
        thoi_gian_cua_ban = tinh_thoi_gian(X, V[-1])
    else:
        quang_duong_con_lai = X - Z
        if quang_duong_con_lai <= 0:
            thoi_gian_cua_ban = 1
        else:
            thoi_gian_cua_ban = 1 + tinh_thoi_gian(quang_duong_con_lai, V[-1])
    
    # Bạn thắng nếu thời gian của bạn nhỏ hơn thời gian nhanh nhất của người khác
    return thoi_gian_cua_ban < thoi_gian_nhanh_nhat

def tim_Z_nho_nhat(N, X, Y, V):
    # Kiểm tra trường hợp không cần tăng tốc
    if kiem_tra_chiec_thang(N, X, Y, V, 0):
        return 0
    
    # Tìm Z nhỏ nhất bằng cách thử từng giá trị
    Z_nho_nhat = -1
    for Z in range(1, Y + 1):
        if kiem_tra_chiec_thang(N, X, Y, V, Z):
            Z_nho_nhat = Z
            break
    
    return Z_nho_nhat

def xu_ly():
    T = int(input())
    ket_qua = []  # Mảng lưu kết quả
    
    # Xử lý từng test case
    for _ in range(T):
        # Đọc input
        N, X, Y = map(int, input().split())
        V = list(map(int, input().split()))
        
        # Tìm kết quả và thêm vào mảng
        ket_qua.append(tim_Z_nho_nhat(N, X, Y, V))
    
    # In kết quả
    for kq in ket_qua:
        print(kq)

if __name__ == "__main__":
    xu_ly() 