"""From models.py importing User and UserList."""
from models import User, UserList

evan = User('Evan Denny')
offline_list = UserList('OFFLINE', [evan])
offline_list.display_users()
