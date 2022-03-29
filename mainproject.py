from telegram.ext import *
import responses as Res

print ('Bot started Now....')

def start(update,context):
    update.message.reply_text("type something to get started")

def help(update,context):
    update.message.reply_text("if you need help We will Reply soon")

def handlmsg(update,context):
    print(update.message.text)
    text=str(update.message.text).lower()
    response=Res.response(text)
    update.message.reply_text(response)

def error(update, context):
    print(f'Update {update} caused error{context.error}')

def main():
    updater=Updater('API_KEY From Botfather',use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text,handlmsg))
    dp.add_error_handler(error)
    updater.start_polling(timeout=600)
    
    updater.idle()
main()
