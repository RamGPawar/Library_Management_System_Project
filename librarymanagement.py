from library import Book
import os
import datetime

class LibraryManagement:
    def __init__(self):
        self.logged_in_user = None

    def admin_login(self):
        username = input("Enter admin username: ")
        # Add your authentication logic here
        if username == "admin":
            self.logged_in_user = "admin"
            print("Admin login successful.")
        else:
            print("Invalid username. Exiting...")

    def user_login(self):
        username = input("Enter username: ")
        # Add your authentication logic here
        self.logged_in_user = username
        print(f"User login successful. Welcome {username}!")

    def admin_choices(self, ch):
        if ch == 1:
            self.admin_login()
        elif ch == 3:
            self.insert_book()
        elif ch == 4:
            self.display_books()
        elif ch == 5:
            id = int(input("Enter book ID to search: "))
            self.search_book(id)
        elif ch == 6:
            if self.logged_in_user == "admin":
                id = int(input("Enter book ID to delete: "))
                self.delete_book(id)
            else:
                print("You don't have permission to delete a book.")
        else:
            print("Invalid choice for admin. Please enter a valid option.")

    def user_choices(self, ch):
        if ch == 7:
            self.display_books()
        elif ch == 8:
            if self.logged_in_user == "user":
                self.display_all_books()
            else:
                print("You don't have permission to view all books.")
        elif ch == 9:
            if self.logged_in_user == "user":
                book_name = input("Enter book name to issue: ")
                self.issue_book_by_name(book_name)
            else:
                print("You don't have permission to issue a book.")
        elif ch == 10:
            if self.logged_in_user == "user":
                book_name = input("Enter book name to return: ")
                
                self.return_book_by_name(book_name)

            else:
                print("You don't have permission to return a book.")
        else:
            print("Invalid choice for user. Please enter a valid option.")

    def insert_book(self):
        if self.logged_in_user == "admin":
            # Admin functionality to insert a book
            id = int(input("Enter id of book: "))
            name = input("Enter name of book: ")
            price = int(input("Enter price of book: "))
            book = Book(id, name, price)
            with open("data.txt", "a") as fp:
                fp.write(str(book) + "\n")
            print("Book inserted successfully.")
        else:
            print("You don't have permission to insert a book.")

    def display_books(self):
        if self.logged_in_user == "admin" or self.logged_in_user == "user":
            with open("data.txt", "r") as fp:
                for e in fp:
                    sep_text = e.split(',')
                    print("id: ", sep_text[0])
                    print("Name: ", sep_text[1])
                    print("Price: ", sep_text[2])
                    print("Availability: ", sep_text[3])
                    print('----------')
        else:
            print("You don't have permission to display books.")

    def search_book(self, book_id):
        if self.logged_in_user == "admin" or self.logged_in_user == "user":
            with open('data.txt', 'r') as fp:
                for e in fp:
                    try:
                        e.index(str(book_id), 0, 4)
                        print("Book found")
                        break
                    except ValueError:
                        pass
                else:
                    print("Book not found")
        else:
            print("You don't have permission to search for a book.")

    def delete_book(self, book_id):
        if self.logged_in_user == "admin":
            container = []
            found = False
            with open("data.txt", "r") as fp:
                for e in fp:
                    sep_list = e.split(",")
                    if sep_list[0] == str(book_id):
                        found = True
                        
                    else:
                        container.append(e)

            if found:
                with open("data.txt", "w") as fp:
                    fp.writelines(container)
                print("Book deleted successfully.")
            else:
                print("Book not found.")
        else:
            print("You don't have permission to delete a book.")

    def display_all_books(self):
        if self.logged_in_user == "admin" or self.logged_in_user == "user":
            with open('data.txt', 'r') as fp:
                for e in fp:
                    sep_text = e.split(',')
                    print("id: ", sep_text[0])
                    print("Name: ", sep_text[1])
                    print("Price: ", sep_text[2])
                    print("Availability: ", sep_text[3])
                    print('----------')
        else:
            print("You don't have permission to display books.")


    def issue_book_by_name(self, book_name):
        if self.logged_in_user == "user":
            with open("data.txt", "r") as fp:
                lines = fp.readlines()

            found = False
            for i, line in enumerate(lines):
                try:
                    index = line.index(book_name)  # Find the index of the book name
                    found = True
                    sep_text = line.split(',')

                    # Check if sep_text has enough elements
                    if len(sep_text) >= 4 and sep_text[3].strip() == "1":
                        sep_text[3] = "0"  # Update availability to 0
                        lines[i] = ",".join(sep_text) + "\n"
                    else:
                        print("Book not available for issuing.")
                        return

                except ValueError:
                    pass

            if found:
                issue_date_str = input("Enter issue date (dd-mm-yyyy): ")
                issue_date_list = issue_date_str.split("-")

                d = int(issue_date_list[0])
                m = int(issue_date_list[1])
                y = int(issue_date_list[2])

                d1 = datetime.datetime(y, m, d).date()

                issue_file_path = "issue.txt"
                if not os.path.exists(issue_file_path):
                    open(issue_file_path, 'w').close()  # Create an empty file if it doesn't exist

                with open(issue_file_path, "r") as fp:
                    issue_lines = fp.readlines()

                new_issue_entry = f"{sep_text[0]},{sep_text[1]},{sep_text[2]},{d1.strftime('%d-%m-%Y')}\n"

                # Insert new entry after existing entries
                issue_lines.append(new_issue_entry)

                with open(issue_file_path, "w") as fp:
                    fp.writelines(issue_lines)

                with open("data.txt", "w") as fp:
                    fp.writelines(lines)

                print("Book issued successfully.")
            else:
                print("Book not found.")
        else:
            print("You don't have permission to issue a book.")


    def return_book_by_name(self, book_name):
        if self.logged_in_user == "user":
            with open("data.txt", "r") as fp:
                lines = fp.readlines()

            found = False
            for i, line in enumerate(lines):
                try:
                    index = line.index(book_name)  # Find the index of the book name
                    found = True
                    sep_text = line.split(',')

                    # Check if sep_text has enough elements
                    if len(sep_text) >= 4:
                        sep_text[3] = "1"  # Update availability to 1
                        lines[i] = ",".join(sep_text) + "\n"
                    else:
                        print("Invalid data format in 'data.txt'. Skipping this line.")

                except ValueError:
                    pass

            if found:
                # Update the return_date_str to match the format
                return_date_str = input("Enter return date (dd-mm-yyyy): ")

                try:
                    d2 = datetime.datetime.strptime(return_date_str, '%d-%m-%Y').date()  # Parse input date

                    with open("issue.txt", "r") as fp:
                        issue_lines = fp.readlines()

                    for j, issue_line in enumerate(issue_lines):
                        if str(sep_text[0]) in issue_line:
                            issue_date_str = issue_line.strip().split(",")[3].strip()
                            issue_date = datetime.datetime.strptime(issue_date_str, '%d-%m-%Y').date()

                            days_difference = (d2 - issue_date).days
                            print(f"Days difference: {days_difference}")

                            fine = max(0, days_difference * 10)  # Calculate fine based on days

                            if fine > 0:
                                print(f"Fine for late return: Rs.{fine}")

                            with open("issue.txt", "w") as fp:
                                issue_lines.pop(j)
                                fp.writelines(issue_lines)

                            with open("data.txt", "w") as fp:
                                fp.writelines(lines)

                            print("Book returned successfully.")
                            return

                    print("Issue record not found for the book.")
                except ValueError:
                    print("Invalid date format. Please enter the date in the correct format (dd-mm-yyyy).")
            else:
                print("Book not issued or not found.")
        else:
            print("You don't have permission to return a book.")
