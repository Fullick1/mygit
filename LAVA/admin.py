from main import *
import telebot
from telebot import types
import sqlite3


@bot.message_handler(commands=['alert'])
def alert(message):
        # Получаем текст сообщения после команды /alert
        text = message.text.split(' ', 1)[1]
        # Проверяем, есть ли у сообщения фотография
        if message.photo:
            # Получаем объект file_id фотографии
            photo_id = message.photo[-1].file_id
            # Запускаем отправку фотографии и текста в отдельном потоке
            thread = threading.Thread(target=send_alert_to_all_users, args=(message,text, photo_id))
            thread.start()
        else:
            # Запускаем отправку текста в отдельном потоке
            thread = threading.Thread(target=send_alert_to_all_users, args=(message,text, None))
            thread.start()

def send_alert_to_all_users(message,text, photo_id):
    # Получаем список всех пользователей из базы данных
    db = sqlite3.connect('database/base.db')
    sql = db.cursor()
    all_user_id = sql.execute('SELECT id FROM users').fetchall()
    # Создаем клавиатуру с кнопкой "Убрать"
    edit_key = types.InlineKeyboardMarkup(row_width=2)
    button = types.InlineKeyboardButton("✖️Убрать", callback_data="clear-alert")
    edit_key.add(button)
    # Отправляем фотографию и текст, если есть, каждому пользователю из списка
    no_sms = 0
    for id_user in all_user_id:
        try:
            if photo_id:
                bot.send_photo(id_user[0], photo_id, caption=f'<b>{text}</b>', reply_markup=edit_key, parse_mode='HTML')
            else:
                bot.send_message(id_user[0], f'<b>{text}</b>', reply_markup=edit_key, parse_mode='HTML')
        except:
            no_sms += 1
            continue
    bot.send_message(message.chat.id,str(no_sms) +' Не получило смс')


@bot.message_handler(commands=['admin'])
def admin(message):
    db = sqlite3.connect('database/base.db' , check_same_thread=False)
    sql = db.cursor()
    markup_deposit = types.InlineKeyboardMarkup(row_width=2)
    add_but1 = types.InlineKeyboardButton("➕SUBITO+MAIL", callback_data="add-mail")
    add_but2 = types.InlineKeyboardButton("➕SUBITO", callback_data='add-sub')
    newcash = types.InlineKeyboardButton("♻️Установить цены", callback_data="set-amount")
    dell = types.InlineKeyboardButton("🗑Удалить позицию", callback_data="dell-pos")
    backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
    markup_deposit.add(add_but1, add_but2,newcash,dell,backbutton)
    
    
    users_all = sql.execute(f'SELECT COUNT(*) FROM users').fetchone()[0]
    all_sum = sql.execute('SELECT SUM(cash) FROM users').fetchone()[0]
    bot.send_message(message.chat.id, '<b>🌩АДМИН ПАНЕЛЬ🌩</b>\n'+
                                    f'\n<b>🙉 Юзеров в боте: {users_all}</b>'+
                                    #f'\n<b>⚡️Успешных сделок за все веремя: ?</b>'+
                                    f'\n<b>👾Внесенных средств: {all_sum} $</b>',reply_markup=markup_deposit)


def setMailSub(message):
    try:
        db = sqlite3.connect('database/base.db' , check_same_thread=False)
        sql = db.cursor()
        msg_mail = message.text
        set_db = msg_mail.split(':')
        with open('amount/amount.json', 'r') as src:
            cash = src.read()
            amount = json.loads(cash)
        sql.execute('INSERT OR IGNORE INTO subMail (mail,mailpass,amount,status) VALUES ( ?, ?, ?, ?)', (set_db[0],set_db[1],amount['SUBITO-MAIL'],'Свободен'))
        db.commit()
        db.close()
        msg = bot.send_message(message.chat.id,f'<b>✅Пози́ция успешно размещена</b>\n\n<b>Для того чтобы добавить еще одну позицию отправьте ее вида:</b> <code>mail:pass</code>\nЕсли хотите отменить добавление, напишите "<code>Отмена</code>"')
        bot.register_next_step_handler(msg,newProdMail)
    except:
        bot.send_message(message.chat.id,'Где-то допущена ошибка!')

