# Bài 19: Viết chương trình Perl hoặc Python xóa 
# phần tử thứ k (k nhập từ bàn 
# phím) trong danh sách.

n=int(input("nhap so phan tu cua mang:"))
arr=[]
for i in range(n):
    arr.insert(i,int(input()))
print("mang ban dau:",arr)
k=int(input("nhap vi tri can xoa:"))
arr.pop(k)
print("mang sau khi xoa:",arr)