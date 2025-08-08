import requests
from bs4 import BeautifulSoup
import re

def get_title(soup):
    
    try:
        #outer tag object
        title = soup.find("span", attrs= {"id": 'productTitle'})
        
        #inner navigatable string object
        title_value = title.text
        
        #Title as string value
        title_string = title_value.strip()
        
    except AttributeError:
        title_string = ""
        
    return title_string

def Product_Price(soup):
    try:
        whole_price = soup.find("span", attrs={"class": 'a-price-whole'}).text
        
        fraction_price = soup.find("span", attrs={"class": 'a-price-fraction'}).text
        
        Product_Price = whole_price + fraction_price
        
    except:
        
        try:
            whole_price = soup.find("span", attrs={"class": 'a-price-whole'}).text
        
            Product_Price = whole_price
            
        except:
            Product_Price = ""
        
    return Product_Price
"""url = 'https://www.amazon.com.br/Apple-iPhone-16-Plus-128/dp/B0DGLZC96M/ref=sr_1_1_sspa?crid=GBAR9UBYHUEO&dib=eyJ2IjoiMSJ9.4wTMfF92Nocf2t7rMuNFdhmMM-mlgwWz1w5NAfhebH2cZuMRD24OY7G5TTyN31VqNvYddSY8w_MJkfHpBQtSBaGAo6_RwBCRJ8cbSGVmMw0nA2woQW0x3Fj4lhgJXzVZvrJyI5wKcLKFCfZbvxjGWmjFWSdcivrLzMT7WcK7RtcadprhVzVF7F5NTtZQOspCTXqFOHAZpi0OkQMHGH7Hq7s16HERTKSJrXOLYOirDofd2_3zzuD3YaM-1GFKUKmioU0wD3yMpEw1yvc9ncQS2nqTHnsiQ8RsQOyt5700ePA.92kLUH_VMmK219cLJZTZqNNr3xYmnpF4teN7yToWs3U&dib_tag=se&keywords=iphone%2B16&qid=1753297194&sprefix=i%2Caps%2C728&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.9e6a115c-05b9-4b96-8e1c-b1f9ce2ac1a6&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1' # Replace with the desired product URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html')
title = soup.select_one('#productTitle')
price = Product_Price(soup)
print('aaaa',title)
print('price', price)

#with open('amazon_page.html', 'w') as f:
 #   f.write(response.text)"""


if __name__ == '__main__':
    url = 'https://www.amazon.com.br/' 
    search_param = 's?k'
    results = {}
