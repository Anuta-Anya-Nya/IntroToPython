from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *


async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi, {update.effective_user.first_name}!')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    items = msg.split()  # sum 123 123
    if len(items) < 3:
        await update.message.reply_text(f'введите оба числа!')
        return 0
    x = items[1]
    y = items[2]
    if not x.isdigit() or not y.isdigit():
        await update.message.reply_text(f'введены неправильные числа!')
    else:
        x = int(x)
        y = int(y)
        await update.message.reply_text(f'{x} + {y} = {x+y}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/help')
