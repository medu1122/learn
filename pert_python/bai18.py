# Bài 18: Viết chương trình Perl hoặc Python chèn 
# danh sách [1,2,3] vào vị trí đầu, 
# cuối và thứ 5 của danh sách. 

listadd=[1,2,3]
n=int(input("nhap so phan tu cua mang:"))
arr=[]
for i in range(n):
    arr.insert(i,int(input()))
print("mang ban dau:",arr)
arr[0:0]=listadd
arr[5:5]=listadd
arr[len(arr):len(arr)]=listadd
print("mang sau khi add:",arr)
