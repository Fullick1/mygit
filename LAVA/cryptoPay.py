import json
import requests
import time
import sqlite3








def create_payorder(message): 
    from main import bot,types
    msg_pay = message.text
    if msg_pay == 'Отмена':
        bot.send_message(message.chat.id,'<b>✖️Транзакция отменена</b>')
    else:
        url = 'https://pay.crypt.bot/api/createInvoice'
        headers = {'Crypto-Pay-API-Token': '100211:AAVPAtnqSJQdD8f1UTsAHxXcMDjW2NXEH1d'}
        payload = {
            'asset': 'USDT',
            'amount': msg_pay,
        }

        response = requests.post(url, headers=headers, json=payload)

        j = json.loads(response.text)
        
        url_pay = j['result']['pay_url']
        hash_pay = j['result']['hash']
        amount_pay = j['result']['amount']
        asset_pay = j['result']['asset']
        time_pay = j['result']['created_at']
        markup_urlPay = types.InlineKeyboardMarkup(row_width=2)
        url_button = types.InlineKeyboardButton("🏧Оплатить", url=f"{url_pay}")
        markup_urlPay.add(url_button)
        bot.send_message(message.chat.id,f'<b>🌴Ордер</b>: <code>{hash_pay}</code>\n'+
                                        f'\n<i>🤑Сумма оплаты: {amount_pay} {asset_pay}</i>\n'
                                        f'\n<code>#{time_pay}</code>',reply_markup = markup_urlPay)

        name = str(hash_pay) + '-' + str(message.chat.id)
        with open(f'paymentsLog/{name}', 'w',encoding='utf-8') as src:
            src.write(json.dumps(j, indent=2))
        checkPay(name)






name = 0
def checkPay(name):
        if name != 0:
            from main import bot
            hasH = name.split('-')[0]
            id_user = name.split('-')[1]
            bot.send_message(id_user,'<b>♻️После поступления средств бот тебя оповестит</b>')
            with open(f'paymentsLog/{name}', 'r',encoding='utf-8') as sr:
                check = sr.read()
                chek_status = json.loads(check)
            asset = chek_status['result']['asset']
            amount = chek_status['result']['amount']
            ivoice = chek_status['result']['invoice_id']
            
            
            i = 0
            while i == 0:
                time.sleep(5)
                url = 'https://pay.crypt.bot/api/getInvoices'
                headers = {'Crypto-Pay-API-Token': '100211:AAVPAtnqSJQdD8f1UTsAHxXcMDjW2NXEH1d'}
                payload = {
                    'asset': f'{asset}',
                    'invoice_ids': f'{ivoice}'
                    }
                response = requests.get(url, headers=headers, json=payload)
                j = json.loads(response.text)
                print (j['result']['items'][0]['status'])
                if j['result']['items'][0]['status'] == 'active':
                    print('wait')
                if j['result']['items'][0]['status'] == 'paid':
                    db = sqlite3.connect('database/base.db')
                    cursor = db.cursor()
                    now_balance = cursor.execute('SELECT cash FROM users WHERE id = ?', (id_user,)).fetchone()[0]
                    balance = float(now_balance) + float(amount)
                    print(balance)
                    cursor.execute(f'UPDATE users SET cash = {balance} WHERE id = {id_user}')
                    db.commit()
                    bot.send_message(id_user,f'<b>✅Ордер: {hasH} оплачен!</b>\n'+
                                            f'\n<b>➕Твой баланс пополнен на {amount} usdt</b>')
                    i += 1
                if j['result']['items'][0]['status'] == 'expired':
                    bot.send_message(id_user,f'<b>📣Ордер: {hasH}\n</b> отменен!</b>') 
                    i += 1