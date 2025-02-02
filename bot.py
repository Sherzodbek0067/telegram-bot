import telebot
from telebot import types

tg_bot = telebot.TeleBot(token="")
ADMIN_TELEGRAM_ID = 0000

backend_info = "🕸 Backend\n\n💻 Kurs 3 oy\n\n💵 O'ylik tolov 200.000 som\n\n⏳ Vaqt 10:30 12:00\n\n🌅 Kunlar - Dushanba Chorshanba Juma\n\n👩‍🏫 O'qituvchi - Axrorber"
frontend_info = "📝 Frontend\n\n 💻Kurs 7 oy\n\n💵 O'ylik tolov 250.000 som\n\n⏳ Vaqt 9:30 11:00\n\n🌅 Kunlar - Dushanba Chorshanba Juma\n\n👩‍🏫 O'qituvchi - Akmal"
komp_info = "🖥 Kompyuter savodxonlig\n\n💻 Kurs 3 oy\n\n💵 O'ylik tolov 200.000 som\n\n⏳ Vaqt 8:00 10:00\n\n🌅 Kunlar - Dushanba Chorshanba Juma\n\n👩‍🏫 O'qituvchi - Ilxomjon"
english_info  = "🏴󠁧󠁢󠁥󠁮󠁧󠁿 English\n\n📖 Kurs 6 oy\n\n💵 O'ylik tolov 150.000 som\n\n⏳ Vaqt 17:00 18:30\n\n🌅 Kunlar - Dushanba Chorshanba Juma\n\n👨‍🏫 O'qituvchi - Azizbek"

data_users = {}


@tg_bot.message_handler(commands=['start'])
def command_handler(message):
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton("📍 Bizning manzilimiz", url="https://www.google.com/maps/@40.658483,72.2424858,14z?entry=ttu&g_ep=EgoyMDI1MDEyMi4wIKXMDSoASAFQAw%3D%3D")
    item2 = types.InlineKeyboardButton("👥 Bizning kanalimiz", url="https://t.me/python_easy_ru")
    item3 = types.InlineKeyboardButton("📲 Admin bilan boglanish", callback_data="admin")
    item4 = types.InlineKeyboardButton("⚙️ Shikoyatlar va takliflar", callback_data="complaints")
    item5 = types.InlineKeyboardButton("ℹ️ Kurslarimizdan malumot olish", callback_data="curse")
    item6 = types.InlineKeyboardButton("📝 Ro'yxatan otish", callback_data="test")

    markup.row(item1, item2)
    markup.row(item3, item4)
    markup.row(item5)
    markup.row(item6)
    tg_bot.send_message(message.chat.id, f"😊 Assalomu aleykum {message.from_user.first_name}\n⚙️ Siz asosiy menyudasiz",reply_markup=markup)
    

@tg_bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "ortga":
        command_handler(call.message)

    elif call.data == "admin":
        admin(call.message)

    elif call.data == "complaints":
        data_admin(call.message)

    elif call.data == "test":
        tg_bot.send_message(call.message.chat.id, "Ism: ")
        tg_bot.register_next_step_handler(call.message, name_handler)


    elif call.data == "curse":
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton("Back-end", callback_data="back")
        b2 = types.InlineKeyboardButton("Front-end", callback_data="front")
        b3 = types.InlineKeyboardButton("Kompyuter savodxonligi", callback_data="komp")
        b4 = types.InlineKeyboardButton("English", callback_data="english")
        button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")

        markup.add(b1, b2)
        markup.add(b3, b4)
        markup.add(button)
        
        tg_bot.send_message(call.message.chat.id, "😊 Qaysi kursdan ma'lumot olmoqchisiz?", reply_markup=markup)

    if call.data == "back":
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")
        markup.add(button)
        tg_bot.send_message(call.message.chat.id, backend_info, reply_markup=markup)

    elif call.data == "front":
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")
        markup.add(button)
        tg_bot.send_message(call.message.chat.id, frontend_info, reply_markup=markup)

    elif call.data == "komp":
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")
        markup.add(button)
        tg_bot.send_message(call.message.chat.id, komp_info, reply_markup=markup)

    elif call.data == "english":
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")
        markup.add(button)
        tg_bot.send_message(call.message.chat.id, english_info, reply_markup=markup)

def admin(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")
    markup.add(button)
    tg_bot.send_message(message.chat.id, "📰 Ism Axror\n📞 Telefon raqami +998975676767", reply_markup=markup)


def data_admin(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton("⬅️ Ortga", callback_data="ortga")
    markup.add(button)
    tg_bot.send_message(message.chat.id, "🆘 Shikoyat va takliflaringizni yozib qoldiring", reply_markup=markup)
    tg_bot.register_next_step_handler(message, send_message_handler)


def send_message_handler(message):
    data = message.text
    tg_bot.send_message(ADMIN_TELEGRAM_ID, f"Yangi shikoyat/taklif:\n\n{data}")
    tg_bot.send_message(message.chat.id, "✅ Sizning xabaringiz yuborildi. Rahmat!")

def curse_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("Back-end")
    b2 = types.KeyboardButton("Front-end")
    b3 = types.KeyboardButton("Kompyuter savodxonligi")
    b4 = types.KeyboardButton("English")
    markup.add(b1, b2)
    markup.add(b3, b4)
    
    tg_bot.send_message(message.chat.id, "😊 Qaysi kursdan ma'lumot olmoqchisiz?", reply_markup=markup)


@tg_bot.callback_query_handler(func=lambda call: call.data == "test")
def test_registration(call):
    tg_bot.send_message(call.message.chat.id, "Ismingizni kiriting:")
    tg_bot.register_next_step_handler(call.message, name_handler)

def name_handler(message):
    chat_id = message.chat.id
    data_users[chat_id] = {'name': message.text}  # Сохраняем имя
    tg_bot.send_message(chat_id, "Familiyangizni kiriting:")
    tg_bot.register_next_step_handler(message, surname_handler)

def surname_handler(message):
    chat_id = message.chat.id
    data_users[chat_id]['surname'] = message.text  # Сохраняем фамилию
    tg_bot.send_message(chat_id, "Yoshingizni kiriting:")
    tg_bot.register_next_step_handler(message, age_handler)

def age_handler(message):
    chat_id = message.chat.id
    data_users[chat_id]['age'] = message.text  # Сохраняем возраст
    tg_bot.send_message(chat_id, "Telefon raqamingizni kiriting:")
    tg_bot.register_next_step_handler(message, phone_handler)

def phone_handler(message):
    chat_id = message.chat.id
    data_users[chat_id]['phone'] = message.text  # Сохраняем телефон

    user_info = data_users.pop(chat_id)  # Удаляем данные после сохранения

    response = (f"✅ Sizning ma'lumotlaringiz:\n"
                f"👤 Ism: {user_info['name']}\n"
                f"👥 Familiya: {user_info['surname']}\n"
                f"🎂 Yosh: {user_info['age']}\n"
                f"📞 Telefon: {user_info['phone']}")

    tg_bot.send_message(chat_id, response)

tg_bot.infinity_polling(skip_pending=True)