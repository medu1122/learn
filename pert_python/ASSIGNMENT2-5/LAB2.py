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
def display_student(arr):
    for i in range(len(arr)):
        print(arr[i].name,arr[i].age,arr[i].gender,arr[i].score)
def delete_student(arr,index):
    arr.pop(index)
def count_student(arr):
    print("have ",len(arr)," student \n")
def search_student (name):
    for i in range(len(arr)):
        if arr[i].name==name:
            return i
    return -1
def update_student(arr,index,name,age,gender,score):
    arr[index].name=name
    arr[index].age=age
student=[]

