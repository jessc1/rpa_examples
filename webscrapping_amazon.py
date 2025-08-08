import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_excel('Template_Planilha_Teste.xlsx')

products = df['Produto']
prices = []
url = 'https://www.amazon.com.br/s?k='
for product in products:    
    search_url = f"{url}{product}"
    print(search_url)
    
    try:
        response = requests.get(search_url)
        print(response)        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')         
            whole_price = soup.find("span", attrs={"class": 'a-price-whole'}).text
            fraction_price = soup.find("span", attrs={"class": 'a-price-fraction'}).text
            price =  whole_price + fraction_price
          
            
            print('price', price)
            if price:
                df['Valor'] = price
           
            #print('pricces',prices)
            #print('nnnn====',product == df['Produto'])
            #print('produto', product)
             #   df['Valor'] = pd.Series(prices)
           
            
            
            
           
    except requests.exceptions.RequestException as e:
        print(f"Error searching for '{product}':{e}")


print(df)
