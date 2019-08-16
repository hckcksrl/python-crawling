from urllib.request import urlopen
import urllib.parse
from bs4 import BeautifulSoup
url1 = 'https://lolchess.gg/profile/kr/'
url2 = urllib.parse.quote_plus('신성동나부랭이')
ful = url1+url2

html = urlopen(ful)

bs = BeautifulSoup(html,'html.parser')

a = bs.select('#profile > div > div:nth-child(2) > div:nth-child(1) > div.col-lg-4 > div.profile__tier > div.profile__tier__stats > div  ')
b = bs.select('#profile > div > div:nth-child(2) > div:nth-child(1) > div.col-lg-4 > div.profile__tier > div.profile__tier__info > div.profile__tier__summary')

t=[]

if not b :
    print('전적 정보가 없다')
else :
    print('asdd')

for i in b :
    t= i.text.split()

for i in t :
    print(i)




# for i in a :
#    t =  i.text.split()
#
# for i in t :
#     print(i)