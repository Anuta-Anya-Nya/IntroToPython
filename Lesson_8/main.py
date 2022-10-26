from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token(
    TOKEN).build()

# когда присылается "hi" команда, выполняется метод hi_command
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("help", help_command))

print("All ok")
app.run_polling()
