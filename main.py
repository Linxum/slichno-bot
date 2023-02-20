import telebot
import time
import vk
import govno
import tg_analytic
from telebot import types

# Токен и клавиатура
bot = telebot.TeleBot('<YOUR TOKEN>')
keyboard1 = types.ReplyKeyboardMarkup(True, True)
keyboard1.add('Наши стикеры', 'Ссылки', 'О нас', 'Наша музыка', 'Последняя новость группы')

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
    bot.send_message(message.chat.id, 'Привет, друг! Мы группа из Губкина. Играем рок в своё удовольствие. Можешь ознакомиться с нашим творчеством;) По кнопке найдёшь все ссылки. Yда4и¡')

# Ссылки
@bot.message_handler(commands=['links'])
def links(message):
    tg_analytic.statistics(message.chat.id, message.text)
    lin = types.InlineKeyboardMarkup()
    vk = types.InlineKeyboardButton(text='ВК', callback_data='vk0')
    society = types.InlineKeyboardButton(text='Другие социальные сети', callback_data='society0')
    link = types.InlineKeyboardButton(text='Другие сервисы', callback_data='link0')
    peoples = types.InlineKeyboardButton(text='Личные страницы', callback_data='peoples0')

    lin.add(vk)
    lin.add(society)
    lin.add(link)
    lin.add(peoples)
    bot.send_message(message.chat.id, 'Выбирай, что тебе надо!', reply_markup=lin)

