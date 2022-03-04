from config import Buttons


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
    Output: string to the reply
    """
    return {
            Buttons.button_send : "Send menu",
            Buttons.button_profile : "Your Profile",
            Buttons.button_settings: "Your Settings",
    }.get(value_text, 'Error with the given values')