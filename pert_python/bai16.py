# Bài 16: Viết chương trình Perl hoặc Python tìm số phần tử 
# là số nguyên tố của 
# danh sách và vị trí của nó trong danh sách. 

def checkNT (a):
    if a<=1:
        return 0
    else:
        check=0
        for i in range(2,int(a**0.5)+1):
            if a%i==0:
                check+=1
                break
        if check==0 :
            return 1
def kiemtrasoNTtrongmang(arr):
    for i in range(len(arr)):
        if checkNT(arr[i]):
            print("gia tri:",arr[i]," thuoc vi tri:",i," la so NT \n")
arr=[]   
a=int(input("nhap so phan tu cua mang:"))
for i in range(a):
    arr.insert(i,int(input()))
kiemtrasoNTtrongmang(arr)