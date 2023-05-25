# -*- coding:utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
import json
import time
import telebot

bot = telebot.TeleBot(token = '6286287548:AAETXQytj03GCH0eV-jKOkw3NXsQlPodUFU',parse_mode ='HTML')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id,'Пришли мне номер формата 9000000000')
@bot.message_handler(content_types=['text'])
def check(message):
    number = message.text
    print(number)
    session = requests.Session()
    headers ={
      'Host':'ipoteka.vtb.ru',
      'Accept-Encoding' : 'gzip, deflate, br',
      'Content-Length' : '28',
      'Origin': 'https://ipoteka.vtb.ru',
      'Connection': 'keep-alive',
      'Referer': 'https://ipoteka.vtb.ru/ipoteka/phone',
      'Cookie': 'adrcid=AFoXNp-j5pvQYSEw1yH2-Fw; client_source={"utmSource":"direct_","utmMedium":"none","utmCampaign":"(not set)","utmTerm":"(not set)","utmContent":"(not set)","actionId":""}; utm_source=direct_; utm_medium=none; utm_campaign=(not set); utm_term=(not set); utm_content=(not set); tmr_lvid=58ffeca0dfe3055bc2ef91d46bce9812; tmr_lvidTS=1678784214828; _ym_uid=1669452687277215946; _ym_d=1682315272; _ym_isad=2; _ym_visorc=b; tmr_detect=0%7C1682315276122',
      'Sec-Fetch-Dest': 'empty',
       'Sec-Fetch-Mode': 'cors',
       'Sec-Fetch-Site': 'same-origin',
       'Accept': 'application/json, text/plain, */*',
       'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
       'Content-Type': 'application/json',
       'X-Finger-Print': 'eyJmb250cyI6eyJ2YWx1ZSI6WyJBZ2VuY3kgRkIiLCJBcmlhbCBVbmljb2RlIE1TIiwiQ2FsaWJyaSIsIkNlbnR1cnkiLCJDZW50dXJ5IEdvdGhpYyIsIkZyYW5rbGluIEdvdGhpYyIsIkhFTFYiLCJIYWV0dGVuc2Nod2VpbGVyIiwiTHVjaWRhIEJyaWdodCIsIkx1Y2lkYSBTYW5zIiwiTVMgT3V0bG9vayIsIk1TIFJlZmVyZW5jZSBTcGVjaWFsdHkiLCJNUyBVSSBHb3RoaWMiLCJNVCBFeHRyYSIsIk1ZUklBRCBQUk8iLCJNYXJsZXR0IiwiTWVpcnlvIFVJIiwiTW9ub3R5cGUgQ29yc2l2YSIsIlByaXN0aW5hIiwiU2Vnb2UgVUkgTGlnaHQiLCJTbWFsbCBGb250cyJdLCJkdXJhdGlvbiI6MTIwfSwiZG9tQmxvY2tlcnMiOnsiZHVyYXRpb24iOjE5fSwiZm9udFByZWZlcmVuY2VzIjp7InZhbHVlIjp7ImRlZmF1bHQiOjE0OS4zNTAwMDYxMDM1MTU2MiwiYXBwbGUiOjE0OS4zNTAwMDYxMDM1MTU2Miwic2VyaWYiOjE0OS4zNTAwMDYxMDM1MTU2Miwic2FucyI6MTQ0LjAxNjY2MjU5NzY1NjI1LCJtb25vIjoxMTksIm1pbiI6OS4zNjY2Njg3MDExNzE4NzUsInN5c3RlbSI6MTQ3Ljg5OTk5Mzg5NjQ4NDM4fSwiZHVyYXRpb24iOjM4Mn0sImF1ZGlvIjp7InZhbHVlIjozNS43MzgzMjk1OTMwOTIyLCJkdXJhdGlvbiI6Mjk3fSwic2NyZWVuRnJhbWUiOnsidmFsdWUiOlstMTIwLDE5MjAsMTYwLC0xOTIwXSwiZHVyYXRpb24iOjF9LCJvc0NwdSI6eyJ2YWx1ZSI6IldpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCIsImR1cmF0aW9uIjoxfSwibGFuZ3VhZ2VzIjp7InZhbHVlIjpbWyJydS1SVSJdLFsicnUtUlUiLCJydSIsImVuLVVTIiwiZW4iXV0sImR1cmF0aW9uIjowfSwiY29sb3JEZXB0aCI6eyJ2YWx1ZSI6MjQsImR1cmF0aW9uIjowfSwiZGV2aWNlTWVtb3J5Ijp7ImR1cmF0aW9uIjowfSwic2NyZWVuUmVzb2x1dGlvbiI6eyJ2YWx1ZSI6WzE5MjAsMTIwMF0sImR1cmF0aW9uIjowfSwiaGFyZHdhcmVDb25jdXJyZW5jeSI6eyJ2YWx1ZSI6MiwiZHVyYXRpb24iOjB9LCJ0aW1lem9uZSI6eyJ2YWx1ZSI6IkV1cm9wZS9Nb3Njb3ciLCJkdXJhdGlvbiI6MX0sInNlc3Npb25TdG9yYWdlIjp7InZhbHVlIjp0cnVlLCJkdXJhdGlvbiI6MH0sImxvY2FsU3RvcmFnZSI6eyJ2YWx1ZSI6dHJ1ZSwiZHVyYXRpb24iOjB9LCJpbmRleGVkREIiOnsidmFsdWUiOnRydWUsImR1cmF0aW9uIjowfSwib3BlbkRhdGFiYXNlIjp7InZhbHVlIjpmYWxzZSwiZHVyYXRpb24iOjB9LCJjcHVDbGFzcyI6eyJkdXJhdGlvbiI6MH0sInBsYXRmb3JtIjp7InZhbHVlIjoiV2luMzIiLCJkdXJhdGlvbiI6MH0sInBsdWdpbnMiOnsidmFsdWUiOlt7Im5hbWUiOiJQREYgVmlld2VyIiwiZGVzY3JpcHRpb24iOiJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQiLCJtaW1lVHlwZXMiOlt7InR5cGUiOiJhcHBsaWNhdGlvbi9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9LHsidHlwZSI6InRleHQvcGRmIiwic3VmZml4ZXMiOiJwZGYifV19LHsibmFtZSI6IkNocm9tZSBQREYgVmlld2VyIiwiZGVzY3JpcHRpb24iOiJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQiLCJtaW1lVHlwZXMiOlt7InR5cGUiOiJhcHBsaWNhdGlvbi9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9LHsidHlwZSI6InRleHQvcGRmIiwic3VmZml4ZXMiOiJwZGYifV19LHsibmFtZSI6IkNocm9taXVtIFBERiBWaWV3ZXIiLCJkZXNjcmlwdGlvbiI6IlBvcnRhYmxlIERvY3VtZW50IEZvcm1hdCIsIm1pbWVUeXBlcyI6W3sidHlwZSI6ImFwcGxpY2F0aW9uL3BkZiIsInN1ZmZpeGVzIjoicGRmIn0seyJ0eXBlIjoidGV4dC9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9XX0seyJuYW1lIjoiTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlciIsImRlc2NyaXB0aW9uIjoiUG9ydGFibGUgRG9jdW1lbnQgRm9ybWF0IiwibWltZVR5cGVzIjpbeyJ0eXBlIjoiYXBwbGljYXRpb24vcGRmIiwic3VmZml4ZXMiOiJwZGYifSx7InR5cGUiOiJ0ZXh0L3BkZiIsInN1ZmZpeGVzIjoicGRmIn1dfSx7Im5hbWUiOiJXZWJLaXQgYnVpbHQtaW4gUERGIiwiZGVzY3JpcHRpb24iOiJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQiLCJtaW1lVHlwZXMiOlt7InR5cGUiOiJhcHBsaWNhdGlvbi9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9LHsidHlwZSI6InRleHQvcGRmIiwic3VmZml4ZXMiOiJwZGYifV19XSwiZHVyYXRpb24iOjB9LCJ0b3VjaFN1cHBvcnQiOnsidmFsdWUiOnsibWF4VG91Y2hQb2ludHMiOjAsInRvdWNoRXZlbnQiOmZhbHNlLCJ0b3VjaFN0YXJ0IjpmYWxzZX0sImR1cmF0aW9uIjowfSwidmVuZG9yIjp7InZhbHVlIjoiIiwiZHVyYXRpb24iOjB9LCJ2ZW5kb3JGbGF2b3JzIjp7InZhbHVlIjpbXSwiZHVyYXRpb24iOjB9LCJjb29raWVzRW5hYmxlZCI6eyJ2YWx1ZSI6dHJ1ZSwiZHVyYXRpb24iOjB9LCJjb2xvckdhbXV0Ijp7InZhbHVlIjoic3JnYiIsImR1cmF0aW9uIjowfSwiaW52ZXJ0ZWRDb2xvcnMiOnsiZHVyYXRpb24iOjB9LCJmb3JjZWRDb2xvcnMiOnsidmFsdWUiOmZhbHNlLCJkdXJhdGlvbiI6MH0sIm1vbm9jaHJvbWUiOnsidmFsdWUiOjAsImR1cmF0aW9uIjowfSwiY29udHJhc3QiOnsidmFsdWUiOjAsImR1cmF0aW9uIjowfSwicmVkdWNlZE1vdGlvbiI6eyJ2YWx1ZSI6ZmFsc2UsImR1cmF0aW9uIjowfSwiaGRyIjp7InZhbHVlIjpmYWxzZSwiZHVyYXRpb24iOjB9LCJtYXRoIjp7InZhbHVlIjp7ImFjb3MiOjEuNDQ3MzU4ODY1ODI3ODUyMiwiYWNvc2giOjcwOS44ODkzNTU4MjI3MjYsImFjb3NoUGYiOjM1NS4yOTEyNTE1MDE2NDMsImFzaW4iOjAuMTIzNDM3NDYwOTY3MDQ0MzUsImFzaW5oIjowLjg4MTM3MzU4NzAxOTU0MywiYXNpbmhQZiI6MC44ODEzNzM1ODcwMTk1NDI5LCJhdGFuaCI6MC41NDkzMDYxNDQzMzQwNTQ4LCJhdGFuaFBmIjowLjU0OTMwNjE0NDMzNDA1NDgsImF0YW4iOjAuNDYzNjQ3NjA5MDAwODA2MSwic2luIjowLjgxNzg4MTkxMjExNTkwODUsInNpbmgiOjEuMTc1MjAxMTkzNjQzODAxNCwic2luaFBmIjoyLjUzNDM0MjEwNzg3MzMyNCwiY29zIjotMC44MzkwNzE1MjkwMDk1Mzc3LCJjb3NoIjoxLjU0MzA4MDYzNDgxNTI0MzcsImNvc2hQZiI6MS41NDMwODA2MzQ4MTUyNDM3LCJ0YW4iOi0xLjQyMTQ0ODgyMzg3NDcyNDUsInRhbmgiOjAuNzYxNTk0MTU1OTU1NzY0OSwidGFuaFBmIjowLjc2MTU5NDE1NTk1NTc2NDksImV4cCI6Mi43MTgyODE4Mjg0NTkwNDUsImV4cG0xIjoxLjcxODI4MTgyODQ1OTA0NSwiZXhwbTFQZiI6MS43MTgyODE4Mjg0NTkwNDUsImxvZzFwIjoyLjM5Nzg5NTI3Mjc5ODM3MDcsImxvZzFwUGYiOjIuMzk3ODk1MjcyNzk4MzcwNywicG93UEkiOjEuOTI3NTgxNDE2MDU2MDIwNmUtNTB9LCJkdXJhdGlvbiI6MH19'
         }
   
   
    param = {'phoneNumber': f'{number}'}
    json_param = json.dumps(param)
    # отправка POST-запроса с данными в формате JSON
    r = session.post('https://ipoteka.vtb.ru/api/v1/auth/sendPhoneNumber',headers=headers,data=json_param)
    j = json.loads(r.text) # обрезаем лишнее обрамление у JSON
    with open('out.json', 'w+') as src:
            src.write(json.dumps(j, indent= 2))
            src.close()
    with open('out.json', 'r',encoding='utf-8') as sr:
        check = sr.read()
        templates = json.loads(check)
    out = templates['result']['status']
    if out == 401:
        bot.send_message(message.chat.id,'<b>✅Смс отправлено</b>')
    else:
        bot.send_message(message.chat.id,'<b>❌Не отправлено</b>')
            
            
            
            



bot.infinity_polling()