from sms import *
from pay_crypto import *


if __name__ == '__main__':
    from sms import bot
    thread = threading.Thread(target=checkPay, args=(name,))
    thread = threading.Thread(target=getcode, args=(idtz_idtrans, tz_id, service))
    thread.start()
    

    bot.infinity_polling() 