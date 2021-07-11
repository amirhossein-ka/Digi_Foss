from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(filters.command("id") & filters.user(258564057))
async def return_id(_, m: Message):
    await m.reply_text(str(m.reply_to_message.message_id))


@Client.on_message(filters.command("chat_id") & filters.user(258564057))
async def chat_id(_, m: Message):
    await m.reply_text(str(m.chat.id))
