from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
url = 'https://pokemondb.net/pokedex/all'
txt = open('Pokemon.txt','w+')

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = AppURLopener()
response = opener.open(url)
soup = BeautifulSoup(response, 'html.parser')
data = soup.get_text('td').split('td')

poke_list = []
poke_dict = {}
i = 0
for dat in data:
    dat = dat.strip()
    if(dat == ''):
        if(i>0):
            if(poke_list == []):
                pass
            else:
                poke_dict[poke_list[0]] = poke_list[1:]
                poke_list = []
        i += 1
        pass
    else:
        i = 0
        poke_list.append(dat)
key_removal = []
for keys in poke_dict.keys():
    try:
        key = int(keys)
    except ValueError:
        key_removal.append(keys)
for key in key_removal:
    poke_dict.pop(key)
for keyn in poke_dict.keys():
    for item in poke_dict[keyn]:
        try:
            txt.write(str(item) + ',')
        except UnicodeEncodeError:
            item = ''
            for letter in item:
                try:
                    item = item + str(letter)
                except UnicodeEncodeError:
                    pass
            txt.write(str(item) + ',') 
    txt.write('! \r\n')              
txt.close()