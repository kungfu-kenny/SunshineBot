import os
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardButton


class ViewMenu:
    """
    class which is dedicated to return the     
    """
    def __init__(self) -> None:
        pass

    def return_main_keyboard(self) -> object:
        """
        Method which is dedicated to work with the main keyboard of the user
        """
        #TODO add here the buttons
        return ReplyKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('Hi', callback_data='1'),
                    InlineKeyboardButton('f', callback_data='1')
                ]
            ], 
            resize_keyboard=True, 
            one_time_keyboard=False
        )