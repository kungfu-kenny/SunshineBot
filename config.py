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
    button_send = 'Send 📨'
    button_settings = 'Settings ⚙️'
    button_profile = 'Profile 🙍‍♀️'
    button_help = 'Help ❓'
    button_donations = 'Support Us 💵'
    button_characteristics = 'Characteristics 📊'

class InlineButtonSend:
    button_sun = '1'
    button_cloud = '2'
    button_cock = '3'

class InlineButtonAdd:
    button_add = 'Add'
    button_delete = 'Delete'
    button_clear = 'Clear'

class CallbackReplyMain:
    callback_main_send = '100'
    callback_main_settings = '101'
    callback_main_profile = '102'
    callback_main_help = '103'
    callback_main_donations = '104'
    callback_main_characteristics = '105'

class CallbackSend:
    callback_send_sun = '000'
    callback_send_cloud = '001'
    callback_send_sun_cloud = '002'
    callback_send_cloud_sun = '003'
    callback_send_selected = lambda x: f"00{x}"
    