profiles_db = [('EvanDenny', 'evandenny')]

class Login:
    database = []
    username = None
    password = None
    success = False

    def __init__(self, database: list):
        self.database = database
    
    def __call__(self):
        while not self.success:
            self.username = input("USERNAME: ")
            self.password = input("PASSWORD: ")
            self.check_db()
            if not self.success:
                print('Login UNSUCCESSFUL! Please try again. ')
        print('Login SUCCESSFUL!')

    def check_db(self):
        for item in self.database:
            if item[0] == self.username and item[1] == self.password:
                self.success = True

login = Login(profiles_db)
login()