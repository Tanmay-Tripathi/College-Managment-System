import mysql.connector as msql
from mysql.connector import Error


# ========================= B A C K E N D ==========================#

########################## SQL CONNECTION ##########################

try:
    db = msql.connect(host='localhost', username='ypur_username',
                      password='your_password', db='database_name')
    command_handler = db.cursor(buffered=True)

except Error as e:
    print("Error while connecting to MySQL", e)


# =========================College Managment Function ==========================#

# ========================= Main Menu in Command Line interface =========================#
def main():
    while 1:
        print("")
        print("# ========================= Welcome to the College System ========================= #")
        print("")
        print("1 > Login as a Student")
        print("2 > Login as a Teacher")
        print("3 > Login as a Admin")
        print("4 > End the Command Line Interface")
        print("")

        user_option = input(str("Option : "))

        if user_option == "1":
            auth_student()

        elif user_option == "2":
            auth_teacher()

        elif user_option == '3':
            auth_admin()
            
        elif user_option == '4':
            break;

        else:
            print("Invalid Option")
            
            

# ========================= Admin Part of the system ========================= #


def auth_admin():
    print("")
    print("# ========================= Admin Page ========================= #")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    print("")

    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password")

    else:
        print("Login details not recognized")


def admin_session():
    while 1:
        print("")
        print("# ========================= Admin Menu ========================= #")
        print("")

        print("1 > Register new Student")
        print("2 > Register new Teacher")
        print("3 > Delete exsisting student")
        print("4 > Delete exsisting Teacher")
        print("5 > Logout")
        print("")

        user_option = input(str("Option : "))
        print("")

        if user_option == '1':
            print("")
            print("Register new Student")
            username = input(str("Student Username : "))
            password = input(str("Student password : "))
            query_val = (username, password)
            command_handler.execute(
                "INSERT INTO user (username,password,account_type) VALUES (%s,%s,'student')", query_val)
            db.commit()
            print(username + " has been registered as a student")

        elif user_option == '2':
            print("")
            print("Register new Teacher")
            username = input(str("Teacher Username : "))
            password = input(str("Teacher password : "))
            query_val = (username, password)
            command_handler.execute(
                "INSERT INTO user (username,password,account_type) VALUES (%s,%s,'teacher')", query_val)
            db.commit()
            print(username + " has been registered as a teacher")

        elif user_option == '3':
            print("")
            print("Delete Exsisting Student account")
            username = input(str("Student Username : "))
            query_val = (username, "student")
            command_handler.execute(
                "DELETE FROM user WHERE username = %s AND account_type = %s", query_val)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == '4':
            print("")
            print("Delete Exsisting Teacher account")
            username = input(str("Teacher Username : "))
            query_val = (username, "teacher")
            command_handler.execute(
                "DELETE FROM user WHERE username = %s AND account_type = %s", query_val)
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print(username + " has been deleted")

        elif user_option == '5':
            break

        else:
            print("Not valid")


#========================= Teacher part of the System ========================= #


def auth_teacher():
    print("")
    print("# ========================= Teacher's Page ========================= #")
    print("")

    username = input(str("Username : "))
    password = input(str("Password : "))
    print("")

    query_val = (username, password)
    command_handler.execute(
        "SELECT * FROM user WHERE username = %s AND password = %s AND account_type = 'teacher'", query_val)
    if command_handler.rowcount <= 0:
        print("Login not recognized")
    else:
        teacher_session()


def teacher_session():

    while 1:
        print("")
        print("# ========================= Teacher's Menu ========================= #")
        print("")

        print("1 > Mark student register")
        print("2 > View Register")
        print("3 > Logout")
        print("")

        user_option = input(str("Option : "))

        if user_option == '1':
            print("")
            print("Mark student register")
            command_handler.execute(
                "SELECT username FROM user WHERE account_type = 'student'")
            record = command_handler.fetchall()
            date = input(str("DATE : DD/MM/YYYY : "))

            # to sort down the relevant data in touple
            for i in record:
                i = str(i).replace("'", "")
                i = str(i).replace(",", "")
                i = str(i).replace("(", "")
                i = str(i).replace(")", "")

                # Present/Absent/Late

                status = input(str("Status for "+str(i) + " P/A/L : "))
                query_val = (str(i), date, status)
                command_handler.execute(
                    "INSERT INTO attendance (username,date,status) VALUES(%s,%s,%s)", query_val)
                db.commit()
                print(i + " Marked as " + status)
                print("")

        elif user_option == '2':
            print("")
            print("Viewing all student register")
            print("")
            command_handler.execute(
                "SELECT username, date, status FROM attendance")
            records = command_handler.fetchall()

            for i in records:
                print(i)

        elif user_option == '3':
            break

        else:
            print("Not Valid")
            
            
#========================= Student part of the System =========================#


def auth_student():
    print("")
    print("# ========================= Student Page ========================= #")
    print("")

    username = input(str("Username : "))
    password = input(str("Password : "))

    query_val = (username, password)
    command_handler.execute(
        "SELECT * FROM user WHERE username = %s AND password = %s AND account_type = 'student'", query_val)

    if command_handler.rowcount <= 0:
        print("Invalid Login")
    else:
        student_session(username)


def student_session(username):

    while 1:
        print("")
        print("# ========================= Student's Menu ========================= #")
        print("")
        print("1 > View Register")
        print("2 > Download Register")
        print("3 > Logout")
        print("")

        user_option = input(str("Option : "))

        if user_option == "1":
            username = (str(username),)
            command_handler.execute(
                "SELECT date, username, status FROM attendance WHERE username = %s", username)
            records = command_handler.fetchall()

            for i in records:
                print(i)

        elif user_option == "2":
            print("")
            print("Downloading register data ⏳⌛️ ")
            username = (str(username),)
            command_handler.execute(
                "SELECT date, username, status FROM attendance WHERE username = %s", username)
            records = command_handler.fetchall()

            for i in records:
                with open("D:/WebScrapping/College_ManagmentSystem/register.txt", "w") as f:
                    f.write(str(records) + "\n")
                f.close()
            print("")
            print("All records saved")
            print("")

        elif user_option == "3":
            break

        else:
            print("Invlaid Option")


#========================= Main call for the execution ========================= #

main()
