from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = "7984749524:AAFf9_P04zdEz2bRwAwB-NsflWfqG4qTjbE"  # atau os.environ.get("TOKEN")
CHANNEL_B = '@mochsup'

video_file_ids = {
    "video1": "BAACAgIAAxkBAAIDmF9r9PlExampleFileId1",
    "video2": "BAACAgIAAxkBAAIDmV9r9PlExampleFileId2",
    "video3": "BAACAgIAAxkBAAIDmV9r9PlExampleFileId3"
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    args = context.args
    if not args:
        await update.message.reply_text("Halo! Kirim perintah /asupan [kode_video]\nContoh: /asupan video1")
        return

    kode = args[0].lower()

    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_B, user_id=user_id)
        if member.status not in ['member', 'administrator', 'creator']:
            await update.message.reply_text(f"Kamu harus join channel dulu: {CHANNEL_B}")
            return
    except:
        await update.message.reply_text(f"Kamu harus join channel dulu: {CHANNEL_B}")
        return

    if kode in video_file_ids:
        await context.bot.send_video(chat_id=update.effective_chat.id, video=video_file_ids[kode])
    else:
        await update.message.reply_text("Kode video tidak ditemukan. Coba lagi.")

async def asupan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await start(update, context)

async def handle_video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    video = update.message.video
    if video:
        file_id = video.file_id
        await update.message.reply_text(f"File ID video kamu:\n{file_id}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("asupan", asupan))
    app.add_handler(MessageHandler(filters.VIDEO, handle_video))
    app.run_polling()
