from librarymanagement import LibraryManagement
if __name__ == "__main__":
    obj = LibraryManagement()
    ch = 0

    while ch != 11:
        print('''
            1. Admin - Login
            2. User - Login
            3. Admin - Insert new book
            4. Admin - Display book details as Admin
            5. Admin - Search book
            6. Admin - Delete book
            7. User - Display books
            8. User - display all the books as User
            9. User - issue book
            10. user - return book
            11. user - Exit
        ''')
        ch = int(input("Enter choice: "))

        if ch == 1:
            obj.admin_login()
        elif ch == 2:
            obj.user_login()
        elif ch in [3, 4, 5, 6]:
            obj.admin_choices(ch)
        elif ch in [7, 8, 9, 10]:
            obj.user_choices(ch)
        elif ch == 11:
            print("Exiting the Library Management System.")
        else:
            print("Invalid choice. Please enter a valid option.")