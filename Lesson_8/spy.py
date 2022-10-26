from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime


def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('db.csv', 'a', encoding="utf-8") as file:
        file.write(
            f"{update.effective_user.first_name}-{update.effective_user.id}-{datetime.datetime.now().time()}-{update.message.text}\n")
