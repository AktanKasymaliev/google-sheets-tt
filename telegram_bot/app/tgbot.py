from .mixin import TelegramBotAPIMixin

from telebot import TeleBot

class TelegramBotAPI(TelegramBotAPIMixin):    
    
    def __init__(self, token: str) -> None:
        self.bot = self.create_bot(token)

        @self.bot.message_handler(commands=['start'])
        def __start_handler(message):
            self.start_handler(self.bot, message)
        
        @self.bot.message_handler(content_types=['text'])
        def __send_message(message):
            self.send_message(self.bot, message)
        
        self.infinity_polling()

    def infinity_polling(self):
        self.bot.infinity_polling()

    def create_bot(self, token: str) -> TeleBot:
        return TeleBot(token, parse_mode='html')