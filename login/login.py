import hashlib
profiles_db = []

class Database:
    def __init__(self):
        self.profiles = []

    def add_profile(self, username: str, password: str):
        pwd = hashlib.sha256(password)
        self.profiles.append((username, pwd.hexdigest()))

    def remove_profile(self, username: str):
        for i in range(len(self.profiles)):
            if self.profiles[i][0] == username:
                self.profiles.remove(self.profiles[i])

class Login:
    database = Database()

    def __init__(self):
        self.username = None
        self.password = None
        self.logged_in = False

    def add_profile(self, username: str, password: str):
        self.database.add_profile(username, password)

    def login(self):
        self.username = input('USERNAME:')
        self.password = input('PASSWORD:')
        for item in database.profiles:
            if item[0] == self.username:
                pwd = hashlib.sha256(self.password)
                if pwd.hexdigest() == item[1]:
                    self.logged_in = True
                    print(f'LOGIN SUCCESSFUL! You are now signed in as {self.username}')
                    return
        if not self.logged_in:
            print('LOGIN FAILED!')

login = Login()
login.add_profile('EvanDenny', 'ejdenny1997')
login.login()
login()
