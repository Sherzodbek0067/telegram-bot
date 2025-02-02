import telebot 
import random

data_random_number = random.randint(1,5)
user_card = 7777

bot = telebot.TeleBot(token="")

@bot.message_handler(commands=['start'])
def main(message):
    # kirituvchidan raqam sorayapan
    bot.send_message(message.chat.id, f"1:5 kiriting {data_random_number}!")
    # data func kiritilgan raqamni jonatyapan !
    bot.register_next_step_handler(message, data)

def data(message):
    # user_num ni text ga tenglayapan 
    user_num = message.text
    # raqamlika tekshiramiz
    if user_num.isdigit() and 1 <= int(user_num) <= 5:
        if int(user_num) == data_random_number:
            test_fun(message)

        else:
            bot.reply_to(message, text=f"Komyuter tanlovi {data_random_number}\nUser tanlovi {user_num} !")
        
    else:
        main(message)

def test_fun(message):
    bot.reply_to(message, text="Sen to'ri topting \nkarta raqamini kirit !")
    bot.register_next_step_handler(message, payme_fun)

def payme_fun(message):
    card_code = message.text
    if card_code.isdigit() and int(card_code) == user_card:
        bot.send_message(message.chat.id, text="Karta parol tastixlandi!\nBalansingiz toldirildi")
    else:
        test_fun(message)
        
bot.polling()