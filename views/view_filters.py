from aiogram.types import Message
from aiogram.dispatcher.filters import Filter
from config import Buttons


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