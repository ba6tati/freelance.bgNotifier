import requests
from bs4 import BeautifulSoup
import io
import time
import subprocess
from notifypy import Notify

url = 'https://www.freelance.bg/'

start = time.time()
while True:
    print(f'The program is running for {time.time() - start} seconds')
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    # raw_premium_ads = soup.findAll('a', {'class': 'user-premium'})
    
    # last_premium_ad = raw_premium_ads[0].text

    raw_ads = soup.findAll('a', {'class': 'user-normal'})

    last_ad = raw_ads[0].text
    
    

    with io.open('data', 'r', encoding='utf-8') as f:
        data = f.readlines()
    
    with io.open('data', 'w', encoding='utf-8') as f:
        found = False
        for i, var in enumerate(data):
            if var.startswith('last_ad'):
                if var.split('=')[1] == last_ad:
                    found = True
                else:
                    notification = Notify()
                    notification.title = 'New Project!'
                    notification.message = f'{last_ad}'
                    notification.send()
                    
                    data[i] = f'last_ad={last_ad}'
                    found = True
                break
            
        if not found:
            data.append(f'last_ad={last_ad}')
            
        f.writelines(data)

"""
with io.open('results.txt', "w", encoding="utf-8") as f:
    for raw_ad in raw_ads:
        f.write(raw_ad.text + '\n')
        
"""