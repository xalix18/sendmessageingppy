import random
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, filters
)

TOKEN = "8569569823:AAGtEBlMeUinAZzLZMbWOe-ChzJQPTXS5sY"

# پیام‌های پیشنهادی ربات
messages = [
    "کیر",
    "کص",
    "مادرجنده",
    "پدرسگ",
    "خواهرجنده",
    "کونی",
    "جنده",
    "لاشی",
    "گاییدم",
    "بکنمت",
    "سگ",
    "حرومزاده",
    "کصکش",
    "کیرم تو دهنت",
    "گوزو",
    "گوه خوردم",
    "کص ننه",
    "کیر خر",
    "لخت مادر",
    "تخم سگ",
    "کص عمه",
    "کیر تو کون بابات",
    "مادرتو گاییدم",
    "جاکش",
    "کصکش حرفه‌ای",
    "کونی گشاد",
    "گاییدم ننه‌تو",
    "کصخل",
    "کیر کلفت",
    "جنده‌خانه",
    "کص لیس",
    "گوزیدم تو صورتت",
    "کیرم تو مغزت",
    "مادرقهوه",
    "کص بابا",
    "حرومی",
    "کونی بی‌شرف",
    "گاییدم خواهرتو",
    "کصکش خایه‌مال",
    "کیر ساطانی",
    "جنده‌ی محل",
    "کص ننه‌ی مرده",
    "گوه تو سرت",
    "کیرم دهنت سرویس",
    "مادرتو دراز کش",
    "کونی کثیف",
    "گاییدم عمتو",
    "کصکش بی‌ریشه",
    "کیر تو چشمات",
    "جنده‌ی اینترنتی",
    "گوز گوسفند",
    "کص لیس حرفه‌ای",
    "مادرجنده‌ی محل",
    "کونی بی‌غیرت",
    "گاییدم کل فامیلت",
    "کصکش بی‌کلاس",
    "کیر تو کله‌ت",
    "جنده‌ی خیابونی",
    "گوه تو کاسه‌ت",
    "کص ننه‌ی تازه",
    "کونی پاره",
    "گاییدم خاله‌تو",
    "کصکش خاین",
    "کیر تو گوشت",
    "جنده‌ی ارزون",
    "گوز تو دهنت",
    "کص لیس بی‌شرف",
    "مادرتو سگ گایید",
    "کونی لخت",
    "گاییدم دایی‌تو",
    "کصکش بی‌مغز",
    "کیر تو قلبم",
    "جنده‌ی حرفه‌ای",
    "گوه تو کون بابات",
    "کص ننه‌ی گشاد",
    "کونی بی‌ریخت",
    "گاییدم عمه‌تو",
    "کصکش بی‌ادب",
    "کیر تو رگت",
    "جنده‌ی کثیف",
    "گوز تو مغزت",
    "کص لیس بی‌کلاس",
    "مادرجنده‌ی تازه",
    "کونی بی‌مزه",
    "گاییدم زن‌عموتو",
    "کصکش بی‌وجدان",
    "کیر تو کون مامانت",
    "جنده‌ی بی‌شرف",
    "گوه تو چشمات",
    "کص ننه‌ی پاره",
    "کونی گشادکن",
    "گاییدم شوهرخاله‌تو",
    "کصکش بی‌دین",
    "کیر تو کله‌خرت",
    "جنده‌ی بی‌کلاس",
    "گوز تو کاسه‌سرت",
    "کص لیس بی‌غیرت",
    "مادرتو گاییدم تو قبر",
    "کونی بی‌مادر",
    "گاییدم کل محله‌تو",
    "کصکش بی‌وطن",
    "کیر تو کون خواهرت",
    "جنده‌ی بی‌ریشه",
    "گوه تو دهن بابات",
    "کص ننه‌ی کثیف",
    "کونی بی‌عرضه",
    "گاییدم نامزدتو",
    "کصکش بی‌لیاقت",
    "کیر تو مغز خواهرت",
    "جنده‌ی بی‌حیا",
    "گوز تو صورت مامانت",
    "کص لیس بی‌وجدان",
    "مادرجنده‌ی بی‌شرف",
    "کونی بی‌دین",
    "گاییدم همسایه‌تو",
    "کصکش بی‌اخلاق",
    "کیر تو کون عمه‌ت",
    "جنده‌ی بی‌ادب",
    "گوه تو کون خواهرت",
    "کص ننه‌ی بی‌غیرت",
    "کونی بی‌کلاس",
    "گاییدم رئیس‌تو",
    "کصکش بی‌مغز",
    "کیر تو دهن عموت",
    "جنده‌ی بی‌مزه",
    "گوز تو کون بابات",
    "کص لیس بی‌کفایت",
    "مادرتو گاییدم با سگ",
    "کونی بی‌وجدان",
    "گاییدم معلم‌تو",
    "کصکش بی‌ریخت",
    "کیر تو کون خاله‌ت",
    "جنده‌ی بی‌لیاقت",
    "گوه تو صورت خواهرت",
    "کص ننه‌ی بی‌کلاس",
    "کونی بی‌اخلاق",
    "گاییدم دوست‌دخترتو",
    "کصکش بی‌حیا",
    "کیر تو مغز بابات",
    "جنده‌ی بی‌وجدان",
    "گوز تو کون مامانت",
    "کص لیس بی‌ادب",
    "مادرجنده‌ی بی‌کلاس",
    "کونی بی‌مغز",
    "گاییدم همکارتو",
    "کصکش بی‌کثافت",
    "کیر تو کون دایی‌ت",
    "جنده‌ی بی‌مغز",
    "گوه تو دهن خواهرت",
    "کص ننه‌ی بی‌مزه",
    "کونی بی‌کثافت",
    "گاییدم رئیس‌جمهور",
    "کصکش بی‌عرضه",
    "کیر تو کون نامزدت",
    "جنده‌ی بی‌کثافت",
    "گوز تو صورت بابات",
    "کص لیس بی‌مزه",
    "مادرتو گاییدم تو حموم",
    "کونی بی‌عرضه",
    "گاییدم همکلاسی‌تو",
    "کصکش بی‌دین",
    "کیر تو مغز مامانت",
    "جنده‌ی بی‌عرضه",
    "گوه تو کون عمه‌ت",
    "کص ننه‌ی بی‌کثافت",
    "کونی بی‌لیاقت",
    "گاییدم استادتو",
    "کصکش بی‌مزه",
    "کیر تو کون شوهرعمه‌ت",
    "جنده‌ی بی‌دین",
    "گوز تو دهن مامانت",
    "کص لیس بی‌کثافت",
    "مادرجنده‌ی بی‌مزه",
    "کونی بی‌حیا",
    "گاییدم فامیل دور",
    "کصکش بی‌کلاس",
    "کیر تو کون خاله‌ت",
    "جنده‌ی بی‌حیا",
    "گوه تو صورت عمه‌ت",
    "کص ننه‌ی بی‌حیا",
    "کونی بی‌کلاس",
    "گاییدم کل ایران",
    "کصکش بی‌حیا",
    "کیر تو کون کل فامیل",
    "جنده‌ی بی‌کلاس",
    "گوز تو کون کل دنیا",
    "کص لیس بی‌کلاس",
    "مادرجنده‌ی کل عالم",
    "کونی کل کون",
    "گاییدم همه رو"
]

