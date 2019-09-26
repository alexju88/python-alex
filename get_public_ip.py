#Python3
#from bs4 import BeautifulSoup
import json
from urllib.request import urlopen

my_ip = json.load(urlopen('http://jsonip.com'))['ip']
print(my_ip)

my_ip = urlopen('http://ip.42.pl/raw').read() #bytes value
print(str(my_ip)) #transfer to string

#slow 
my_ip = json.load(urlopen('https://api.ipify.org/?format=json'))['ip']
print(my_ip)

