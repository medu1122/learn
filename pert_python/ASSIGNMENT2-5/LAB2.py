class student:
    def __init__(self,name,age,gender,score):
        self.name=name
        self.age=age
        self.gender=gender
        self.score=score
def add_student(arr):
    name=input("nhapten:")
    age=int(input("nhap tuoi:"))
    gender=input("nhap gioi tinh:")
    score=int(input("nhap diem:"))
    arr.append(student(name,age,gender,score))
    print("add thanh cong")
def display_student(arr):
    print("danh sach sinh vien:\n")
    for i in range(len(arr)):
        print(arr[i].name,arr[i].age,arr[i].gender,arr[i].score,"\n")
def delete_student(arr):
    index=int(input("nhap vi tri can xoa:"))
    arr.pop(index)
    print("xoa thanh cong")
def count_student(arr):
    print("have ",len(arr)," student \n")
def search_student (arr):
    name=input("nhap ten can tim:")
    for i in range(len(arr)):
        if arr[i].name==name:
            return i
    return -1
def update_student(arr,index,name,age,gender,score):
    arr[index].name=name
    arr[index].age=age
    arr[index].gender=gender
    arr[index].score=score
    print("update thanh cong\n")
def sort_students_byname(arr):
    arr.sort(key=lambda x:x.name)
    print("sort thanh cong\n")
def reverse_students(arr):
    arr.reverse()
    print("reverse thanh cong\n")

def main():
    while(True):
        print("-----------MENU-----------")
        print("1.add student")
        print("2.update student")
        print("3.delete student")
        print("4.display student") 
        print("5.search student")
        print("6.count student")
        print("7.sort student by name")
        print("8.reverse student")
        print("9.exit")
        choice=int(input("nhap lua chon:"))
        if choice==1:
            add_student(students)
        elif choice==2:
            index = search_student(students)
            if index != -1:
                name=input("nhap ten moi:")
                age=int(input("nhap tuoi moi:"))
                gender=input("nhap gioi tinh moi:")
                score=int(input("nhap diem moi:"))
                update_student(students, index, name, age, gender, score)
            else:
                print("Khong tim thay sinh vien")
        elif choice==3:
            delete_student(students)
        elif choice==4:
            display_student(students)
        elif choice==5:
            index = search_student(students)
            if index != -1:
                print("Tim thay sinh vien:", students[index].name, students[index].age, students[index].gender, students[index].score)
            else:
                print("Khong tim thay sinh vien")
        elif choice==6:
            count_student(students)
        elif choice==7:
            sort_students_byname(students)
        elif choice==8:
            reverse_students(students)
        elif choice==9:
            print("Thoat chuong trinh")
            break
        else:
            print("nhap lai \n")
students = []
if __name__=="__main__":
    main()

