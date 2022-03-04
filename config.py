import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('TOKEN')
users_resend = [int(os.getenv('USER_DEFAULT', 0))]

class Folders:
    folder_here = os.getcwd()
    folder_logs = 'logs'
    folder_storage = 'storage'

class Commands:
    command_start = 'start'
    command_settings = 'settings'
    command_profile = 'profile'
    command_users = 'users'
    command_help = 'help'

class Buttons:
    button_settings = 'Settings'
    button_profile = 'Profile'
    button_help = 'Help'
    button_users = 'Users'

class InlineButtonSend:
    button_sun = '1'
    button_cloud = '2'
    button_cock = '3'

class InlineButtonAdd:
    button_add = 'Add'
    button_delete = 'Delete'
    button_clear = 'Clear'
    