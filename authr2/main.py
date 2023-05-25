# -*- coding:utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
import json
import time



def check():
    session = requests.Session()
    headers ={
      'Host':'ipoteka.vtb.ru',
      'Accept-Encoding' : 'gzip, deflate, br',
      'Content-Length' : '28',
      'Origin': 'https://ipoteka.vtb.ru',
      'Connection': 'keep-alive',
      'Referer': 'https://ipoteka.vtb.ru/phone',
      'Cookie': 'adrcid=AFoXNp-j5pvQYSEw1yH2-Fw; _ym_uid=1669452687277215946; _ym_d=1678785871; tmr_lvid=58ffeca0dfe3055bc2ef91d46bce9812; tmr_lvidTS=1678784214828; client_source={"utmSource":"direct_","utmMedium":"none","utmCampaign":"(not set)","utmTerm":"(not set)","utmContent":"(not set)","actionId":""}; utm_source=direct_; utm_medium=none; utm_campaign=(not set); utm_term=(not set); utm_content=(not set)',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      'Content-Type': 'application/json',
      'X-Finger-Print': 'eyJmb250cyI6eyJ2YWx1ZSI6WyJBZ2VuY3kgRkIiLCJBcmlhbCBVbmljb2RlIE1TIiwiQ2FsaWJyaSIsIkNlbnR1cnkiLCJDZW50dXJ5IEdvdGhpYyIsIkZyYW5rbGluIEdvdGhpYyIsIkhFTFYiLCJIYWV0dGVuc2Nod2VpbGVyIiwiTHVjaWRhIEJyaWdodCIsIkx1Y2lkYSBTYW5zIiwiTVMgT3V0bG9vayIsIk1TIFJlZmVyZW5jZSBTcGVjaWFsdHkiLCJNUyBVSSBHb3RoaWMiLCJNVCBFeHRyYSIsIk1hcmxldHQiLCJNZWlyeW8gVUkiLCJNb25vdHlwZSBDb3JzaXZhIiwiUHJpc3RpbmEiLCJTbWFsbCBGb250cyJdLCJkdXJhdGlvbiI6MTc3fSwiZG9tQmxvY2tlcnMiOnsiZHVyYXRpb24iOjI0fSwiZm9udFByZWZlcmVuY2VzIjp7InZhbHVlIjp7ImRlZmF1bHQiOjE0OS4zNTAwMDYxMDM1MTU2MiwiYXBwbGUiOjE0OS4zNTAwMDYxMDM1MTU2Miwic2VyaWYiOjE0OS4zNTAwMDYxMDM1MTU2Miwic2FucyI6MTQ0LjAxNjY2MjU5NzY1NjI1LCJtb25vIjoxMTksIm1pbiI6OS4zNjY2Njg3MDExNzE4NzUsInN5c3RlbSI6MTQ3Ljg5OTk5Mzg5NjQ4NDM4fSwiZHVyYXRpb24iOjI0MH0sImF1ZGlvIjp7InZhbHVlIjozNS43MzgzMjk1OTMwOTIyLCJkdXJhdGlvbiI6MTY0fSwic2NyZWVuRnJhbWUiOnsidmFsdWUiOlstMTIwLDE5MjAsMTYwLC0xOTIwXSwiZHVyYXRpb24iOjB9LCJvc0NwdSI6eyJ2YWx1ZSI6IldpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCIsImR1cmF0aW9uIjowfSwibGFuZ3VhZ2VzIjp7InZhbHVlIjpbWyJydS1SVSJdLFsicnUtUlUiLCJydSIsImVuLVVTIiwiZW4iXV0sImR1cmF0aW9uIjowfSwiY29sb3JEZXB0aCI6eyJ2YWx1ZSI6MjQsImR1cmF0aW9uIjowfSwiZGV2aWNlTWVtb3J5Ijp7ImR1cmF0aW9uIjowfSwic2NyZWVuUmVzb2x1dGlvbiI6eyJ2YWx1ZSI6WzE5MjAsMTIwMF0sImR1cmF0aW9uIjowfSwiaGFyZHdhcmVDb25jdXJyZW5jeSI6eyJ2YWx1ZSI6MiwiZHVyYXRpb24iOjF9LCJ0aW1lem9uZSI6eyJ2YWx1ZSI6IkFmcmljYS9LaGFydG91bSIsImR1cmF0aW9uIjowfSwic2Vzc2lvblN0b3JhZ2UiOnsidmFsdWUiOnRydWUsImR1cmF0aW9uIjowfSwibG9jYWxTdG9yYWdlIjp7InZhbHVlIjp0cnVlLCJkdXJhdGlvbiI6MH0sImluZGV4ZWREQiI6eyJ2YWx1ZSI6dHJ1ZSwiZHVyYXRpb24iOjB9LCJvcGVuRGF0YWJhc2UiOnsidmFsdWUiOmZhbHNlLCJkdXJhdGlvbiI6MH0sImNwdUNsYXNzIjp7ImR1cmF0aW9uIjowfSwicGxhdGZvcm0iOnsidmFsdWUiOiJXaW4zMiIsImR1cmF0aW9uIjowfSwicGx1Z2lucyI6eyJ2YWx1ZSI6W3sibmFtZSI6IlBERiBWaWV3ZXIiLCJkZXNjcmlwdGlvbiI6IlBvcnRhYmxlIERvY3VtZW50IEZvcm1hdCIsIm1pbWVUeXBlcyI6W3sidHlwZSI6ImFwcGxpY2F0aW9uL3BkZiIsInN1ZmZpeGVzIjoicGRmIn0seyJ0eXBlIjoidGV4dC9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9XX0seyJuYW1lIjoiQ2hyb21lIFBERiBWaWV3ZXIiLCJkZXNjcmlwdGlvbiI6IlBvcnRhYmxlIERvY3VtZW50IEZvcm1hdCIsIm1pbWVUeXBlcyI6W3sidHlwZSI6ImFwcGxpY2F0aW9uL3BkZiIsInN1ZmZpeGVzIjoicGRmIn0seyJ0eXBlIjoidGV4dC9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9XX0seyJuYW1lIjoiQ2hyb21pdW0gUERGIFZpZXdlciIsImRlc2NyaXB0aW9uIjoiUG9ydGFibGUgRG9jdW1lbnQgRm9ybWF0IiwibWltZVR5cGVzIjpbeyJ0eXBlIjoiYXBwbGljYXRpb24vcGRmIiwic3VmZml4ZXMiOiJwZGYifSx7InR5cGUiOiJ0ZXh0L3BkZiIsInN1ZmZpeGVzIjoicGRmIn1dfSx7Im5hbWUiOiJNaWNyb3NvZnQgRWRnZSBQREYgVmlld2VyIiwiZGVzY3JpcHRpb24iOiJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQiLCJtaW1lVHlwZXMiOlt7InR5cGUiOiJhcHBsaWNhdGlvbi9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9LHsidHlwZSI6InRleHQvcGRmIiwic3VmZml4ZXMiOiJwZGYifV19LHsibmFtZSI6IldlYktpdCBidWlsdC1pbiBQREYiLCJkZXNjcmlwdGlvbiI6IlBvcnRhYmxlIERvY3VtZW50IEZvcm1hdCIsIm1pbWVUeXBlcyI6W3sidHlwZSI6ImFwcGxpY2F0aW9uL3BkZiIsInN1ZmZpeGVzIjoicGRmIn0seyJ0eXBlIjoidGV4dC9wZGYiLCJzdWZmaXhlcyI6InBkZiJ9XX1dLCJkdXJhdGlvbiI6MH0sInRvdWNoU3VwcG9ydCI6eyJ2YWx1ZSI6eyJtYXhUb3VjaFBvaW50cyI6MCwidG91Y2hFdmVudCI6ZmFsc2UsInRvdWNoU3RhcnQiOmZhbHNlfSwiZHVyYXRpb24iOjB9LCJ2ZW5kb3IiOnsidmFsdWUiOiIiLCJkdXJhdGlvbiI6MH0sInZlbmRvckZsYXZvcnMiOnsidmFsdWUiOltdLCJkdXJhdGlvbiI6MH0sImNvb2tpZXNFbmFibGVkIjp7InZhbHVlIjp0cnVlLCJkdXJhdGlvbiI6MX0sImNvbG9yR2FtdXQiOnsidmFsdWUiOiJzcmdiIiwiZHVyYXRpb24iOjB9LCJpbnZlcnRlZENvbG9ycyI6eyJkdXJhdGlvbiI6NH0sImZvcmNlZENvbG9ycyI6eyJ2YWx1ZSI6ZmFsc2UsImR1cmF0aW9uIjowfSwibW9ub2Nocm9tZSI6eyJ2YWx1ZSI6MCwiZHVyYXRpb24iOjB9LCJjb250cmFzdCI6eyJ2YWx1ZSI6MCwiZHVyYXRpb24iOjB9LCJyZWR1Y2VkTW90aW9uIjp7InZhbHVlIjpmYWxzZSwiZHVyYXRpb24iOjB9LCJoZHIiOnsidmFsdWUiOmZhbHNlLCJkdXJhdGlvbiI6MH0sIm1hdGgiOnsidmFsdWUiOnsiYWNvcyI6MS40NDczNTg4NjU4Mjc4NTIyLCJhY29zaCI6NzA5Ljg4OTM1NTgyMjcyNiwiYWNvc2hQZiI6MzU1LjI5MTI1MTUwMTY0MywiYXNpbiI6MC4xMjM0Mzc0NjA5NjcwNDQzNSwiYXNpbmgiOjAuODgxMzczNTg3MDE5NTQzLCJhc2luaFBmIjowLjg4MTM3MzU4NzAxOTU0MjksImF0YW5oIjowLjU0OTMwNjE0NDMzNDA1NDgsImF0YW5oUGYiOjAuNTQ5MzA2MTQ0MzM0MDU0OCwiYXRhbiI6MC40NjM2NDc2MDkwMDA4MDYxLCJzaW4iOjAuODE3ODgxOTEyMTE1OTA4NSwic2luaCI6MS4xNzUyMDExOTM2NDM4MDE0LCJzaW5oUGYiOjIuNTM0MzQyMTA3ODczMzI0LCJjb3MiOi0wLjgzOTA3MTUyOTAwOTUzNzcsImNvc2giOjEuNTQzMDgwNjM0ODE1MjQzNywiY29zaFBmIjoxLjU0MzA4MDYzNDgxNTI0MzcsInRhbiI6LTEuNDIxNDQ4ODIzODc0NzI0NSwidGFuaCI6MC43NjE1OTQxNTU5NTU3NjQ5LCJ0YW5oUGYiOjAuNzYxNTk0MTU1OTU1NzY0OSwiZXhwIjoyLjcxODI4MTgyODQ1OTA0NSwiZXhwbTEiOjEuNzE4MjgxODI4NDU5MDQ1LCJleHBtMVBmIjoxLjcxODI4MTgyODQ1OTA0NSwibG9nMXAiOjIuMzk3ODk1MjcyNzk4MzcwNywibG9nMXBQZiI6Mi4zOTc4OTUyNzI3OTgzNzA3LCJwb3dQSSI6MS45Mjc1ODE0MTYwNTYwMjA2ZS01MH0sImR1cmF0aW9uIjowfX0='
         }
   
    with open('base.txt','r', encoding='utf-8') as src:
      nums  = src.readlines()
      for i in nums:
            
        try:    
            t = i[1:].split('\n')
            param = {'phoneNumber': f'{t[0]}'}
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
            out = templates['result']['username']
            if int(out[:1]) < 5:
                with open('fold/vtb.txt','a') as s:
                    s.write(i)
                    s.close()
                    print('|RESULT| => |200|')
            if int(out[:1]) >= 5:
                with open('fold/Novtb.txt','a') as s:
                    s.write(i)
                    s.close()
                    print('|RESULT| => |404|')
        except:
            print('|CONNCTION CLOSED|')
            time.sleep(5)
            continue
            
            
            



check()