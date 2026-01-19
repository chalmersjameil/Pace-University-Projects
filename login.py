users = []  
class User:
    def __init__(self, username: str, name: str):
        self.username = username
        self.name = name
        self.password = None

    def set_password(self):
        self.password = hash(input(f"Set password for {self.name}: "))

    def login(self, username: str, password: str):
        return self.username == username and self.password == hash(password)

    def __str__(self):
        return self.name


def register():
    username = input("Enter username: ")
    name = input("Enter name: ")
    user = User(username, name)
    user.set_password()
    users.append(user)
    print(f"User {name} registered successfully!\n")


def signin():
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = next((u for u in users if u.username == username), None)
    if user:
        if user.login(username, password):
            print(f"Welcome, {user}!\n")
        else:
            print("Incorrect password.\n")
    else:
        print("User not found.\n")


def main():
    print("=== User Registration ===")
    for _ in range(2):
        register()  
    print("=== User Login ===")
    signin()  

if __name__ == '__main__':
    main()
