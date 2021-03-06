import random
import requests
import telebot

# main variables
bot = telebot.TeleBot('1106845063:AAFUWishJZFfzOL9YWElj6GrXjfeLiWxUWs')


@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Привет, я пишу речи для ваших выступлений! Для начала напишите "!Речь"')
    bot.polling(none_stop=True)


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "привет":
        bot.send_message(chat_id, 'Привет, я бот - писатель политической речи.')
    elif text == "как дела?":
        bot.send_message(chat_id, 'Хорошо, а у тебя?')
    else:
        bot.send_message(chat_id, 'Простите, я вас не понял :(')


@bot.message_handler(commands=['!Речь', 'Speech'])
def start_handler(message):
    bot.send_message(message.chat.id, 'На сколько предложений вы хотите речь? '
                                      'Напишите число от 1 до 10.')
    text = message.text.lower()
    chat_id = message.chat.id
    # Дальше у нас список вариантов для рандомайзера
    first_table = ['Товарищи!',
                   'С другой стороны',
                   'Равным образом',
                   'Не следует, однако, забывать, что',
                   'Таким образом',
                   'Повседневная практика показывает, что',
                   'Значимость этих проблем настолько очевидна, что',
                   'Разнообразный и богатый опыт,',
                   'Задача организации, в особенности же',
                   'Идейные соображения высшего порядка,']
    second_table = ['реализация намеченных планов',
                    'рамки и место обучения кадров',
                    'постоянный количественный рост и сфера нашей активности',
                    'сложившаяся структура организации',
                    'новая модель организационной деятельности',
                    'дальнейшее развитие различных форм деятельности',
                    'укрепления и развития структуры',
                    'консультация с широким активом',
                    'начало повседневной работы по формированию позиции',
                    'постоянное информационно-пропагандистское обеспечение нашей деятельности']
    third_table = ['играет важную роль в формировании',
                   'требуют от нас анализа',
                   'требуют определения и уточнения',
                   'способствуют подготовке и реализации',
                   'обеспечивает широкому кругу специалистов участие в формировании',
                   'позволяет выполнять важные задания по разработке',
                   'в значительной ступени обуславливает создание',
                   'позволяет оценить значение',
                   'представляет собой интересный эксперемент проверки',
                   'влечет за собой процесс внедрения и модерницации']
    fourth_table = ['существующих финансовых и административных условий.',
                    'дальнейших направлений развития.',
                    'системы массового участия.',
                    'позиций, занимаемых участниками в отношении поставленных задач.',
                    'новых предложений.',
                    'направлений прогрессивного развития.',
                    'системы обучения кадров, соответствующей насущным потребностям.',
                    'соответствующих условий активизации.', 'модели развития.', 'форм воздействия.']
    s = 0
    while s < int(message):
        bot.send_message(chat_id,
                         f'{first_table(random)} {second_table(random)} {third_table(random)} {fourth_table(random)}')
    s = s + 1
