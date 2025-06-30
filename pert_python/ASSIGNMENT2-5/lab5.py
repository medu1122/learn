def add_student(student_dict):
    student_id = input("Nhap ma sinh vien: ")
    if student_id in student_dict:
        print("Ma sinh vien da ton tai")
        return
    
    name = input("Nhap ten sinh vien: ")
    age = int(input("Nhap tuoi: "))
    major = input("Nhap nganh hoc: ")
    gpa = float(input("Nhap diem GPA: "))
    
    student_dict[student_id] = {
        "name": name,
        "age": age,
        "major": major,
        "gpa": gpa
    }
    print("Them sinh vien thanh cong")

def display_student(student_dict):
    student_id = input("Nhap ma sinh vien can xem: ")
    if student_id in student_dict:
        student = student_dict[student_id]
        print(f"Thong tin sinh vien {student_id}:")
        print(f"Ten: {student['name']}")
        print(f"Tuoi: {student['age']}")
        print(f"Nganh: {student['major']}")
        print(f"GPA: {student['gpa']}")
    else:
        print("Khong tim thay sinh vien")

def update_student(student_dict):
    student_id = input("Nhap ma sinh vien can cap nhat: ")
    if student_id not in student_dict:
        print("Khong tim thay sinh vien")
        return
    
    print("Nhap thong tin can cap nhat (de trong neu khong muon cap nhat):")
    name = input("Ten moi: ")
    age_str = input("Tuoi moi: ")
    major = input("Nganh hoc moi: ")
    gpa_str = input("Diem GPA moi: ")
    
    kwargs = {}
    if name:
        kwargs["name"] = name
    if age_str:
        kwargs["age"] = int(age_str)
    if major:
        kwargs["major"] = major
    if gpa_str:
        kwargs["gpa"] = float(gpa_str)
    
    student_dict[student_id].update(kwargs)
    print("Cap nhat thong tin sinh vien thanh cong")

def delete_student(student_dict):
    student_id = input("Nhap ma sinh vien can xoa: ")
    if student_id in student_dict:
        del student_dict[student_id]
        print("Xoa sinh vien thanh cong")
    else:
        print("Khong tim thay sinh vien")

def display_all_students(student_dict):
    if not student_dict:
        print("Danh sach sinh vien trong")
        return
    
    print("Danh sach sinh vien:")
    print("Ma SV | Ten | Tuoi | Nganh | GPA")
    print("-" * 60)
    for student_id, info in student_dict.items():
        print(student_id, info['name'], info['age'], info['major'], info['gpa'], sep=" | ")

def find_students_by_major(student_dict):
    major = input("Nhap nganh hoc can tim: ")
    found = False
    
    print(f"Danh sach sinh vien nganh {major}:")
    print("Ma SV | Ten | Tuoi | Nganh | GPA")
    print("-" * 60)
    
    for student_id, info in student_dict.items():
        if info["major"].lower() == major.lower():
            print(student_id, info['name'], info['age'], info['major'], info['gpa'], sep=" | ")
            found = True
    
    if not found:
        print(f"Khong tim thay sinh vien nganh {major}")

def find_top_and_bottom_students(student_dict):
    if not student_dict:
        print("Danh sach sinh vien trong")
        return
    
    max_student_id = max(student_dict, key=lambda x: student_dict[x]["gpa"])
    min_student_id = min(student_dict, key=lambda x: student_dict[x]["gpa"])
    
    print("Sinh vien co diem cao nhat:")
    print(f"Ma SV: {max_student_id}")
    print(f"Ten: {student_dict[max_student_id]['name']}")
    print(f"GPA: {student_dict[max_student_id]['gpa']}")
    
    print("\nSinh vien co diem thap nhat:")
    print(f"Ma SV: {min_student_id}")
    print(f"Ten: {student_dict[min_student_id]['name']}")
    print(f"GPA: {student_dict[min_student_id]['gpa']}")

def main():
    student_dict = {}
    
    while True:
        print("\n-----------MENU-----------")
        print("1. Them sinh vien moi")
        print("2. Hien thi thong tin sinh vien theo ma")
        print("3. Cap nhat thong tin sinh vien")
        print("4. Xoa sinh vien")
        print("5. Hien thi toan bo sinh vien")
        print("6. Tim sinh vien theo nganh")
        print("7. Tim sinh vien diem cao nhat va thap nhat")
        print("Q. Thoat")
        
        choice = input("Nhap lua chon: ")
        
        if choice == "1":
            add_student(student_dict)
        elif choice == "2":
            display_student(student_dict)
        elif choice == "3":
            update_student(student_dict)
        elif choice == "4":
            delete_student(student_dict)
        elif choice == "5":
            display_all_students(student_dict)
        elif choice == "6":
            find_students_by_major(student_dict)
        elif choice == "7":
            find_top_and_bottom_students(student_dict)
        elif choice.upper() == "Q":
            print("Thoat chuong trinh")
            break
        else:
            print("Nhap lai")

if __name__ == "__main__":
    main()