def newProdMail(message):
    msg = message.text
    if msg == 'Отмена':
        bot.send_message(message.chat.id,'Вы отменили добавление товара')
        start(message)
    else:
        try:
            db = sqlite3.connect('database/base.db' , check_same_thread=False)
            sql = db.cursor()
            msg_mail = message.text
            set_db = msg_mail.split(':')
            with open('amount/amount.json', 'r') as src:
                cash = src.read()
                amount = json.loads(cash)
            sql.execute('INSERT OR IGNORE INTO subMail (mail,mailpass,amount,status) VALUES ( ?, ?, ?, ?)', (set_db[0],set_db[1],amount['SUBITO-MAIL'],'Свободен'))
            db.commit()
            db.close()
            msg = bot.send_message(message.chat.id,f'<b>✅Пози́ция успешно размещена</b>\n\n<b>Для того чтобы добавить еще одну позицию отправьте ее вида:</b> <code>mail:pass</code>\nЕсли хотите отменить добавление, напишите "<code>Отмена</code>"')
            bot.register_next_step_handler(msg,newProdMail)
        except:
            bot.send_message(message.chat.id,'Где-то допущена ошибка!')





def setSub(message):
    try:
        db = sqlite3.connect('database/base.db' , check_same_thread=False)
        sql = db.cursor()
        msg_mail = message.text
        set_db = msg_mail.split(':')
        with open('amount/amount.json', 'r') as src:
            cash = src.read()
            amount = json.loads(cash)
        sql.execute('INSERT OR IGNORE INTO subito (login,password,amount,status) VALUES (?, ?, ?, ?)', (set_db[0],set_db[1],amount['SUBITO'],'Свободен'))
        db.commit()
        db.close()
        msg = bot.send_message(message.chat.id,f'<b>✅Пози́ция успешно размещена</b>\n\n<b>Для того чтобы добавить еще одну позицию отправьте ее вида:</b> <code>login:pass</code>\nЕсли хотите отменить добавление, напишите "<code>Отмена</code>"')
        bot.register_next_step_handler(msg,newProdSub)
    except:
        bot.send_message(message.chat.id,'Где-то допущена ошибка!')


def newProdSub(message):
    msg = message.text
    if msg == 'Отмена':
        bot.send_message(message.chat.id,'Вы отменили добавление товара')
        start(message)
    else:
        try:
            db = sqlite3.connect('database/base.db' , check_same_thread=False)
            sql = db.cursor()
            msg_mail = message.text
            set_db = msg_mail.split(':')
            with open('amount/amount.json', 'r') as src:
                cash = src.read()
                amount = json.loads(cash)
            sql.execute('INSERT OR IGNORE INTO subito (login,password,amount,status) VALUES (?, ?, ?, ?)', (set_db[0],set_db[1],amount['SUBITO'],'Свободен'))
            db.commit()
            db.close()
            msg = bot.send_message(message.chat.id,f'<b>✅Пози́ция успешно размещена</b>\n\n<b>Для того чтобы добавить еще одну позицию отправьте ее вида:</b> <code>login:pass</code>\nЕсли хотите отменить добавление, напишите "<code>Отмена</code>"')
            bot.register_next_step_handler(msg,newProdSub)
        except:
            bot.send_message(message.chat.id,'Где-то допущена ошибка!')





def deleteChoice(message,choice):
    try:
        msg = message.text
        db = sqlite3.connect('database/base.db' , check_same_thread=False)
        sql = db.cursor()
        sql.execute(f'DELETE FROM {choice} WHERE id = {msg}')
        db.commit()
        bot.send_message(message.chat.id,'🗑Позиция успешно удалена')
    except:
        bot.send_message(message.chat.id,'Ошибка')
