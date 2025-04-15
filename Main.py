from Admin import Admin
from Student import Student
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        try:
            with open('passwords.txt', 'r') as auth:

                for line in auth:
                    if line.strip() == f"{username},{password}":
                        print("Login successful")
                        return username
        except FileNotFoundError:
            print("Password file not found.")

        print("Incorrect username or password.")


def get_info(username):
    try:
        with open('users.txt', 'r') as info:
            for line in info:
                data = line.strip().split(',')
                if data[0] == username:
                    return username, data[1], data[2], data[3], data[4]
    except FileNotFoundError:
        print("User file not found.")
    return None

def main():
    while True:
        username = login()

        user_info = get_info(username)

        if user_info:
            username, name, role, id, age = user_info

 
            if role == "admin":
    
                admin = Admin(username, name, id, role, age)
                admin.admin_menu()
            elif role == "student":
                student = Student(username, name, id, role, age)
                student.student_menu()
            else:
                print("Unknown role.")
        else:
            print("User not found in database.")
        again = input("Do you want to log in again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye!")
            break

main()
