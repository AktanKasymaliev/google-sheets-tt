from app.tgbot import TelegramBotAPI
from configurations import config
from configurations import get_config_data

def main():
    config()

    TOKEN = get_config_data("TG_TOKEN")
    TelegramBotAPI(TOKEN)

if __name__ == "__main__":
    main()