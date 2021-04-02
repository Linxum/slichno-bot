import telebot
import time
import vk
import govno
import tg_analytic
# Токен и клавиатура
bot = telebot.TeleBot('1692814273:AAFQ7UzpKP9X2JGVGeWtv1jKgRNCcZn0XHo')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Наши стикеры', 'Ссылки', 'О нас', 'Наша музыка', 'Последняя новость группы')

# Начальные сообщения
@bot.message_handler(commands=['start'])
def start(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Привет!')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Это бот слишкомлично')
    time.sleep(1)
    bot.send_message(message.chat.id, 'Выберите, что вам нужно:', reply_markup=keyboard1)

# О нас
@bot.message_handler(commands=['about'])
def about(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Привет,друг! Мы группа из Губкина. Играем рок в своё удовольствие. Можешь ознакомиться с нашим творчеством;) По кнопке найдёте все ссылки. Yда4и¡')


# Ссылки
@bot.message_handler(commands=['links'])
def links(message):
    tg_analytic.statistics(message.chat.id, message.text)

    vk = telebot.types.InlineKeyboardMarkup()
    peoples = telebot.types.InlineKeyboardMarkup()
    link = telebot.types.InlineKeyboardMarkup()

    group_vk = telebot.types.InlineKeyboardButton(text='Группа в ВК', url='https://vk.com/clishkomlichnoe')
    vk.add(group_vk)
    music_vk = telebot.types.InlineKeyboardButton(text='Музыка в ВК', url='https://vk.com/artist/clishkomlichnoe')
    vk.add(music_vk)
    bot.send_message(message.chat.id, "ВК", reply_markup=vk)

    spotify = telebot.types.InlineKeyboardButton(text='Spotify', url='https://open.spotify.com/artist/2XAkDxAqUKgoR6rxtIl5as?si=a3382b4a434f4609')
    link.add(spotify)
    yandex = telebot.types.InlineKeyboardButton(text='Яндекс.Музыка', url='https://music.yandex.ru/artist/9584394')
    link.add(yandex)
    time.sleep(1)
    bot.send_message(message.chat.id, "Ссылки на другие ресурсы", reply_markup=link)

    morozov = telebot.types.InlineKeyboardButton(text='Солист', url="https://vk.com/idbynelka")
    peoples.add(morozov)
    guitar = telebot.types.InlineKeyboardButton(text='Гитарист-басист', url="https://vk.com/pajiloi_basist")
    peoples.add(guitar)
    jorik = telebot.types.InlineKeyboardButton(text='Гитаристик', url="https://vk.com/novlya.egorov")
    peoples.add(jorik)
    baraban = telebot.types.InlineKeyboardButton(text='Барабанщик', url="https://vk.com/pozhilaya_chokopaika")
    peoples.add(baraban)
    design = telebot.types.InlineKeyboardButton(text='Дизайнер', url="https://vk.com/maybeshutup")
    peoples.add(design)
    krasavchik = telebot.types.InlineKeyboardButton(text='Красавчик', url="https://vk.com/ыьлртм")
    peoples.add(krasavchik)
    photo = telebot.types.InlineKeyboardButton(text='Фотограф', url="https://vk.com/karakaskarakas")
    peoples.add(photo)
    time.sleep(1)
    bot.send_message(message.chat.id, "Личные страницы", reply_markup=peoples)


