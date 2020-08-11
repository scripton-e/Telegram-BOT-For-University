# Unfinished Code:
import telebot
from telebot import types 
bot = telebot.TeleBot("1077973012:AAEERUumAOdbescEtV86tIK-cnzEBTBHmig")
###################### [ Language Select ] ######################
@bot.message_handler(commands=['start','help'])
def welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=3)
    markup = types.ReplyKeyboardMarkup()
    language = types.KeyboardButton("English 🇺🇸")
    languagea = types.KeyboardButton("Polish 🇵🇱")
    languageb = types.KeyboardButton("Russian 🇷🇺")
    markup.row(language,languagea,languageb) 
    bot.send_message(message.chat.id, "Please select language / Proszę wybrać język / Пожалуйста выберите язык",reply_markup=markup)
####################### [ Languages / Functions] ##############################
@bot.message_handler(content_types=['text'])
def send_text(message):
    ##============================= [ English ] =============================##
    if message.text == "English 🇺🇸":
        pselect = types.ReplyKeyboardMarkup(row_width=2)
        pselect = types.ReplyKeyboardMarkup()
        pbus = types.KeyboardButton("Timetable")
        pkarta = types.KeyboardButton("Questions")
        pselect.row(pbus,pkarta)
        bot.send_message(message.chat.id,"Please select:", reply_markup=pselect)
    
    elif message.text == "Timetable":
        engkeyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Monday", callback_data="1")
        samshabati = types.InlineKeyboardButton(text="Tuesday", callback_data="2")
        otxshabati = types.InlineKeyboardButton(text="Wednesday", callback_data="3")
        xutshabati = types.InlineKeyboardButton(text="Thursday", callback_data="4")
        paraskevi = types.InlineKeyboardButton(text="Friday", callback_data="5")
        shabati = types.InlineKeyboardButton(text="Saturday", callback_data="6")
        engkeyboard.add(url_button,samshabati,otxshabati)
        engkeyboard.add(xutshabati,paraskevi,shabati)
        bot.send_message(message.chat.id,"Please select a day", reply_markup=engkeyboard)

    elif message.text == "Questions":
        questions = types.InlineKeyboardMarkup()
        qkey = types.InlineKeyboardButton(text = "Where is university?", callback_data="1")
        questions.add(qkey)
        bot.send_message(message.chat.id, "Select what you want", reply_markup=questions)
        bot.send_location(message.chat, latitude="50.040468", longitude="22.001913", disable_notification = FALSE,reply_to_message_id = NULL, reply_markup = NULL)
    ##============================= [ Polish ] =============================##
    elif message.text == "Polish 🇵🇱":
        pselect = types.ReplyKeyboardMarkup(row_width=2)
        pselect = types.ReplyKeyboardMarkup()
        pbus = types.KeyboardButton("Rozklad Jazdy")
        pkarta = types.KeyboardButton("Karta Pobyta")
        pselect.row(pbus,pkarta)
        bot.send_message(message.chat.id,"Prosze wybrac", reply_markup=pselect)

    elif message.text == "Rozklad Jazdy":
        prozklad = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Poniedziałek", callback_data="Infos")
        samshabati = types.InlineKeyboardButton(text="Wtorek", callback_data="2")
        otxshabati = types.InlineKeyboardButton(text="Środa", callback_data="3")
        xutshabati = types.InlineKeyboardButton(text="Czwartek", callback_data="4")
        paraskevi = types.InlineKeyboardButton(text="Piątek", callback_data="5")
        shabati = types.InlineKeyboardButton(text="Sobota", callback_data="6")
        prozklad.add(url_button,samshabati,otxshabati)
        prozklad.add(xutshabati,paraskevi,shabati)
        bot.send_message(message.chat.id,"Prosze wybra dzień:", reply_markup=prozklad)
    ##======================== [ Russian ] ========================== ##
    if message.text == "Russian 🇷🇺":
        pselect = types.ReplyKeyboardMarkup(row_width=2)
        pselect = types.ReplyKeyboardMarkup()
        pbus = types.KeyboardButton("Рассписание автобусов")
        pkarta = types.KeyboardButton("Вапроси")
        pselect.row(pbus,pkarta)
        bot.send_message(message.chat.id,"Сделайте выбор:", reply_markup=pselect)

    elif message.text == "Рассписание автобусов":
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Понедельни", callback_data="1")
        samshabati = types.InlineKeyboardButton(text="Вторник", callback_data="2")
        otxshabati = types.InlineKeyboardButton(text="Среда", callback_data="3")
        xutshabati = types.InlineKeyboardButton(text="Четверг", callback_data="4")
        paraskevi = types.InlineKeyboardButton(text="Пятница", callback_data="5")
        shabati = types.InlineKeyboardButton(text="Субота", callback_data="6")
        keyboard.add(url_button,samshabati,otxshabati)
        keyboard.add(xutshabati,paraskevi,shabati)
        bot.send_message(message.chat.id,"Выберите день:", reply_markup=keyboard)
###################################################

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
   if call.message:
        if call.data == "Infos":
            rust = types.InlineKeyboardMarkup()
            testb = types.InlineKeyboardButton(text="Select Next Dey",callback_data="Menu")
            rust.add(testb)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=rust,text= myfile.read())
            ##bot.register_next_step_handler( next step )

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)
#BOT RUN
if __name__ == "__main__":
    bot.polling(none_stop=True)  
#GITHUB : 
# https://github.com/scripton-e/Telegram-BOT-For-University