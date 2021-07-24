import telebot
import wikipedia

bot = telebot.TeleBot("1898553724:AAGZU4Uy3WqjwBJFa9GKfy1GWH1mNP6MLfc")


@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, "Я говорю, кто правил в стране некоторое определенное количество лет назад. Чтобы начать, "
                          "введи /start"
                          "Это простыня текста уже у третьего бота")
    sticker = open("C:\\Users\\Lex\\Desktop\\pythonProject\\wikip.webp", "rb")
    bot.send_sticker(message.chat.id, sticker)


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, "Цена аренды?")
        bot.register_next_step_handler(message, get_answer)
        print(message.date)
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


def get_answer(message):
    print("Бот работает")
    wiki = int(message.date) ## переменная от 2 бота
    pricemnoj = str(message.text)
    end_date=1627178400
    print(wiki)
    print(pricemnoj)
    if pricemnoj.isdigit():
        napkin=float((end_date/60//60)-(wiki/60//60))*float(pricemnoj)
        if napkin<0:
            bot.send_message(message.from_user.id, "Я ем детей и одобряю австрийских художников, а еще")
        bot.send_message(message.from_user.id, napkin)
    else:
        print("pro chydo chydesa")
        check_fail(message)




    ##bot.register_next_step_handler(message, get_answer)


def check_fail(message):
    bot.send_message(message.from_user.id, "Жди гостей")
    wikipedia.set_lang("ru")
    print("Я здесь")
    i = 0
    page = wikipedia.page("О культе личности и его последствиях").content
    while True:
        if i+1000 < len(page):
            part_page = page[i:i + 1000]
            i += 1000
            bot.send_message(message.chat.id, part_page)
        else:
            part_page = page[i:len(page)-1]
            bot.send_message(message.chat.id, part_page)
            break


bot.polling(none_stop=True, interval=0)
