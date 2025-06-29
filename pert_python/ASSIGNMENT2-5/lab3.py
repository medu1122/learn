def add_book(arr):
    id = input("Nhap ID: ")
    title = input("Nhap ten sach: ")
    author = input("Nhap tac gia: ")
    year = int(input("Nhap nam xuat ban: "))
    arr.append((id, title, author, year))
    print("Them sach thanh cong")

def display_books(arr):
    print("Danh sach sach trong thu vien:")
    print(arr)

def delete_book(arr):
    id = input("Nhap ID sach can xoa: ")
    for i, book in enumerate(arr):
        if book[0] == id:
            arr.pop(i)
            print("Xoa sach thanh cong")
            return
    print("Khong tim thay sach co ID nay")

def count_books(arr):
    print(f"Co {len(arr)} cuon sach trong thu vien\n")

def search_book(arr):
    title = input("Nhap ten sach can tim: ")
    found = False
    print("Ket qua tim kiem:")
    for book in arr:
        if book[1].lower() == title.lower():
            print(f"{book[0]}\t{book[1]}\t\t{book[2]}\t\t{book[3]}")
            found = True
    if not found:
        print("Khong tim thay sach")
    return found

def update_book(arr):
    id = input("Nhap ID sach can cap nhat: ")
    for i, book in enumerate(arr):
        if book[0] == id:
            title = input("Nhap ten sach moi: ")
            author = input("Nhap tac gia moi: ")
            year = int(input("Nhap nam xuat ban moi: "))
            arr[i] = (id, title, author, year)
            print("Cap nhat thanh cong\n")
            return
    print("Khong tim thay sach co ID nay")

def statistics(arr):
    if not arr:
        print("Thu vien trong")
        return
        
    years = [book[3] for book in arr]
    newest = max(years)
    oldest = min(years)
    
    print(f"Nam xuat ban moi nhat: {newest}")
    print(f"Nam xuat ban cu nhat: {oldest}")

def main():
    while(True):
        print("-----------MENU-----------")
        print("1. Them sach moi")
        print("2. Cap nhat thong tin sach")
        print("3. Xoa sach")
        print("4. Hien thi thong tin sach") 
        print("5. Tim kiem sach")
        print("6. Thong ke")
        print("Q. Thoat")
        
        choice = input("Nhap lua chon: ")
        
        if choice == "1":
            add_book(books)
        elif choice == "2":
            update_book(books)
        elif choice == "3":
            delete_book(books)
        elif choice == "4":
            display_books(books)
        elif choice == "5":
            search_book(books)
        elif choice == "6":
            count_books(books)
            statistics(books)
        elif choice.upper() == "Q":
            print("Thoat chuong trinh")
            break
        else:
            print("Nhap lai\n")

books = []
if __name__ == "__main__":
    main()
