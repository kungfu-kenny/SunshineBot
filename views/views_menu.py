import os
from aiogram.types import (
    ReplyKeyboardMarkup, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup
)
from views.views_callback import cbc
from config import (
    ButtonBasic,
    Buttons, 
    CallbackSend, 
    CallbackHelp,
    CallbackReplyMain
)


class ViewMenu:
    """
    class which is dedicated to return the     
    """
    def __init__(self) -> None:
        self.dictionary_inline = {
            Buttons.button_send : self.return_user_send,
            Buttons.button_profile: self.return_user_profile,
            Buttons.button_settings: self.return_user_settings,
            Buttons.button_characteristics: self.return_user_characteristics,
            Buttons.button_help: self.return_user_help,
            Buttons.button_donations: self.return_user_donations,
        }
        
    @staticmethod
    def return_user_donations(value_id:int) -> object:
        """
        Method which is dedicated to work with the donations
        Input:  value_id = id of the
        Output: we developed the donation to the selected values
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        'Check',
                        callback_data='1223314'
                    ),
                    InlineKeyboardButton(
                        'Check',
                        callback_data='1223314'
                    )
                ]
            ]
        )

    @staticmethod
    def return_user_help(value_id:int) -> object:
        """
        Method which is dedicated to work with the help
        Input:  value_id = id of the
        Output: we developed the help to the user
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        'Basic Description',
                        callback_data=\
                            CallbackHelp.callback_help_basic_description
                            # cbc.new(action='help', id=CallbackHelp.callback_help_basic_description)
                        )
                ],
                [
                    InlineKeyboardButton(
                        'Add emotions',
                        callback_data=\
                            CallbackHelp.callback_help_add_emotions
                            # cbc.new(action='help', id=CallbackHelp.callback_help_add_emotions)
                    ),
                    InlineKeyboardButton(
                        'Add users',
                        callback_data=\
                            CallbackHelp.callback_help_add_users
                            # cbc.new(action='help', id=CallbackHelp.callback_help_add_users)
                    )
                ],
                [
                    InlineKeyboardButton(
                        'About us',
                        callback_data=\
                            CallbackHelp.callback_help_about_us
                            # cbc.new(action='help', id=CallbackHelp.callback_help_about_us)
                    )
                ]
            ]
        )

    @staticmethod
    def return_user_characteristics(value_id:int) -> object:
        """
        Method which is dedicated to produce the 
        Input:  value_id = id of the selected values
        Output: we developed the characteristics to the user
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        'Sent from me',
                        callback_data='1223314'
                    ),
                    InlineKeyboardButton(
                        'Sent to me',
                        callback_data='1223314'
                    )
                ]
            ]
        )

    @staticmethod
    def return_user_settings(value_id:int) -> object:
        """
        Method which is dedicated to work with the user settings to it
        Input:  value_id = id of the selected user
        Output: we developed the settings module of the user
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        'Notifications',
                        callback_data='1223314'
                    ),
                    InlineKeyboardButton(
                        ButtonBasic.button_true,
                        callback_data='1223314'
                    )
                ]
            ]
        )

    @staticmethod
    def return_user_profile(value_id:int) -> object:
        """
        Static method which is about to return the prodile value
        Input:  value_id = id value of the 
        Output: we developed the Inline values to the
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        'Check',
                        callback_data='1223314'
                    ),
                    InlineKeyboardButton(
                        'Check',
                        callback_data='1223314'
                    )
                ]
            ]
        )

    @staticmethod
    def return_user_send(value_id:int) -> object:
        """
        Static method to return the
        Input:  value_id = id of the selected user
        Output: Inline markup
        """
        return InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        'Check',
                        callback_data='1223314'
                    ),
                    InlineKeyboardButton(
                        'Check',
                        callback_data='1223314'
                    )
                ]
            ]
        )

    def return_main_key_board_values(self, value_text:str, value_id:int) -> object:
        """
        Method which is dedicated to work with the continue of the start
        Input:  value_text = string of start menu
                value_id = id of the selected user
        Output: object of the see 
        """
        return self.dictionary_inline.get(value_text, lambda x: None)(value_id)

    @staticmethod
    def return_main_keyboard() -> object:
        """
        Method which is dedicated to work with the main keyboard of the user
        Input:  None
        Output: reply menu for the start
        """
        return ReplyKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        Buttons.button_send, 
                    ),
                    InlineKeyboardButton(
                        Buttons.button_profile, 
                    )
                ],
                [
                    InlineKeyboardButton(
                        Buttons.button_settings, 
                    ),
                    InlineKeyboardButton(
                        Buttons.button_characteristics, 
                    ),
                    InlineKeyboardButton(
                        Buttons.button_help, 
                    )
                ],
                [
                    InlineKeyboardButton(
                        Buttons.button_donations, 
                    )
                ]
            ], 
            resize_keyboard=True, 
            one_time_keyboard=False
        )