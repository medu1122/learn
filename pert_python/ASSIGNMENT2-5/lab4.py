import random

def create_question_bank():
    return set()

def add_question(arr):
    question = input("Nhap cau hoi: ")
    arr.add(question)
    print("Them cau hoi thanh cong")

def display_questions(arr):
    print("Danh sach cau hoi trong ngan hang:")
    for question in arr:
        print(question)

def delete_question(arr):
    question = input("Nhap cau hoi can xoa: ")
    arr.discard(question)
    print("Xoa cau hoi thanh cong")

def count_questions(arr):
    print("Co", len(arr), "cau hoi trong ngan hang")

def check_question(arr):
    question = input("Nhap cau hoi can kiem tra: ")
    if question in arr:
        print("Cau hoi da ton tai trong ngan hang")
        return True
    else:
        print("Cau hoi chua ton tai trong ngan hang")
        return False

def generate_exam(arr):
    if not arr:
        print("Ngan hang cau hoi trong, khong the tao de thi")
        return
    
    n = int(input("Nhap so luong cau hoi can tao de thi: "))
    if n > len(arr):
        print(f"So luong cau hoi vuot qua so cau hoi trong ngan hang ({len(arr)} cau)")
        return
    
    exam = random.sample(list(arr), n)
    print(f"\nDe thi gom {n} cau hoi:")
    for i, question in enumerate(exam, 1):
        print(f"Cau {i}: {question}")

def main():
    question_bank = create_question_bank()
    
    while(True):
        print("\n-----------MENU-----------")
        print("1. Tao ngan hang cau hoi moi")
        print("2. Them cau hoi moi")
        print("3. Xoa cau hoi")
        print("4. Kiem tra cau hoi ton tai")
        print("5. In toan bo cau hoi") 
        print("6. Dem so luong cau hoi")
        print("7. Tao de thi ngau nhien")
        print("Q. Thoat")
        
        choice = input("Nhap lua chon: ")
        
        if choice == "1":
            question_bank = create_question_bank()
            print("Da tao ngan hang cau hoi moi")
        elif choice == "2":
            add_question(question_bank)
        elif choice == "3":
            delete_question(question_bank)
        elif choice == "4":
            check_question(question_bank)
        elif choice == "5":
            display_questions(question_bank)
        elif choice == "6":
            count_questions(question_bank)
        elif choice == "7":
            generate_exam(question_bank)
        elif choice.upper() == "Q":
            print("Thoat chuong trinh")
            break
        else:
            print("Nhap lai")

if __name__ == "__main__":
    main()
