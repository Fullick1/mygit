import telebot
from telebot import types
import sqlite3
import requests
import time
import random
from cryptoPay import *
from config import *
import threading
import json


bot = telebot.TeleBot(token=token,parse_mode='HTML')


@bot.message_handler(commands=['start','menu'])
def start(message):
    db = sqlite3.connect('database/base.db')
    sql = db.cursor()  
    sql.execute("""CREATE TABLE IF NOT EXISTS users( 
            id INTEGER,
            cash INTEGER,
            orders INTEGER,
            fact BOOLEAN            
            )""")
    db.commit()
    sql.execute("""CREATE TABLE IF NOT EXISTS subMail( 
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            mail TEXT,
            mailpass TEXT,
            amount INTEGER,
            status TEXT            
            )""")
    db.commit()
    sql.execute("""CREATE TABLE IF NOT EXISTS subito( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT,
                password TEXT,
                amount INTEGER,
                status TEXT            
                )""")
    db.commit()
    data = sql.execute(f'SELECT id FROM users WHERE id = ?',(message.chat.id,)).fetchone()
    if data is None:
        sql.execute(f'INSERT OR IGNORE INTO users VALUES ({message.chat.id}, {0},{0},{False});')
        db.commit()
        
    info_main = sql.execute(f'SELECT * FROM users WHERE id = ?',(message.chat.id,)).fetchall()
    for info in info_main:
        id = info[0]
        cash = info[1]
        order = info[2]
        fact = info[3]
    if fact == True:
        markup_menu2 = types.InlineKeyboardMarkup(row_width=2)
        menu_1 = types.InlineKeyboardButton("🔥Пополнить", callback_data="Deposit")
        menu_2 = types.InlineKeyboardButton("🛒Каталог", callback_data="catalog")
        menu_3 = types.InlineKeyboardButton("❓FAQ❓", callback_data="FAQ")
        markup_menu2.add(menu_2,menu_1,menu_3)
        with open('photo/ph.jpg', 'rb') as f:
            bot.send_photo(message.chat.id, f, caption=f'<b>💲Ваш баланс: </b> <code>{cash}$</code>',reply_markup=markup_menu2)
            
    
    
    
    
    
    
    
    if fact == False:
        markup = types.InlineKeyboardMarkup(row_width=1)
        cb_yes = types.InlineKeyboardButton("👋 Согласиться с правилами", callback_data="cb-yes")
        cb_no  = types.InlineKeyboardButton("❓ Не соглашаюсь с правилами", callback_data="cb-no")
        markup.add(cb_yes,cb_no)
        bot.send_message(message.chat.id,'<b>👁Чтобы продолжить нужно принять пользовательское соглашения</b>'+
                                         '\n\n📜Правила:'+
                                         '\n\n1.Гарантия на товар 8 часов с момента покупки, в редких случая до 24ч.'+
                                         '\n2.Запрещено:'+
                                         '\n-Писать в поддержку с вопросами когда будут аккаунты,а так же спамить более 10 сообщениями.'+
                                         '\n-Писать привет и больше ничего, просто отвлекать, потому что скучно и хочется поговорить о жизни. '+
                                         '\n-Просить лично отписать, а так же спрашивать по предзаказы. '+
                                         '\n\nНа первый раз  игнор, на второй ЧС.'+
                                         '\n\nВОПРОС-ОТВЕТ:'+
                                         '\n1.Можно ли оплатить чеком,бтс?'+
                                         '\n-Да, можно но суммами больше 100р'+
                                         '\n\n2 баланс в боте пополняется автоматически, если возникли проблемы пишите мне '+
                                         '\n\n3.Какой товар подлежит замене?'+
                                         '\n-Только тот, что ПРИ покупке был не рабочим,или заблокирован. Если он отлетел в результате  вашей деятельности, это не гарантийный случай.'+
                                         '\n\n4.Как получить замену?'+
                                         '\n-Отписать в поддержку'+
                                         '\nОтправить данные от аккаунтов, сказать какие именно покупались, указать проблему, ждать замены.'+
                                         '\n\n5.Когда будет пополнение?'+
                                         '\n-Этими вопросами можно лишь только отвлечь, и оттянуть пополнения еще на больший срок, ведь Вы не один, кто пишет.'+
                                         '\n\n6.Почему так долго отвечают?'+
                                         '\n-Отвечают в порядке очереди, значит много сообщений, ждите а не поднимайте новыми свою очередь. Донат или заказы рекламы поставит колокольчик на ваши сообщения и возможно ответят быстрее.  '+
                                         '\n\n7.Не прошла оплата, не выдало товар,что делать?'+
                                         '\n-Писать в поддержку,предоставить скрин оплаты и написать что должны выдать.'+
                                         '\n\n8.Можно ли предзаказ, или сообщить лично когда будет товар?'+
                                         '\n-Нет, уверяю до Вас еще тысячу человек писало с такой же просьбой, смысл бота теряется если всё будет в ручную. Все в равных условиях.'+
                                         '\n\n11.Было пополнение,но не вижу аккаунтов.'+
                                         '\n-Их уже скупили'+
                                         '\n\n12.Как пополнить счёт?'+
                                         '\n-В боте не существует внутреннего баланса,никак.'+
                                         '\n\n1. Внутренний баланс'+
                                         '\n\n1.1 Пополнение внутреннего баланса происходит автоматически через платёжную систему QIWI, @CryptoBot '+
                                         '\n1.2 Перед переводом средств пользователь обязан проверить актуальность реквизитов.'+
                                         '\n1.3 Пользователь согласен, что средства, отправленные с неверным комментарием и/или на старый кошелёк, не будут возвращены/зачислены.'+
                                         '\n1.4 Пользователь согласен, что виртуальный баланс в боте не имеет ценности и может быть обнулён в любой момент.'+
                                         '\n1.5 Пользователь согласен, что виртуальные средства возврату не подлежат.'+
                                         '\n\n2. Товары'+
                                         '\n2.1 т.к  баланс не имеет ценности,  то вы ничего не покупаете.'+
                                         "\n Данный бот является свободной торговой площадкой, администрация магазина не взламывает аккаунты, не добывает со стиллера и скама.Весь ассортимент предоставлен для ознакомления. Информация собрана с офф.сайтов, деятельность бота ни коим образом не связана с кардингом и продажей его производных.АДМИНИСТРАЦИЯ ВПРАВЕ ОТКАЗАТЬ ВАМ В ЛЮБОЙ УСЛУГЕ И ДАТЬ БАН БЕЗ ОБЪЯСНЕНИЯ ПРИЧИН!!!Все платежи с неверным комментарием, номером телефоном и суммой - расцениваются как ПОЖЕРТВОВАНИЕ проекту"+
                                         '\n\n2.3 Оскорбление администрации  может  повлечь за собой блокировку навсегда в боте.'+
                                         '\n2.4 При обращении в поддержку пишем по форме'+
                                         '\nФорма:'+
                                         '\n1.Суть проблемы без воды'+
                                         '\n2.Переслать от бота информацию о покупке (с временем) '+
                                         '\n3.Переслать от бота сам товар'+
                                         '\n4.Видео/Чек/Скриншоты и другие доказательства',reply_markup=markup)