# ذخیره اعضای هر گروه
def add_user(chat_id, user_id, context):
    if "members" not in context.bot_data:
        context.bot_data["members"] = {}

    if chat_id not in context.bot_data["members"]:
        context.bot_data["members"][chat_id] = set()

    context.bot_data["members"][chat_id].add(user_id)

# حذف عضو هنگام خروج
def remove_user(chat_id, user_id, context):
    if "members" in context.bot_data:
        if chat_id in context.bot_data["members"]:
            if user_id in context.bot_data["members"][chat_id]:
                context.bot_data["members"][chat_id].remove(user_id)

# هر ساعت یک نفر را انتخاب و تگ کن
async def random_pick(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.data["chat_id"]

    # اگر هنوز members ساخته نشده، یعنی کسی چیزی ننوشته → خروج
    if "members" not in context.bot_data:
        return

    members = context.bot_data["members"].get(chat_id, [])

    if not members:
        return

    user_id = random.choice(list(members))
    msg = random.choice(messages)

    mention = f"[کاربر]({f'tg://user?id={user_id}'})"

    await context.bot.send_message(
        chat_id,
        f"{mention} {msg}",
        parse_mode="MarkdownV2"
    )


# شروع تایمر
# شروع تایمر (نسخه دقیقه‌ای برای تست سریع)
async def start_timer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("فرمت:\n/starttimer 1  (یعنی هر ۱ دقیقه)")
        return

    minutes = int(context.args[0])
    chat_id = update.effective_chat.id

    context.job_queue.run_repeating(
        random_pick,
        interval=minutes * 60,   # هر X دقیقه
        first=5,                 # ۵ ثانیه بعد از دستور تست
        data={"chat_id": chat_id},
        name=str(chat_id)
    )

    await update.message.reply_text(f"⏳ تایمر هر {minutes} دقیقه فعال شد!")

# ذخیره اعضا هنگام پیام دادن
async def save_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    add_user(chat_id, user_id, context)

# عضو جدید وارد شد
async def new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id

    for user in update.message.new_chat_members:
        add_user(chat_id, user.id, context)

# عضو خارج شد
async def left_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    user = update.message.left_chat_member
    remove_user(chat_id, user.id, context)

# ساده‌ترین دستور شروع
async def start(update, context):
    await update.message.reply_text("ربات فعال شد! 🤖")

app = ApplicationBuilder().token(TOKEN).build()

# دستورات
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("starttimer", start_timer))

# ذخیره‌سازی اعضا
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_user))
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, new_member))
app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, left_member))

print("Bot running...")
app.run_polling()
