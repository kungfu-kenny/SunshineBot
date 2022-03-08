import os
from dotenv import load_dotenv


load_dotenv()

token = os.getenv('TOKEN')
users_resend = [int(os.getenv('USER_DEFAULT', 0))]

class Folders:
    folder_here = os.getcwd()
    folder_logs = 'logs'
    folder_storage = 'storage'
    db = 'database.sql'

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

class ButtonBasic:
    button_next = '➡️'
    button_prev = '⬅️'
    button_true = '✅'
    button_false = '❌'

class InlineButtonSend:
    button_sun = [1, '☀️']
    button_cloud = [2, '☁️']
    button_sun_cloud = [3, '🌤']
    button_cloud_sun = [4, '⛅️']

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
    callback_send_sun = '001'
    callback_send_cloud = '002'
    callback_send_sun_cloud = '003'
    callback_send_cloud_sun = '004'
    callback_send_selected = lambda x: f"00{x}"
    callback_all = [
        callback_send_cloud_sun, 
        callback_send_cloud, 
        callback_send_sun_cloud, 
        callback_send_cloud_sun
    ]

class CallbackHelp:
    callback_help_basic_description = '200'
    callback_help_add_emotions = '201'
    callback_help_add_users = '202'
    callback_help_about_us = '203'
    callback_all = [
        callback_help_basic_description, 
        callback_help_add_emotions, 
        callback_help_add_users, 
        callback_help_about_us
    ]