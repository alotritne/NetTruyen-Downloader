import os
os.system('cls')
os.system('clear')
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
def taianh(i,tentruyen):
    global anh
    anh = i.img.get('data-sv1')
    tenanh = re.search(r'/nettruyen/(.*)', anh).group(1)
    tenanh = tenanh.replace('/', '_')
    if os.path.exists(f'{tenanh}'):
        pass
    else:
        try:
            headers = {
                'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
                'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                'priority': 'i',
                'referer': 'https://nettruyenaa.com/',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Brave";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'image',
                'sec-fetch-mode': 'no-cors',
                'sec-fetch-site': 'cross-site',
                'sec-gpc': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}

            laylanh = requests.get(anh, headers=headers)
            if laylanh.status_code == 200:
                print(f'tải thành công {tenanh}')
            else:
                print(f'lỗi khi tải {tenanh}')
                open(f'loi_{tentruyen}.txt', 'a').write(anh + '\n')

            with open(f'{tenanh}', 'wb') as file:
                file.write(laylanh.content)
        except Exception as e:
            print(e)

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
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in image:
            [].append(executor.submit(taianh,i,tentruyen))
    os.chdir(thumucgoc)
input("Đã hoàn thành")
