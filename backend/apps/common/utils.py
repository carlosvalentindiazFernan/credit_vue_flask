
def create_super_user():
    "This function create a super user for the app"

    print("Name")
    name = input()
    print("Email")
    email = input()
    print("Password")
    password = input()
    user = {
        'name': name,
        'email': email,
        'password': password
    }

    print(user)

    print("User created")