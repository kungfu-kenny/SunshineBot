from config import Buttons, CallbackHelp


def text_start(name_first:str, name_last:str, name_user:str) -> str:
    """
    Function to return the introduction text
    Input:  name_first = first name of the user
            name_last = last name of the user
            name_user = username
    Output: we developed the string to greetings 
    """
    #TODO change the text after
    return "Hi!\nI'm EchoBot!\nPowered by aiogram."

def text_inline_after_reply(value_text:str) -> str:
    """
    Function to return text after the reply to it
    Input:  value_text = text value
    Output: string to the reply in the Inline menus
    """
    return {
            Buttons.button_send : "Send menu",
            Buttons.button_profile : "My Profile",
            Buttons.button_settings: "My Settings",
            Buttons.button_donations: "Support Us",
            Buttons.button_help: "FAQ",
            Buttons.button_characteristics: "My Statistics",

    }.get(value_text, 'Error with the given values')

def text_user_return(value_list:list) -> set:
    """
    Function which is dedicated to return the user for it
    Input:  value_list = list of the selected user info
    Output: set with id and name
    """
    user_id, user_name_first, user_name_last, username = value_list
    if username: 
        return user_id, f"@{username}"
    elif user_name_first or user_name_last:
        return user_id, ' '.join([user_name_first, user_name_last]).strip()
    return user_id, 'unknown'

def text_user_help(callback_help:str) -> str:
    """
    Function which is dedicated to work with the 
    Input:  callback_help = callback which is dedicated to return selected text
    Output: we developed the selected text
    """
    if callback_help == CallbackHelp.callback_help_about_us:
        return \
            "Text about us "
    if callback_help == CallbackHelp.callback_help_add_emotions:
        return \
            "Text add emotions which would be changed"
    if callback_help == CallbackHelp.callback_help_add_users:
        return \
            "Text add users to all of it"
    if callback_help == CallbackHelp.callback_help_basic_description:
        return \
            "Text about the basic description"