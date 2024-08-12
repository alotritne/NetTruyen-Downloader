import os
try:
    os.system('clear')
except:
    os.system('cls')
banner =r"""
  _   _      _ _______                            _____                      _                 _           
 | \ | |    | |__   __|                          |  __ \                    | |               | |          
 |  \| | ___| |_ | |_ __ _   _ _   _  ___ _ __   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 | . ` |/ _ \ __|| | '__| | | | | | |/ _ \ '_ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
 | |\  |  __/ |_ | | |  | |_| | |_| |  __/ | | | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 |_| \_|\___|\__||_|_|   \__,_|\__, |\___|_| |_| |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                __/ |                                                                      
                               |___/                                                                       
"""
print(banner)



try:
    import requests
except:
    os.system('pip install requests')
try:
    from bs4 import BeautifulSoup
except:
    os.system('pip install bs4')
try:
    import wget
except:
    os.system('pip3 install wget')
try:
    import re
except:
    os.system('pip install re')    
try:
    import threading
except:
    os.system('pip install threading')
thumucgoc = os.getcwd()
if os.path.exists('link.txt'):
    os.remove('link.txt')
else:
    pass
from concurrent.futures import ThreadPoolExecutor
def taianh(i):
    global anh
    anh = i.img.get('data-src')
    print(anh)
    tenanh = re.search(r'/nettruyen/(.*)', anh).group(1)
    tenanh = tenanh.replace('/', '_')
    if os.path.exists(f'{tenanh}'):
        pass
    else:
        laylanh = requests.get(anh).content
        with open(f'{tenanh}', 'wb') as handler:
            handler.write(laylanh)

linktruyen = input('Nhập link truyện: ')
respones = requests.get(linktruyen)
soup = BeautifulSoup(respones.text, 'html.parser')
linkchap = soup.find_all('div', class_='col-xs-5 chapter')
for link in linkchap:
    open(f'link.txt', 'a').write(link.a.get('href') + '\n')
with open('link.txt', 'r') as file:
    lines = file.readlines()
    xoadong = set(lines)
with open('link.txt', 'w') as file:
    file.writelines(xoadong)
linkne = open('link.txt', 'r')
for url in linkne:
    respones = requests.get(url)
    soup = BeautifulSoup(respones.text, 'html.parser')
    tenchap = re.search(r' </a> <span>- (.*?)</span>', respones.text).group(1)
    tentruyen = re.search(r'/truyen-tranh/(.*?)/', url).group(1)
    if os.path.exists(f'{tentruyen}'):
        pass
    else:
        os.makedirs(f'{tentruyen}')
    os.chdir(f'{tentruyen}')
    if os.path.exists(f'{tenchap}'):
        pass
    else:
        os.makedirs(f'{tenchap}')
    os.chdir(f'{tenchap}')

    image = soup('div',class_="page-chapter")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in image:
            [].append(executor.submit(taianh,i))
    os.chdir(thumucgoc) # type: ignore

