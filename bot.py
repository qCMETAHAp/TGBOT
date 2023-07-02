from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import chatgpt

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот для создания уникальных поздравлений. Пожалуйста, ответьте на несколько вопросов, чтобы я мог составить поздравление для вас.")

def handle_message(update, context):
    message_text = update.message.text
    # Вызов API ChatGPT и получение ответа
    response = chatgpt.call_api(message_text, api_key=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)
    generated_text = response['generated_text']
    # Отправка сгенерированного текста пользователю
    context.bot.send_message(chat_id=update.effective_chat.id, text=generated_text)

updater = Updater(token=5961691201:AAGjx3QSL7K67Q14i_qmV0Lt5qw790T-n1c, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

message_handler = MessageHandler(Filters.text & (~Filters.command), handle_message)
dispatcher.add_handler(message_handler)

updater.start_polling()

