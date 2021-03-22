import telebot
import config
 
from telebot import types
 

 
@bot.message_handler(commands=['start'])

def welcome(message):
    #sti = open('static/welcome.webp', 'rb')
    #bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("1")
    item2 = types.KeyboardButton("2")
    item3 = types.KeyboardButton("3")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный, чтобы помочь тебе освоиться на новом рабочем месте.\nПросто выбери интересующий тебя вопрос и я с радостью отвечу :)".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup = markup)

    bot.send_message(message.chat.id, "Cписок вопросов:\n\n1. Предусмотрена ли денежная компенсация за переработки?\n2. Требуется ли соблюдать дресскод?\n3. Можно ли использовать свой банковский счет для перечисления зарплаты?".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup = markup)

@bot.message_handler(content_types=['text'])
def v1(message):
    if message.chat.type == 'private':
        if message.text == '1':
             bot.send_message(message.chat.id, 'Предусмотрена ли денежная компенсация за переработки?\n\nКонечно! Размер компенсации рассчитывается в соответствии с окладом. За подробностями обратитесь пожалуйста к бухгалтеру в каб.433')
             bot.send_message(message.chat.id, "Cписок вопросов:\n\n1. Предусмотрена ли денежная компенсация за переработки?\n2. Требуется ли соблюдать дресскод?\n3. Можно ли использовать свой банковский счет для перечисления зарплаты?".format(message.from_user, bot.get_me()),
                 parse_mode='html')
             
        elif message.text == '2':
             bot.send_message(message.chat.id, 'Требуется ли соблюдать дресскод?\n\nНет, форма одежды свободная. Разумеется, в пределах разумного :)')
             bot.send_message(message.chat.id, "Cписок вопросов:\n\n1. Предусмотрена ли денежная компенсация за переработки?\n2. Требуется ли соблюдать дресскод?\n3. Можно ли использовать свой банковский счет для перечисления зарплаты?".format(message.from_user, bot.get_me()),
                 parse_mode='html')    

        elif message.text == '3':
             bot.send_message(message.chat.id, 'Можно ли использовать свой банковский счет для перечисления зарплаты?\n\nТакой возможности не предусмотрено. Зарплатная карта выдается каждому сотруднику.')
             bot.send_message(message.chat.id, "Cписок вопросов:\n\n1. Предусмотрена ли денежная компенсация за переработки?\n2. Требуется ли соблюдать дресскод?\n3. Можно ли использовать свой банковский счет для перечисления зарплаты?".format(message.from_user, bot.get_me()),
                 parse_mode='html')    

        else:
            bot.send_message(message.chat.id, 'Выберите пожалуйста вопрос из списка')


# RUN
bot.polling(none_stop=True)
            
    
