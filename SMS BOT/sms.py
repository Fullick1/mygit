import telebot
import sqlite3
from telebot import types
import time
import json
import requests
import os
import pay_crypto 


bot = telebot.TeleBot("5448420684:AAGNPnBCBPvoIEwvOoIx7cO1BJRxO-O9Sww", parse_mode="HTML")


class MeDb:
    def __init__(self, id):
        self.id = id
    
    def getMeDB(self,id):
        db = sqlite3.connect('base.db')
        cursor = db.cursor()
        select_me = cursor.execute("SELECT * FROM users WHERE id = ?",(id,)).fetchall()
        return select_me 
    def getMeBalance(self,id):
        db = sqlite3.connect('base.db')
        cursor = db.cursor()
        balance_me = cursor.execute("SELECT balance FROM users WHERE id = ?",(id,)).fetchone()[0]
        return balance_me 
    def getMeOrders(self,id):
        db = sqlite3.connect('base.db')
        cursor = db.cursor()
        orders_me = cursor.execute("SELECT orders FROM users WHERE id = ?",(id,)).fetchone()[0]
        return orders_me
    def UpdateBalance(self,id,balance):
        db = sqlite3.connect('base.db')
        cursor = db.cursor()
        updateBalances = cursor.execute("UPDATE users SET balance = ? WHERE id = ?",(balance,id,))
        db.commit()
        return updateBalances 
    def updateorders(self,id,endOrder):
        db = sqlite3.connect('base.db')
        cursor = db.cursor()
        updateOrder = cursor.execute("UPDATE users SET orders = ? WHERE id = ?",(endOrder,id,))
        db.commit()
        return updateOrder

