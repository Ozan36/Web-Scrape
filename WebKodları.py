import requests
from bs4 import BeautifulSoup

# Verisi alınan web sayfasının URL'si
url = 'https://www.w4getsdh.com'

# Web sayfasını almak için GET isteği yapılır
response = requests.get(url)
# istek onaylanırsa 200 değeri gönderilir
print(response)
# Web sayfasının içeriği BeautifulSoup ile parse edilir
pars = BeautifulSoup(response.text, 'html.parser')

# başlıklar değişkeninin içerisine h1 başlığı atanır
basliklar  = pars.find_all('h1')
# başlıklar2 değişkeninin içerisine h2 başlığı atanır
basliklar2 = pars.find_all('h2')
# başlıklar3 değişkeninin içerisine h3 başlığı atanır
basliklar3 = pars.find_all('h3')

# Sitenin başlığı yazdırılır
print( pars.find_all('title'))

# H1 başlıkları ekrana yazdır
for baslik in basliklar:
    print(baslik.text)
# H2 başlıklarını yan yana yazdırır
for baslik1 in basliklar2:
    print(*baslik1.text,sep="\t")
# H3 başlıklarını  alt alta yazdırır  
for baslik2 in basliklar3:
    print(baslik2.text)