#Музыка
@bot.message_handler(commands=['music'])
def music(message):
    tg_analytic.statistics(message.chat.id, message.text)
    albums = types.InlineKeyboardMarkup()
    nz = types.InlineKeyboardButton(text='Не забывай', callback_data='ne')
    albums.add(nz)
    tts = types.InlineKeyboardButton(text='Тихо-тише', callback_data='tt')
    albums.add(tts)
    mvn = types.InlineKeyboardButton(text='Мама, верни', callback_data='mve')
    albums.add(mvn)
    dvs = types.InlineKeyboardButton(text='Девочка-весна', callback_data='dv')
    albums.add(dvs)
    reyv = types.InlineKeyboardButton(text='С чувствами на рейвах', callback_data='reyvk')
    albums.add(reyv)
    bot.send_message(message.from_user.id, 'Музыка', reply_markup=albums)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "reyvk":
        tg_analytic.statistics(call.message.chat.id, 'С чувствами на рейвах')
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
        tg_analytic.statistics(call.message.chat.id, 'Не забывай')
        ne1 = open("/home/ubuntu/music/слишкомлично - Не забывай (Не забывай).mp3", "rb")
        bot.send_audio(call.message.chat.id, ne1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "tt":
        tg_analytic.statistics(call.message.chat.id, 'Тихо-тише')
        tt1 = open("/home/ubuntu/music/слишкомлично - Тихо-тише (Тихо-тише).mp3", "rb")
        bot.send_audio(call.message.chat.id, tt1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "mve":
        tg_analytic.statistics(call.message.chat.id, 'Мама, верни')
        mv1 = open("/home/ubuntu/music/слишкомлично - Мама, верни (Мама, верни).mp3", "rb")
        bot.send_audio(call.message.chat.id, mv1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == "dv":
        tg_analytic.statistics(call.message.chat.id, 'Девочка-весна')
        dv1 = open("/home/ubuntu/music/слишкомлично - Девочка-весна (Девочка-весна).mp3", "rb")
        bot.send_audio(call.message.chat.id, dv1)
        bot.send_audio(call.message.chat.id, "FILEID")
    elif call.data == 'vk0':
        tg_analytic.statistics(call.message.chat.id, 'Ссылки на группу ВК')
        vk1 = types.InlineKeyboardMarkup()
        group_vk = types.InlineKeyboardButton(text='Группа в ВК', url='https://vk.com/clishkomlichnoe')
        vk1.add(group_vk)
        music_vk = types.InlineKeyboardButton(text='Музыка в ВК', url='https://vk.com/artist/slishkomlichno')
        vk1.add(music_vk)
        bot.send_message(call.message.chat.id, "ВК", reply_markup=vk1)
    elif call.data == 'society0':
        tg_analytic.statistics(call.message.chat.id, 'Ссылки на соц. сети')
        society1 = types.InlineKeyboardMarkup()
        insta = types.InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/_slishkomlichno/')
        society1.add(insta)
        bot.send_message(call.message.chat.id, 'Другие социальные сети', reply_markup=society1)
    elif call.data == 'link0':
        tg_analytic.statistics(call.message.chat.id, 'Ссылки на сервисы')
        link1 = types.InlineKeyboardMarkup()
        spotify = types.InlineKeyboardButton(text='Spotify', url='https://open.spotify.com/artist/2XAkDxAqUKgoR6rxtIl5as?si=a3382b4a434f4609')
        link1.add(spotify)
        yandex = types.InlineKeyboardButton(text='Яндекс.Музыка', url='https://music.yandex.ru/artist/9584394')
        link1.add(yandex)
        bot.send_message(call.message.chat.id, "Другие сервисы", reply_markup=link1)
    elif call.data == 'peoples0':
        peoples1 = types.InlineKeyboardMarkup()
        vkp = types.InlineKeyboardButton(text='Ссылки на ВК', callback_data='vkp0')
        peoples1.add(vkp)
        instp = types.InlineKeyboardButton(text='Ссылки на Instagram', callback_data='instp0')
        peoples1.add(instp)
        bot.send_message(call.message.chat.id, "Выбирай соц.сеть!", reply_markup=peoples1)
    elif call.data == 'vkp0':
        tg_analytic.statistics(call.message.chat.id, 'Ссылки на людей ВК')
        vkp1 = types.InlineKeyboardMarkup()
        morozov = types.InlineKeyboardButton(text='Солист', url="https://vk.com/idbynelka")
        vkp1.add(morozov)
        guitar = types.InlineKeyboardButton(text='Гитарист-басист', url="https://vk.com/pajiloi_basist")
        vkp1.add(guitar)
        jorik = types.InlineKeyboardButton(text='Гитаристик', url="https://vk.com/novlya.egorov")
        vkp1.add(jorik)
        baraban = types.InlineKeyboardButton(text='Барабанщик', url="https://vk.com/pozhilaya_chokopaika")
        vkp1.add(baraban)
        design = types.InlineKeyboardButton(text='Дизайнер', url="https://vk.com/maybeshutup")
        vkp1.add(design)
        krasavchik = types.InlineKeyboardButton(text='Специлист по креативу', url="https://vk.com/smkhnv")
        vkp1.add(krasavchik)
        photo = types.InlineKeyboardButton(text='Фотограф', url="https://vk.com/karakaskarakas")
        vkp1.add(photo)
        bot.send_message(call.message.chat.id, "Личные страницы ВК", reply_markup=vkp1)
    elif call.data == 'instp0':
        tg_analytic.statistics(call.message.chat.id, 'Ссылки на людей Instagram')
        instp1 = types.InlineKeyboardMarkup()
        morozov = types.InlineKeyboardButton(text='Солист', url="https://instagram.com/a.morozovik")
        instp1.add(morozov)
        guitar = types.InlineKeyboardButton(text='Гитарист-басист', url="https://instagram.com/pajilay_basiska")
        instp1.row(guitar)
        jorik = types.InlineKeyboardButton(text='Гитаристик', url="https://instagram.com/sick.chav")
        instp1.row(jorik)
        baraban = types.InlineKeyboardButton(text='Барабанщик', url="https://instagram.com/artea_mus")
        instp1.add(baraban)
        design = types.InlineKeyboardButton(text='Дизайнер', url="https://instagram.com/maybeshutup")
        instp1.add(design)
        krasavchik = types.InlineKeyboardButton(text='Специалист по креативу', url="https://instagram.com/_smkchnv_")
        instp1.add(krasavchik)
        photo = types.InlineKeyboardButton(text='Фотограф', url="https://instagram.com/arseny__v")
        instp1.add(photo)
        bot.send_message(call.message.chat.id, "Личные страницы Instagram", reply_markup=instp1)

@bot.message_handler(commands=['гамак'])
def sms(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Ты просто умница!🤗 Ты смог найти пасхалку. Вот тебе за это невыпущенная песня "Смска". Наслаждайся! Мои друзья сказали мне, что она очень классная! 😏 Только тссссс🤫 Никому не рассказывай об этой песне и о том, как её найти. Особенно солисту группы. Он её ненавидит😂 Не знаю, почему. Надеюсь, ты умеешь хранить секреты и я могу тебе доверить эту тайну?')
    sms = open("/home/ubuntu/music/sms.mp3", "rb")
    bot.send_audio(message.chat.id, sms)
    bot.send_audio(message.chat.id, "FILEID")

#Пасхалка#1
@bot.message_handler(commands=['sugarcrash'])
def sugarcrash(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Поздравляю тебя! 🎉 Ты отыскал нашу пасхалку. За это тебя ждёт вознаграждание: эксклюзивный стикер с изображением солиста группы. Ты просто молодец! Мой респект тебе за догадливость🤘')
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAECJAZgaFmtJe1vwP9WqHd7Z09D82pljwAC5AwAAuR_QUtcRJod3hHt_x4E')

#Пасхалка#2
@bot.message_handler(commands=['by'])
def creators(message):
    tg_analytic.statistics(message.chat.id, message.text)
    bot.send_message(message.chat.id, 'Бот был написан Иваном "Linxum" Смехнёвым. Другие проекты: https://github.com/linxum', reply_markup=keyboard1)

#Последняя_новость
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
