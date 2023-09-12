"""Module provides 'randint' function for setting User's 
ID Number to a random integer between 100_000 and 999_999."""
from random import randint

class User:
    """User profile for logging into an interface."""
    def __init__(self, name: str | None):
        self.name = name
        self.password = ''
        self.id_number = randint(100_000, 999_999)
        self.dob = {'dob':'','month':'','day':'','year':''}

    def create_password(self):
        """Set the Password for the User."""
        self.password = input('Create your password: ')

    def set_dob(self, month: str, day: str | int, year: str | int):
        """Set the Date of Birth (DOB) for the User."""
        self.dob['month'] =  month
        self.dob['day'] = day
        self.dob['year'] = year
        self.dob['dob'] = str(month)+' '+str(day)+', '+str(year)

    def __hide_password(self):
        return len(self.password)*'*'

    def display_user(self):
        """Displays information within the User's profile."""
        print('Name:',self.name)
        print('DOB:',self.dob['dob'])
        print('Password:',self.__hide_password())

    def setup(self):
        """Setup a new User from scratch."""
        print('CREATE NEW USER:')

class UserList:
    """Container for organizing Users based on activity. i.e. ONLINE/OFFLINE"""
    def __init__(self, title: str, users: list | None):
        self.title = title
        if users is None:
            self.users = []
        elif users is not None:
            self.users = users

    def display_users(self):
        """Displays Users in list of users."""
        a=1
        print(self.title+":")
        for item in self.users:
            print(str(a)+'.',item.name)
            a+=1

    def change_title(self, title: str):
        """Change the title of the UserList."""
        self.title = title

    def add_user(self, user: User):
        """Add one User to the users list."""
        self.users.append(user)

    def add_users(self, users: list):
        """Add multiple Users to the users list."""
        for item in users:
            self.users.append(item)

    def delete_user(self, user: User):
        # DOESN'T WORK
        """Delete User from the users list."""
        for item in self.users:
            if item == user:
                del item

class Interface:
    """Interface for User interacting with some system."""
    def __init__(self, title: str):
        self.title = title
        self.user = None
        self.logged_in = False
        self.user_lists = {'Default': UserList('Default', None)}
        self.admin = False
        self.access = set()

    def add_user_list(self, user_list: UserList):
        """Add a UserList to the user_lists dictionary. 
        Accessing the list: self.user_lists[user_list.title]"""
        self.user_lists[user_list.title] = user_list.users

    def set_access(self, user_list: UserList, access: bool):
        """Set whether UserList has access to special functions/methods."""
        if access:
            self.access += self.user_lists[user_list.name]
        else:
            self.access -= self.user_lists[user_list.name]

    def login(self):
        """Login to the Interface via a User's name."""
        user = input('Enter your name: ')
        for item in self.user_lists['Default'].users:
            if user == item.name:
                self.logged_in = True
                self.user = user
        if self.logged_in:
            print('LOGIN SUCCESSFUL! Welcome,',user+'.')
        else:
            print('LOGIN FAILED! Please try again.')

    def __check_access(self):
        """Checks whether logged in User has permissions to use certain
        functions/methods."""
        if self.user is None:
            self.admin = False
            print('Access denied.')
            return
        for item in self.access:
            for user in item.users:
                if self.user == user:
                    self.admin = True
                    return
        self.admin = False

    def test_method(self):
        """Testing __check_access() method."""
        self.__check_access()
        if self.admin:
            print('If this text appears, __check_access() method is working.')