#Музыка
@bot.message_handler(commands=['music'])
def music(message):
    tg_analytic.statistics(message.chat.id, message.text)
    albums = telebot.types.InlineKeyboardMarkup()
    nz = telebot.types.InlineKeyboardButton(text='Не забывай', callback_data='ne')
    albums.add(nz)
    tts = telebot.types.InlineKeyboardButton(text='Тихо-тише', callback_data='tt')
    albums.add(tts)
    mvn = telebot.types.InlineKeyboardButton(text='Мама, верни', callback_data='mve')
    albums.add(mvn)
    dvs = telebot.types.InlineKeyboardButton(text='Девочка-весна', callback_data='dv')
    albums.add(dvs)
    secret = telebot.types.InlineKeyboardButton(text='СМСка', callback_data='sms')
    albums.add(secret)
    reyv = telebot.types.InlineKeyboardButton(text='С чувствами на рейвах', callback_data='reyvk')
    albums.add(reyv)
    bot.send_message(message.from_user.id, 'Музыка', reply_markup=albums)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "sms":
        sms = open("/home/ubuntu/music/слишком личное вариант 3.mp3", "rb")
        bot.send_audio(call.message.chat.id, sms)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "reyvk":
        r1 = open("/home/ubuntu/music/слишкомлично - Меня убили (С чувствами на рейвах).mp3", "rb")
        bot.send_audio(call.message.chat.id, r1)
        r2 = open("/home/ubuntu/music/слишкомлично - Твоё фото (С чувствами на рейвах).mp3", "rb")
        bot.send_audio(call.message.chat.id, r2)
        r3 = open("/home/ubuntu/music/слишкомлично - Девочка-весна (С чувствами на рейвах).mp3", "rb")
        bot.send_audio(call.message.chat.id, r3)
        r4 = open("/home/ubuntu/music/слишкомлично - Моя зависимость (С чувствами на рейвах).mp3", "rb")
        bot.send_audio(call.message.chat.id, r4)
        r5 = open("/home/ubuntu/music/слишкомлично - Этот мир (С чувствами на рейвах).mp3", "rb")
        bot.send_audio(call.message.chat.id, r5)
        r6 = open("/home/ubuntu/music/слишкомлично - Любви! (С чувствами на рейвах).mp3", "rb")
        bot.send_audio(call.message.chat.id, r6)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "ne":
        ne1 = open("/home/ubuntu/music/слишкомлично - Не забывай (Не забывай).mp3", "rb")
        bot.send_audio(call.message.chat.id, ne1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "tt":
        tt1 = open("/home/ubuntu/music/слишкомлично - Тихо-тише (Тихо-тише).mp3", "rb")
        bot.send_audio(call.message.chat.id, tt1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "mve":
        mv1 = open("/home/ubuntu/music/слишкомлично - Мама, верни (Мама, верни).mp3", "rb")
        bot.send_audio(call.message.chat.id, mv1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "dv":
        dv1 = open("/home/ubuntu/music/слишкомлично - Девочка-весна (Девочка-весна).mp3", "rb")
        bot.send_audio(call.message.chat.id, dv1)
        bot.send_audio(call.message.chat.id, "FILEID")


@bot.message_handler(commands=['by'])
def creators(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Бот был написан Иваном "Linxum" Смехнёвым. Другие проекты: https://github.com/linxum', reply_markup=keyboard1)

@bot.message_handler(commands=['vk'])
def post(message):
    tg_analytic.statistics(message.chat.id, message.text)
    text = ''
    text = vk.send_text(text)
    bot.send_message(message.chat.id, text)
    photo = ''
    photo = vk.send_photo(photo)
    photo = govno.trans(photo)
    jpg = open('out.jpg', 'rb')
    bot.send_photo(message.chat.id, jpg)
    jpg.close()

# кнопки клавиатуры
@bot.message_handler(content_types=['text'])
def keyboards(message):
    if message.text.lower() == 'ссылки':
        links(message)
    elif message.text.lower() == 'о нас':
        about(message)
    elif message.text.lower() == 'наши стикеры':
        tg_analytic.statistics(message.chat.id, message.text)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECHQlgX6iLBeUihKxdn8FRtWd1mqK4twACwAoAAnYpAAFL1yQdpPpDV64eBA')
        bot.send_message(message.chat.id, 'Теперь просто нажми на этот стикер и ты получишь весь пак!', reply_markup=keyboard1)
    elif message.text.lower() == 'наша музыка':
        music(message)
    elif message.text.lower() == 'последняя новость группы':
        post(message)
    elif message.text[:10] == 'статистика' or message.text[:10] == 'Cтатистика':
        st = message.text.split(' ')
        if 'txt' in st or 'тхт' in st:
            tg_analytic.analysis(st,message.chat.id)
            with open('%s.txt' %message.chat.id ,'r',encoding='UTF-8') as file:
                bot.send_document(message.chat.id,file)
                tg_analytic.remove(message.chat.id)
        else:
            messages = tg_analytic.analysis(st,message.chat.id)
            bot.send_message(message.chat.id, messages)

bot.polling()
