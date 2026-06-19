1)
books = {}
students = {}
issued = {}

while True:
    print("\n===== SMART LIBRARY =====")
    print("1. Add Book")
    print("2. Register Student")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Display Books")
    print("7. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        book_id = input("Book ID: ")
        title = input("Book Title: ")
        author = input("Author: ")
        copies = int(input("Number of Copies: "))

        books[book_id] = [title, author, copies]
        print("Book Added Successfully!")

    elif choice == "2":
        sid = input("Student ID: ")
        name = input("Student Name: ")

        students[sid] = name
        print("Student Registered Successfully!")

    elif choice == "3":
        sid = input("Student ID: ")
        book_id = input("Book ID: ")

        if sid not in students:
            print("Student Not Found")
        elif book_id not in books:
            print("Book Not Found")
        elif books[book_id][2] == 0:
            print("Book Not Available")
        else:
            books[book_id][2] -= 1
            issued[sid] = book_id
            print("Book Issued Successfully!")

    elif choice == "4":
        sid = input("Student ID: ")

        if sid in issued:
            book_id = issued[sid]
            books[book_id][2] += 1
            del issued[sid]
            print("Book Returned Successfully!")
        else:
            print("No Book Issued")

    elif choice == "5":
        key = input("Enter Book Title: ").lower()

        found = False
        for book_id in books:
            if key in books[book_id][0].lower():
                print(book_id, books[book_id])
                found = True

        if not found:
            print("Book Not Found")

    elif choice == "6":
        print("\nBooks List")
        for book_id in books:
            print("Book ID:", book_id)
            print("Title:", books[book_id][0])
            print("Author:", books[book_id][1])
            print("Available Copies:", books[book_id][2])
            print()

    elif choice == "7":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

8)
courses = {}
students = {}
MAX_CREDITS = 20

while True:
    print("\n===== COURSE REGISTRATION SYSTEM =====")
    print("1. Add Course")
    print("2. Register Student")
    print("3. Enroll Course")
    print("4. Student Report")
    print("5. Course Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cid = input("Course ID: ")
        cname = input("Course Name: ")
        credits = int(input("Credits: "))
        seats = int(input("Seat Limit: "))

        courses[cid] = [cname, credits, seats]
        print("Course Added Successfully!")

    elif choice == "2":
        sid = input("Student ID: ")
        name = input("Student Name: ")

        students[sid] = [name, [], 0]
        print("Student Registered Successfully!")

    elif choice == "3":
        sid = input("Student ID: ")
        cid = input("Course ID: ")

        if sid not in students:
            print("Student Not Found")

        elif cid not in courses:
            print("Course Not Found")

        elif cid in students[sid][1]:
            print("Already Registered")

        elif courses[cid][2] == 0:
            print("No Seats Available")

        elif students[sid][2] + courses[cid][1] > MAX_CREDITS:
            print("Credit Limit Exceeded")

        else:
            students[sid][1].append(cid)
            students[sid][2] += courses[cid][1]
            courses[cid][2] -= 1
            print("Course Registered Successfully!")

    elif choice == "4":
        sid = input("Student ID: ")

        if sid in students:
            print("Name:", students[sid][0])
            print("Courses:", students[sid][1])
            print("Total Credits:", students[sid][2])
        else:
            print("Student Not Found")

    elif choice == "5":
        for cid in courses:
            print("\nCourse ID:", cid)
            print("Course Name:", courses[cid][0])
            print("Credits:", courses[cid][1])
            print("Available Seats:", courses[cid][2])

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
