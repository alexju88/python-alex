#from bs4 import BeautifulSoup
from urllib.request import urlopen

my_ip = load(urlopen('http://jsonip.com'))['ip']
print(my_ip)

my_ip = urlopen('http://ip.42.pl/raw').read() #bytes value
print(str(my_ip)) #transfer to string

#slow 
my_ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
print(my_ip)

