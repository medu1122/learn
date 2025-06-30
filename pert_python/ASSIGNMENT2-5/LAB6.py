import numpy as np

def add_grade(word_arr, excel_arr, ppt_arr):
    word = float(input("Nhap diem Word: "))
    excel = float(input("Nhap diem Excel: "))
    ppt = float(input("Nhap diem PowerPoint: "))
    
    word_arr = np.append(word_arr, word)
    excel_arr = np.append(excel_arr, excel)
    ppt_arr = np.append(ppt_arr, ppt)
    print("Them diem thanh cong")
    
    return word_arr, excel_arr, ppt_arr

def update_grade(word_arr, excel_arr, ppt_arr):
    index = int(input(f"Nhap vi tri can cap nhat (0-{len(word_arr)-1}): "))
    word = float(input("Nhap diem Word moi: "))
    excel = float(input("Nhap diem Excel moi: "))
    ppt = float(input("Nhap diem PowerPoint moi: "))
    
    word_arr[index] = word
    excel_arr[index] = excel
    ppt_arr[index] = ppt
    print("Cap nhat diem thanh cong")
    
    return word_arr, excel_arr, ppt_arr

def delete_grade(word_arr, excel_arr, ppt_arr):
    index = int(input(f"Nhap vi tri can xoa (0-{len(word_arr)-1}): "))
    word_arr = np.delete(word_arr, index)
    excel_arr = np.delete(excel_arr, index)
    ppt_arr = np.delete(ppt_arr, index)
    print("Xoa diem thanh cong")
    
    return word_arr, excel_arr, ppt_arr

def display_grades(word_arr, excel_arr, ppt_arr):
    print("Danh sach diem:")
    print("STT | Word | Excel | PowerPoint | Trung binh")
    print("-" * 50)
    
    for i in range(len(word_arr)):
        avg = (word_arr[i] + excel_arr[i] + ppt_arr[i]) / 3
        print(f"{i} | {word_arr[i]} | {excel_arr[i]} | {ppt_arr[i]} | {avg:.2f}")

def calculate_average(word_arr, excel_arr, ppt_arr):
    word_avg = np.mean(word_arr)
    excel_avg = np.mean(excel_arr)
    ppt_avg = np.mean(ppt_arr)
    total_avg = (word_avg + excel_avg + ppt_avg) / 3
    
    print(f"Diem trung binh Word: {word_avg:.2f}")
    print(f"Diem trung binh Excel: {excel_avg:.2f}")
    print(f"Diem trung binh PowerPoint: {ppt_avg:.2f}")
    print(f"Diem trung binh tong: {total_avg:.2f}")

def find_min_max(word_arr, excel_arr, ppt_arr):
    print("Diem cao nhat:")
    print(f"Word: {np.max(word_arr)}")
    print(f"Excel: {np.max(excel_arr)}")
    print(f"PowerPoint: {np.max(ppt_arr)}")
    
    print("\nDiem thap nhat:")
    print(f"Word: {np.min(word_arr)}")
    print(f"Excel: {np.min(excel_arr)}")
    print(f"PowerPoint: {np.min(ppt_arr)}")

def sort_grades(word_arr, excel_arr, ppt_arr):
    # Tính điểm trung bình của mỗi sinh viên
    avg_arr = (word_arr + excel_arr + ppt_arr) / 3
    
    # Lấy chỉ số sau khi sắp xếp
    sorted_indices = np.argsort(avg_arr)
    
    # Sắp xếp các mảng theo chỉ số đã sắp xếp
    sorted_word = word_arr[sorted_indices]
    sorted_excel = excel_arr[sorted_indices]
    sorted_ppt = ppt_arr[sorted_indices]
    
    print("Da sap xep diem theo thu tu tang dan")
    
    return sorted_word, sorted_excel, sorted_ppt

def search_grade(word_arr, excel_arr, ppt_arr):
    search_value = float(input("Nhap diem can tim: "))
    
    # Tìm kiếm trong cả 3 mảng
    word_indices = np.where(word_arr == search_value)[0]
    excel_indices = np.where(excel_arr == search_value)[0]
    ppt_indices = np.where(ppt_arr == search_value)[0]
    
    if len(word_indices) > 0:
        print(f"Tim thay diem {search_value} trong Word tai vi tri:", word_indices)
    
    if len(excel_indices) > 0:
        print(f"Tim thay diem {search_value} trong Excel tai vi tri:", excel_indices)
    
    if len(ppt_indices) > 0:
        print(f"Tim thay diem {search_value} trong PowerPoint tai vi tri:", ppt_indices)
    
    if len(word_indices) == 0 and len(excel_indices) == 0 and len(ppt_indices) == 0:
        print(f"Khong tim thay diem {search_value}")

def main():
    # Khởi tạo mảng rỗng cho điểm Word, Excel, PowerPoint
    word_arr = np.array([], dtype=float)
    excel_arr = np.array([], dtype=float)
    ppt_arr = np.array([], dtype=float)
    
    while True:
        print("\n-----------MENU-----------")
        print("1. Them diem moi")
        print("2. Cap nhat diem")
        print("3. Xoa diem")
        print("4. Hien thi tat ca diem")
        print("5. Tinh diem trung binh")
        print("6. Tim diem cao nhat va thap nhat")
        print("7. Sap xep diem tang dan")
        print("8. Tim kiem diem")
        print("Q. Thoat")
        
        choice = input("Nhap lua chon: ")
        
        if choice == "1":
            word_arr, excel_arr, ppt_arr = add_grade(word_arr, excel_arr, ppt_arr)
        elif choice == "2":
            word_arr, excel_arr, ppt_arr = update_grade(word_arr, excel_arr, ppt_arr)
        elif choice == "3":
            word_arr, excel_arr, ppt_arr = delete_grade(word_arr, excel_arr, ppt_arr)
        elif choice == "4":
            display_grades(word_arr, excel_arr, ppt_arr)
        elif choice == "5":
            calculate_average(word_arr, excel_arr, ppt_arr)
        elif choice == "6":
            find_min_max(word_arr, excel_arr, ppt_arr)
        elif choice == "7":
            word_arr, excel_arr, ppt_arr = sort_grades(word_arr, excel_arr, ppt_arr)
        elif choice == "8":
            search_grade(word_arr, excel_arr, ppt_arr)
        elif choice.upper() == "Q":
            print("Thoat chuong trinh")
            break
        else:
            print("Nhap lai")

if __name__ == "__main__":
    main() 