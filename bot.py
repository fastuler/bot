from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# GANTI Bagian Ini
TOKEN = '7984749524:AAFf9_P04zdEz2bRwAwB-NsflWfqG4qTjbE'
CHANNEL_B = '@mochsup'  # Channel yang wajib diikuti
video_dict = {
    "video1": "https://t.me/channelasupanmu/101",
    "video2": "https://t.me/channelasupanmu/102",
    "video3": "https://t.me/channelasupanmu/103"
}

# Fungsi ketika user ketik /asupan
async def asupan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_B, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            link = random.choice(VIDEO_LINKS)
            await update.message.reply_text(f"Nih asupannya: {link}")
        else:
            raise Exception("Belum join")
    except:
        await update.message.reply_text(
            f"Kamu belum join channel utama!\nGabung dulu ya:\n{CHANNEL_B}"
        )

# Jalankan bot-nya
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("asupan", asupan))
    app.run_polling()
