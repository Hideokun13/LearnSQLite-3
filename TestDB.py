import sqlite3
DB_connect = sqlite3.connect('testLogin.db')

def main():
    print("=== Welcome to the project-db login system ===")
    print("press 1 to login")
    print("press 0 to register")
    print("your choice: ")
    if(input() == "1"):
        Login()
    else:
        Register()

def Login():
    print("== Login ==")
    print("username: ")
    input_Username = getInput()
    print("password: ")
    input_Password = getInput()
    LoginCheck(input_Username, input_Password)

def Register():
    print("== Register ==")
    print("New username: ")
    inputUsername = getInput()
    print("new password: ")
    inputPassword = getInput()
    try:
        executeCode = "INSERT INTO UserAccount (username, password) VALUES (" + "'" + inputUsername + "'" + "," + "'" + inputPassword + "'" + ");"
        DB_connect.execute(executeCode)
        DB_connect.commit()
        print("Register Successful!")
        input("Press enter to continue")
    except DB_connect.Error:
        print("Register Error! please try again")
        input("Press enter to continue")
    except DB_connect.IntegrityError:
        print("This Username has already registered! Please log in")
        input("Press enter to continue")
    main()
def LoginCheck (input_user, input_pass):
    isMatch = False
    cursor = DB_connect.execute("SELECT username, password FROM UserAccount;")
    for row in cursor:
        if(input_user == row[0] and input_pass == row[1]):
            print("=========================")
            print("Welcome! " + row[0])
            print("=========================")
            isMatch = True
    if(isMatch != True):
        print("Login Failed! : please try again")
        input("Press enter to continue")
        main()
def getInput():
    return input()
if __name__ == "__main__":
    main()
DB_connect.close()