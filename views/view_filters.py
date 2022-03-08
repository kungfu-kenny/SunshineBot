from aiogram.types import Message
from aiogram.dispatcher.filters import Filter
from aiogram.utils.callback_data import CallbackData
from config import Buttons, CallbackHelp


class CheckBasicFilter(Filter):
    key = "is_basic_filter"
    async def check(self, message: Message) -> bool:
        return any(
            [
                message.text.strip() == f for f in 
                [
                    Buttons.button_send,
                    Buttons.button_profile,
                    Buttons.button_settings,
                    Buttons.button_characteristics,
                    Buttons.button_help,
                    Buttons.button_donations
                ]
            ]
        )

class CheckPublicPrivateFilter(Filter):
    key = "is_private_message"
    async def check(self, message: Message) -> bool:
        return message.chat.type == "private"

class CheckMessageForwarded(Filter):
    key = "is_forward_user_message"
    async def check(self, message: Message) -> bool:
        if not message.forward_from:
            return False
        return message.chat.id != message.forward_from.id and not message.forward_from.is_bot
        
class CheckCallbackHelp(Filter):
    key = "is_callback_help"
    async def check(self, callback: CallbackData) -> bool:
        return callback.data in CallbackHelp.callback_all