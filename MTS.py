import requests
from bs4 import BeautifulSoup
main_url='https://www.mtsdata.com/content/data/public/slk/fixing'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
main_response=requests.request('GET',url=main_url,headers=headers)
print(main_response.status_code)
main_soup=BeautifulSoup(main_response.content,'html.parser')
# print(main_soup)
tr_tag=main_soup.find('tr').find('a')['href']