@bot.message_handler(commands=['start'])
def start(message):
    db = sqlite3.connect('base.db')
    cursor = db.cursor()  
    cursor.execute("""CREATE TABLE IF NOT EXISTS fact( 
            id INTEGER,
            fact INTEGER
            )""")
    db.commit()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users( 
            id INTEGER,
            balance INTEGER,
            orders INTEGER

            )""")
    db.commit()
    id = message.from_user.id
    id_select = cursor.execute("SELECT id FROM users WHERE id = ?", (id, )).fetchone()
    if id_select is None:
        cursor.execute(f'INSERT OR IGNORE INTO users VALUES ({id}, {0},{0});')
        db.commit()
    check = cursor.execute("SELECT id FROM fact WHERE id = ?", (id, )).fetchone()
    print(check)
    if check is None:
        cursor.execute(f'INSERT OR IGNORE INTO fact VALUES ({id}, 0);')
        db.commit()
    fact = cursor.execute("SELECT fact FROM fact WHERE id = ?", (id, )).fetchone()[0]
    if fact == 0:
        markup = types.InlineKeyboardMarkup(row_width=1)
        cb_yes = types.InlineKeyboardButton("👋 Согласиться с правилами", callback_data="cb-yes")
        cb_no  = types.InlineKeyboardButton("❓ Не соглашаюсь с правилами", callback_data="cb-no")
        markup.add(cb_yes,cb_no)
        bot.send_message(message.chat.id, text=f"Привет, {message.chat.first_name}\nСогласитесь с правилами бота для продолжения!",reply_markup=markup)
    if fact == 1:
        markup_block = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        menu = types.KeyboardButton("Главное меню")
        markup_block.add(menu)
        markup_menu = types.InlineKeyboardMarkup(row_width=2)
        menu_1 = types.InlineKeyboardButton("👋 Пополнение", callback_data="Deposit")
        menu_2  = types.InlineKeyboardButton("❓ ПОМОЩЬ", callback_data="Help")
        menu_3  = types.InlineKeyboardButton("📞 Купить номер", callback_data="Buy-number")
        markup_menu.add(menu_1 ,menu_3 ,menu_2)


        get_db = MeDb(message.chat.id)
        my_info = get_db.getMeDB(message.chat.id)
        for main in my_info:
            cash = main[1]
            order = main[2]

        bot.send_sticker(message.chat.id,'CAACAgEAAxkBAAEIq6pkQorrnsjMja-GSBha7cn8UIc1PgACiQMAAojcyEeb7pyszvxvJS8E',reply_markup=markup_block)
        bot.send_message(message.chat.id,"<b>💼Твой кабинет</b>\n"+
                                         f"\n<b>🤑Баланс: </b>"+'%.2f' % cash + '$' +
                                         f"\n<b>🔺Успешных покупок: {order} шт.</b>"
                         
                         
                         , reply_markup=markup_menu)

        

# Меню
@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    req = call.data.split('_')
    if call.message:
        if call.data == 'cb-yes':
            db = sqlite3.connect('base.db' , check_same_thread=False)
            cursor = db.cursor()
            cursor.execute("UPDATE fact SET fact = ? WHERE id = ?", (1, call.from_user.id))
            db.commit()
            markup_menu = types.InlineKeyboardMarkup(row_width=2)
            menu_1 = types.InlineKeyboardButton("💼Личный кабинет", callback_data="main-menu")
            markup_menu.add(menu_1)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>🏆Отлично,переходи в личный кабинет!</b>",reply_markup=markup_menu)
        
        if call.data == 'cb-no':    
            bot.send_message(call.message.chat.id, "Ты кринж")
        
        if call.data == 'Deposit':
            markup_deposit = types.InlineKeyboardMarkup(row_width=1)
            menu_3 = types.InlineKeyboardButton("🤖Crypto-bot", callback_data="Crypto-bot")
            backbutton = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
            markup_deposit.add(menu_3, backbutton)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>💳Способ попелнения</b>",reply_markup=markup_deposit)
        if call.data == 'Crypto-bot':
                        msg_pay = bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>✍️Введите сумму которую хотите внести</b>\n\n"+"<b>⚠️Обрати внимание:</b>\n"+"\n<i>💲Оплата принимается только в USDT</i>\n\n'<i>Для отмены операции напишите: </i><code>Отмена</code>'")
                        bot.register_next_step_handler(msg_pay, pay_crypto.create_payorder)
        
        if call.data == 'Help':
            markup_help = types.InlineKeyboardMarkup(row_width=2)
            url_button = types.InlineKeyboardButton("👨🏿‍💻Менежер", url="https://t.me/Fruts_dev")
            backbutton2 = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
            markup_help.add(url_button, backbutton2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>🎯В случае если вы столкнулись с какими либо проблемами, пишите нам!</b>",reply_markup=markup_help)

        if call.data == 'main-menu':
            get_db = MeDb(call.message.chat.id)
            my_info = get_db.getMeDB(call.message.chat.id)
            for main in my_info:
                cash = main[1]
                order = main[2]



            markup_menu2 = types.InlineKeyboardMarkup(row_width=2)
            menu_1 = types.InlineKeyboardButton("👋 Пополнение", callback_data="Deposit")
            menu_2  = types.InlineKeyboardButton("❓ ПОМОЩЬ", callback_data="Help")
            menu_3  = types.InlineKeyboardButton("📞 Купить номер", callback_data="Buy-number")
            markup_menu2.add(menu_1, menu_3 ,menu_2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>💼Твой кабинет</b>\n"+
                                         f"\n<b>🤑Баланс: </b>"+'%.2f' % cash + '$' +
                                         f"\n<b>🔺Успешных покупок: {order} шт.</b>",reply_markup=markup_menu2)
        

        if call.data == 'Qiwi':
            markup_block = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
            menu = types.KeyboardButton("Отмена")
            markup_block.add(menu)
            msg = bot.send_message(call.message.chat.id,'<b>✍️Введите сумму депозита</b>\n\n<i>❕Напишите</i> <code>Отмена</code> <i>чтобы отменить транзакцию</i>',reply_markup=markup_block)
            bot.register_next_step_handler(msg, Qiwi_nomer)
            
        if call.data == 'Buy-number':
            markup_number = types.InlineKeyboardMarkup(row_width=2)
            menu_1 = types.InlineKeyboardButton("🇫🇷 Франция", callback_data="countr_33")
            menu_2  = types.InlineKeyboardButton("🇪🇸 Испания", callback_data="countr_34")
            menu_3  = types.InlineKeyboardButton("🇩🇪 Германия", callback_data="countr_49")
            menu_4  = types.InlineKeyboardButton("🇨🇿 Чехия", callback_data="countr_420")
            menu_5  = types.InlineKeyboardButton("🇨🇾 Кипр", callback_data="countr_357")
            menu_6  = types.InlineKeyboardButton("🇬🇧 Британия", callback_data="countr_44")
            menu_7  = types.InlineKeyboardButton("🇩🇰 Дания", callback_data="countr_45")
            menu_8  = types.InlineKeyboardButton("🇮🇹 Италия", callback_data="countr_39")
            menu_9  = types.InlineKeyboardButton("🇵🇹 Португалия", callback_data="countr_351")
            backbutton2 = types.InlineKeyboardButton("👈Назад", callback_data='main-menu')
            markup_number.add(menu_1,menu_2,menu_3,menu_4,menu_5,menu_6,menu_7,menu_8,menu_9,backbutton2)
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text="<b>☔️Выбери страну для которой хотите купить номер</b>", reply_markup=markup_number)
        if req[0] == "countr":
            country_id = req[1]
            name_country = ''
            if country_id == "33":
                name_country = '🇫🇷 Франция'
            if country_id == "34":
                name_country = '🇪🇸 Испания'
            if country_id == "49":
                name_country = '🇩🇪 Германия'
            if country_id == "420":
                name_country = '🇨🇿 Чехия'
            if country_id == "357":
                name_country = '🇨🇾 Кипр'
            if country_id == "44":
                name_country = '🇬🇧 Британия'
            
            with open(f'price/price.json', 'r', encoding='utf-8') as f:
                         data = json.load(f)
            services = data[country_id]

                # Получаем значения для каждого сервиса
            buttons = []
            for service, price in services.items():
                    button_text = f"{service}: {price}$"
                    button = telebot.types.InlineKeyboardButton(text='🔸'+button_text, callback_data=f"service_{service}_{country_id}")
                    buttons.append(button)
            keyboard = telebot.types.InlineKeyboardMarkup(row_width=2)
            keyboard.add(*buttons)
                # отправляем пользователю эту клавиатуру
            bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text=f"<b>🔸Выбор сервиса\n🌐Страна: {name_country}</b>",reply_markup=keyboard)
                
        if req[0] == "service":
            service = req[1]
            country_id = req[2]
            #pay_list
            with open(f'price/price.json', 'r', encoding='utf-8') as f:
                        data = json.load(f)
            check = data[country_id][service]
            get_balance = MeDb(call.from_user.id)
            me_balance = get_balance.getMeBalance(call.from_user.id)
            
            if float(me_balance) < float(check):
                Deposit = types.InlineKeyboardMarkup(row_width=2)
                button = types.InlineKeyboardButton("👋 Пополнить", callback_data="Deposit")
                Deposit.add(button)
                bot.send_message(call.from_user.id, '‼️<b>На твоем балансе недостаточно средств чтобы купить номер для этого сервиса!</b>\n\n❕<i>Пополни баланс чтобы воспользоваться сервисом</i>',reply_markup=Deposit)
            else:
                #инициализация класса для обнвления баланса
                balance_up = float(me_balance) - float(check)
                init__Update = MeDb(call.from_user.id)
                updateDB = init__Update.UpdateBalance(call.from_user.id,balance_up)
                
                url = "https://onlinesim.io/api/getNum.php"
                params = {
                    "apikey": "Y5R6HGxgHdH765W-zkByFN13-1D77PmKc-ARUw6h64-2j84h9k8h29H8fD",
                    "service": service,
                    'country':country_id,
                }
                headers = {"accept": "application/json"}
                
                response = requests.get(url, params=params, headers=headers)
                j = json.loads(response.text)
                idtz_idtrans = str(j['tzid']) + '-' + str(call.from_user.id)  #id заказа и транзы
                output = j['response']
                tz_id = str(j['tzid'])
                if output == 'NO_NUMBER':
                    bot.send_message(call.from_user.id,'<b>🙅‍♂️На данный момент номера для данного сервиса нет</b>')
                if output == 1:
                    url = "https://onlinesim.io/api/getState.php"
                    params = {"apikey": "Y5R6HGxgHdH765W-zkByFN13-1D77PmKc-ARUw6h64-2j84h9k8h29H8fD",
                        "tzid":tz_id,
                            }
                    headers = {"accept": "application/json"}

                    response = requests.get(url, params=params, headers=headers)
                    j = json.loads(response.text)
                    with open(f'ordersNum/{idtz_idtrans}.json', 'w+') as src:
                        src.write(json.dumps(j, indent=2))
                    with open(f'ordersNum/{idtz_idtrans}.json', 'r', encoding='utf-8') as sr:
                        check = sr.read()
                        number = json.loads(check)
                        get_numbers = number[0]["number"]
                    name_country = ''
                    if country_id == "33":
                        name_country = '🇫🇷 Франция'
                    if country_id == "34":
                        name_country = '🇪🇸 Испания'
                    if country_id == "49":
                        name_country = '🇩🇪 Германия'
                    if country_id == "420":
                        name_country = '🇨🇿 Чехия'
                    if country_id == "357":
                        name_country = '🇨🇾 Кипр'
                    if country_id == "44":
                        name_country = '🇬🇧 Британия'
                    bot.send_message(call.from_user.id, f"<b>🌐 Страна: {name_country}</b>\n\n"+
                                    f'<b>💠Сервис: {service}</b>\n'
                                    f"<b>📞Номер телефона: </b> <code>{get_numbers}</code>\n\n"+
                                    '⚠️<b>После отправки смс код в бота поступит автоматически</b>')
                    getcode(idtz_idtrans, tz_id,service) 


idtz_idtrans = 0
tz_id = 0
service = 0
def getcode(idtz_idtrans, tz_id,service):
        print('new thread code')
        if idtz_idtrans != 0 and tz_id != 0 and service != 0:
            me_id = idtz_idtrans.split('-')[1]
            i = 0
            while i == 0:
                
                    time.sleep(10)
                    url = "https://onlinesim.io/api/getState.php"
                    params = {"apikey": "Y5R6HGxgHdH765W-zkByFN13-1D77PmKc-ARUw6h64-2j84h9k8h29H8fD",
                            "tzid":tz_id,
                                }
                    headers = {"accept": "application/json"}

                    response = requests.get(url, params=params, headers=headers)
                    j = json.loads(response.text)
                    with open(f'ordersNum/{idtz_idtrans}.json', 'w+') as src:
                            src.write(json.dumps(j, indent=2))
                    with open(f'ordersNum/{idtz_idtrans}.json', 'r', encoding='utf-8') as sr:
                            check = sr.read()
                            code = json.loads(check)
                            country_id = code[0]['country'] 
                    if code[0]['response'] == 'TZ_NUM_WAIT':
                        if code[0]['time'] < 700:
                            print(code[0]['time'])
                            #price_list
                            
                            with open(f'price/price.json', 'r', encoding='utf-8') as f:
                                data = json.load(f)
                                check = data[country_id][service]

                            get_balance = MeDb(me_id)
                            me_balance = get_balance.getMeBalance(me_id)
                            balance_up = float(me_balance) + float(check)
                            
                            init__Update = MeDb(me_id)
                            updateDB = init__Update.UpdateBalance(me_id,balance_up)
                            
                            
                            url_ok = "https://onlinesim.io/api/setOperationOk.php"
                            params_ok = {"apikey": "Y5R6HGxgHdH765W-zkByFN13-1D77PmKc-ARUw6h64-2j84h9k8h29H8fD",
                            "tzid":tz_id,
                                }
                            
            
                            headers_ok = {"accept": "application/json"}
                            responce_ok = requests.get(url_ok, params=params_ok, headers=headers_ok)
                            

                            
                            
                            bot.send_message(idtz_idtrans.split('-')[1],'<b>‼️Номер автматически отменен системой!\n♻️Средства вернулись на баланс</b>')
                            i += 1
                            os.remove('ordersNum/'+idtz_idtrans+'.json')
                        
                        elif code[0]['time'] > 700:
                            continue
                    if code[0]['response'] == 'TZ_NUM_ANSWER':
                        i += 1
                        sms = code[0]['msg']
                        bot.send_message(idtz_idtrans.split('-')[1], f'<b>🔔Новый код</b>\n\n🔒СМС-КОД: <code>{sms}</code>\n\n🎉Удачи')
                        getOrders = MeDb(me_id)
                        orders = getOrders.getMeOrders(me_id)
                        endOrder = orders + 1
                        getOrders.updateorders(me_id,endOrder)
                        os.remove('ordersNum/'+idtz_idtrans+'.json') 
            
            
        
    


def Qiwi_nomer(message):
    msg = message.text
    if msg == 'Отмена':
        start(message)
    else:
        print(type(msg))
        bot.send_message(message.chat.id, f'Вы пополняете {msg} гребней')


@bot.message_handler(content_types=['text'])
def abort_deposit(message):
    if message.text == 'Отмена':
        bot.send_message(message.chat.id, '🚨<b>Вы отменили заявку на пополнение!</b>')
    if message.text == 'Главное меню':
        start(message)