@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    req = call.data.split('_')
    if call.message:
        if call.data == 'cb-yes':
            db = sqlite3.connect('database/base.db' , check_same_thread=False)
            sql = db.cursor()
            sql.execute("UPDATE users SET fact = ? WHERE id = ?", (True, call.from_user.id))
            db.commit()
            markup_menu = types.InlineKeyboardMarkup(row_width=2)
            menu_1 = types.InlineKeyboardButton("💼Личный кабинет", callback_data="main-menu")
            markup_menu.add(menu_1)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>🏆Отлично,переходи в личный кабинет!</b>",reply_markup=markup_menu)
        
        if call.data == 'cb-no':    
            bot.send_message(call.message.chat.id, "<b>‼️Когда захочешь вернуться, напиши /start</b>")
        if call.data == 'main-menu':
            start(call.message)
    
        if call.data == 'Deposit':
            markup_deposit = types.InlineKeyboardMarkup(row_width=1)
            menu_3 = types.InlineKeyboardButton("🤖Crypto-bot", callback_data="Crypto-bot")
            backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
            markup_deposit.add(menu_3,backbutton)
            bot.edit_message_caption(chat_id=call.from_user.id, message_id=call.message.message_id, caption="<b>💳Способ попелнения</b>",reply_markup=markup_deposit)
        if call.data == 'Crypto-bot':
                        msg_pay = bot.edit_message_caption(chat_id=call.from_user.id, message_id=call.message.message_id, caption="<b>✍️Введите сумму которую хотите внести</b>\n\n"+"<b>⚠️Обрати внимание:</b>\n"+"\n<i>💲Оплата принимается только в USDT</i>\n\n'<i>Для отмены операции напишите: </i><code>Отмена</code>'")
                        bot.register_next_step_handler(msg_pay, create_payorder)
        
        if call.data == 'clear-alert':
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=f"<b>🤍Хорошего дня</b>")
        if call.data == 'add-mail':
            
            msg_mail = bot.send_message(call.from_user.id,'<b>🔥Добавляем товар: SUBITO+MAIL</b>\n\n'+
                                                f'<i>Чтобы добавить товар, заполните данные следующим образом:</i>'+
                                                f'\n<code>mail:pass</code>')
            from admin import setMailSub
            bot.register_next_step_handler(msg_mail,setMailSub)

        if call.data == 'add-sub':
            
            msg_mail = bot.send_message(call.from_user.id,'<b>🔥Добавляем товар: SUBITO</b>\n\n'+
                                                f'<i>Чтобы добавить товар, заполните данные следующим образом:</i>'+
                                                f'\n<code>login:pass</code>')
            from admin import setSub
            bot.register_next_step_handler(msg_mail,setSub)

        if call.data == 'FAQ':
             support = types.InlineKeyboardMarkup(row_width=1)
             menu_3 = types.InlineKeyboardButton("🩻Поддержка", url="https://t.me/subitosupp")
             backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
             support.add(menu_3,backbutton)
             bot.edit_message_caption(chat_id=call.from_user.id, message_id=call.message.message_id, caption='<b>Чтобы получить помощь свяжитесь с поддержкой!</b>',reply_markup=support)
        
        
        
        if call.data == 'dell-pos':
             markup_catalog = types.InlineKeyboardMarkup(row_width=1)
             but_1 = types.InlineKeyboardButton("📧SUBITO + MAIL", callback_data="choiceDell_mail")
             but_2 = types.InlineKeyboardButton("🔗SUBITO", callback_data='choiceDell_subito')
             backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
             markup_catalog.add(but_1, but_2,backbutton)
             bot.send_message(call.from_user.id,'<b>Какой сервис?</b>',reply_markup=markup_catalog)


        if req[0] == 'choiceDell':
                product = req[1]
                
                
                if product == 'mail':
                    markup_dell = types.InlineKeyboardMarkup(row_width=1)
                    but_1 = types.InlineKeyboardButton("♨️Удалить MAIL", callback_data="deleteID_subMail")
                    backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
                    markup_dell.add(but_1,backbutton)
                    db = sqlite3.connect('database/base.db' , check_same_thread=False)
                    sql = db.cursor()
                    info = sql.execute(f'SELECT * FROM subMail').fetchall()
                    text = ''
                    db.close()
                    for i in info:
                         text = text + str(i)
                    bot.send_message(call.from_user.id,text,reply_markup=markup_dell)      
                if product == 'subito':
                    try:
                        markup_dells = types.InlineKeyboardMarkup(row_width=1)
                        but_1 = types.InlineKeyboardButton("♨️Удалить SUBITO", callback_data="deleteID_subito")
                        backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
                        markup_dells.add(but_1,backbutton)
                        db = sqlite3.connect('database/base.db' , check_same_thread=False)
                        sql = db.cursor()
                        info = sql.execute(f'SELECT * FROM subito').fetchall()
                        text = ''
                        db.close()
                        for i in info:
                            text = text + str(i)
                        bot.send_message(call.from_user.id,text,reply_markup=markup_dells)
                    except:
                         bot.send_message(call.from_user.id,'Нет позиций в этой категории')
        if req[0] == 'deleteID':
            choice = req[1] 
            msg = bot.send_message(call.from_user.id,text=f"<b>Введите id позиции которую хотите удалить</b>")
            from admin import deleteChoice
            bot.register_next_step_handler(msg,deleteChoice,choice)
        
        
        if req[0] == 'choice':
            try:
                db = sqlite3.connect('database/base.db' , check_same_thread=False)
                sql = db.cursor()
                
                
                product = req[1]
                if product == 'mail':
                    cash_db_wallet = sql.execute(f'SELECT cash FROM users WHERE id = {call.from_user.id}').fetchone()[0]
                    with open('amount/amount.json', 'r') as src:
                        cash = src.read()
                        amount = json.loads(cash)
                    if cash_db_wallet >= amount['SUBITO-MAIL']:
                        end_db = int(cash_db_wallet) - int(amount['SUBITO-MAIL'])
                        info = sql.execute(f'SELECT * FROM subMail WHERE status = "Свободен"').fetchone()
                        sql.execute(f'UPDATE subMail SET status = "Используется" WHERE id = {info[0]}')
                        sql.execute(f'UPDATE users SET cash = {end_db} WHERE id = {call.from_user.id}')
                        db.commit()
                        bot.send_message(call.from_user.id,f'<b>🛍Спасибо за покупку!</b>\n'+
                                        f'\n🔒<b>Данные для входа:</b>\n📧MAIL: <code>{info[1]}</code>:<code>{info[2]}</code>'+
                                        f'\n\n<b>🤍Хорошего дня</b>')
                    if cash_db_wallet <= amount['SUBITO-MAIL']:
                        bot.send_message(call.from_user.id,'<b>🚫На вашем балансе недостаточно средств</b>')
            
                if product == 'subito':
                    cash_db_wallet = sql.execute(f'SELECT cash FROM users WHERE id = {call.from_user.id}').fetchone()[0]
                    with open('amount/amount.json', 'r') as src:
                        cash = src.read()
                        amount = json.loads(cash)
                    if cash_db_wallet >= amount['SUBITO']:
                        end_db = int(cash_db_wallet) - int(amount['SUBITO'])
                        info = sql.execute(f'SELECT * FROM subito WHERE status = "Свободен"').fetchone()
                        sql.execute(f'UPDATE subMail SET status = "Используется" WHERE id = {info[0]}')
                        sql.execute(f'UPDATE users SET cash = {end_db} WHERE id = {call.from_user.id}')
                        db.commit()
                        bot.send_message(call.from_user.id,f'<b>🛍Спасибо за покупку!</b>\n'+
                                        f'\n🔒<b>Данные для входа:</b>\n🇮🇹SUBITO: <code>{info[1]}</code>:<code>{info[2]}</code>'+
                                        f'\n\n<b>🤍Хорошего дня</b>')
                    if cash_db_wallet <= amount['SUBITO']:
                        bot.send_message(call.from_user.id,'<b>🚫На вашем балансе недостаточно средств</b>')
            except:
                 bot.send_message(call.from_user.id,'<b>⚙️Товар который вы хотите преобрести сейчас недоступен</b>')
        
        
        
        
        
        
        
        if call.data == 'catalog':
            db = sqlite3.connect('database/base.db' , check_same_thread=False)
            sql = db.cursor()
            mail = sql.execute(f'SELECT COUNT(*) FROM subMail WHERE status = "Свободен"').fetchone()[0]
            subito = sql.execute(f'SELECT COUNT(*) FROM subito WHERE status = "Свободен"').fetchone()[0]
            db.close()
            with open('amount/amount.json', 'r') as src:
                cash = src.read()
                amount = json.loads(cash)
            markup_catalog = types.InlineKeyboardMarkup(row_width=1)
            but_1 = types.InlineKeyboardButton(f"📧SUBITO + MAIL [{amount['SUBITO-MAIL']}$]", callback_data="choice_mail")
            but_2 = types.InlineKeyboardButton(f"🔗SUBITO [{amount['SUBITO']}$]", callback_data='choice_subito')
            backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
            markup_catalog.add(but_1, but_2,backbutton)
            bot.edit_message_caption(chat_id=call.from_user.id, message_id=call.message.message_id, caption='<b>🔸Выберите тип товара который хотите преобрести!</b>'+
                                                                                                            f'\n\n📩SUBITO + MAIL: {mail} шт.'+
                                                                                                            f'\n🇮🇹 SUBITO: {subito} шт.',reply_markup=markup_catalog)

            
        if call.data == 'set-amount':
            with open('amount/amount.json', 'r') as src:
                cash = src.read()
                amount = json.loads(cash)
            markup_setamount = types.InlineKeyboardMarkup(row_width=1)
            add_but1 = types.InlineKeyboardButton("➕SUBITO+MAIL", callback_data="new-amount_SUBITO-MAIL")
            add_but2 = types.InlineKeyboardButton("➕SUBITO", callback_data='new_amount_SUBITO')
            backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
            markup_setamount.add(add_but1,add_but2,backbutton)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=f"<b>💢Цены сейчас:\n📨SUBITO+MAIL: {amount['SUBITO-MAIL']} $\n🛍SUBITO: {amount['SUBITO']} $</b>",reply_markup=markup_setamount)    


        
        
        
        
        
        
        if req[0] == 'new-amount':
                service = req[1]
                set_new_sum = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=f"<b>✍️Введите сумму которую хотите установить</b>\n\nЕсли хотите отменить изменение, напишите <code>Отмена</code>")
                bot.register_next_step_handler(set_new_sum,newSum,service)
    
    


def newSum(message,service):
    if message.text == 'Отмена':
         bot.send_message(message.chat.id,'Вы отменили изменение!')
    else:
        set_new_sum = float(message.text)
        # Открыть файл и загрузить его в словарь
        with open('amount/amount.json', 'r') as f:
                    data = json.load(f)

                # Изменить значение
        data[service] = set_new_sum

                # Записать измененный словарь обратно в файл
        with open('amount/amount.json', 'w') as f:
                    json.dump(data, f)
        bot.send_message(message.chat.id,f'♻️<b>Вы успешно изменили цену за товар:</b> <code>[{service}]</code>')