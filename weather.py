from pprint import pprint
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Chennai&APPID=ffb1054510c074df76b0d02f3dd0fde4')
#pprint(r.json())
th = r.json()
cur_w = th['main']['temp']
cur_w = cur_w - 273
print cur_w