from typing import Any

from aiogram import Router
from aiogram.handlers import MessageHandler
from aiogram.methods import SendMessage

echo_router = Router()


@echo_router.message()
class MyHandler(MessageHandler):
    # название функции всегда handle, потому что это перезапись метода
    async def handle(self) -> Any:
        return SendMessage(chat_id=self.chat.id, text=self.event.text)
