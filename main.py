import sqlite3

# Connect to database (or create it)
conn = sqlite3.connect('students.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    roll_no INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
''')
conn.commit()

def add_student():
    name = input("Enter student name: ")
    roll_no = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))
    cursor.execute("INSERT INTO students (roll_no, name, marks) VALUES (?, ?, ?)", (roll_no, name, marks))
    conn.commit()
    print("Student added.")

def view_students():
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        print(row)

def search_student():
    roll_no = int(input("Enter roll number to search: "))
    cursor.execute("SELECT * FROM students WHERE roll_no = ?", (roll_no,))
    student = cursor.fetchone()
    if student:
        print(student)
    else:
        print("Student not found.")

def delete_student():
    roll_no = int(input("Enter roll number to delete: "))
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    print("Deleted if record existed.")

def menu():
    while True:
        print("\n1. Add Student\n2. View All\n3. Search\n4. Delete\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

menu()
conn.close()
