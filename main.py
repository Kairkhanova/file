from telebot import TeleBot
TOKEN = '7594451885:AAG2Y8fRgnObuqc6TIgkpvc88rdmfo_dD9g'
bot= TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет!')

if __name__ == '__main__':
    bot.polling(none_stop=True)