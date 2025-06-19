# Bài 18: Viết chương trình Perl hoặc Python chèn 
# danh sách [1,2,3] vào vị trí đầu, 
# cuối và thứ 5 của danh sách. 

listadd=[1,2,3]

arr=[[4, 12, -14, 11, 91, 4, -3, 10, 7, 15, 4]]

print("mang ban dau:",arr)
arr[0:0]=listadd
arr[5:5]=listadd
arr[len(arr):len(arr)]=listadd
print("mang sau khi add:",arr)
