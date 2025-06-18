# Bài 17: Viết chương trình Perl hoặc Python chèn một số 
# m (m nhập vào từ bàn 
# phím ) vào đầu danh sách, cuối danh sách và vị trí 
# thứ 5 của danh sách

k=int(input("nhap so can chen:"))
n=int(input("nhap so phan tu cua mang:"))
arr=[]
for i in range(n):
    arr.insert(i,int(input()))
print("mang ban dau:",arr)
arr.insert(0,k)
arr.append(k)
arr.insert(5,k)
print("mang sau khi add:",arr)
