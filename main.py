import os

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import Message

from aiohttp_srv import myapp, web
from plugins.querys import get_admins

api_id = os.environ['api_id']
api_hash = os.environ['api_hash']
bot_token = os.environ['bot_token']

app = Client(session_name='bot',
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token)


@app.on_message(filters.command("start") & filters.group)
async def start(client, message: Message):
    # await message.reply_text("Hello World!", reply_to_message_id=message.message_id)
    await message.reply_text("""
    سلام، ربات با موفقیت نصب شد.
    برای دیدن دستور های ربات /help را بفرستید.
    Digi Foss For Ever ✌
    """)


@app.on_message(filters.command("help") | filters.regex(r"^پ+ن+ل$"))
async def help_menu(c, m: Message):
    if get_admins(str(m.chat.id).strip("-"), m.from_user.id):
        await m.reply_text(
            """
        سلام. به پنل راهنما خوش امدید.
        برای اطلاع از دستور های ربات روی دکمه های زیر کلیک کنید.
        """,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "مدیریت گروه",
                        callback_data=
                        f"grp_management,{m.from_user.id}"  # Group_management
                    ),
                    InlineKeyboardButton(
                        'فان😜', callback_data=f"fun,{m.from_user.id}"),
                    InlineKeyboardButton(
                        "تنظیمات", callback_data=f"setting,{m.from_user.id}")
                ],
                [
                    InlineKeyboardButton(
                        "بستن پنل",
                        callback_data=f"cls_pnl,{m.from_user.id}"  # Close_panel
                    )
                ]
            ]))


async def job():
    await app.send_message(-1001154364334, "ّI'm up  /:")


scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=300)

scheduler.start()
# خط های بالا برای روشن نگه داشتن ربات روی هروکو هست، اگه شما از هروکو استفده نمیکنید  میتونید کامنت کنید
# یا اگه استفاده میکنید یه گروه بسازید و تو قسمت ارسال پیامش چت ایدی اون گروه رو قرار بدید
web.run_app(myapp)
app.run()

