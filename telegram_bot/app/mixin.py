class TelegramBotAPIMixin:    

    def send_message(self, bot, message):
        chat_id = message.chat.id
        if message.text == "Hi!":
            bot.send_message(chat_id, "How you doing?")
    
    def start_handler(self, bot, message):
        chat_id = message.chat.id
        bot.send_message(chat_id, "Hello!")