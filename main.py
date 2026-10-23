import os
import asyncio
import logging

from pyrogram import Client

logging.basicConfig(level=logging.INFO)

API_ID = int(os.environ["API_ID"])
API_HASH = os.environ["API_HASH"]

# مثال: @my_channel یا شناسه عددی کانال
CHANNEL_ID = os.environ["CHANNEL_ID"]

# آیدی عددی کاربر مقصد
TARGET_USER_ID = int(os.environ["TARGET_USER_ID"])

app = Client(
    "my_personal_account",
    api_id=API_ID,
    api_hash=API_HASH,
    phone_number=os.environ.get("PHONE_NUMBER")
)


async def main():
    async with app:
        me = await app.get_me()
        print(f"Logged in as: {me.first_name} (@{me.username})")

        # دریافت آخرین پیام کانال
        messages = [
            message async for message in
            app.get_chat_history(CHANNEL_ID, limit=1)
        ]

        if not messages:
            print("کانال پیام ندارد.")
            return

        message = messages[0]

        # ارسال یا فوروارد پیام به پیوی مقصد
        await app.forward_messages(
            chat_id=TARGET_USER_ID,
            from_chat_id=CHANNEL_ID,
            message_ids=message.id
        )

        print("آخرین پیام با موفقیت فوروارد شد.")


if __name__ == "__main__":
    app.run(main())
