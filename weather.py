from pprint import pprint
import requests

r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Chennai&APPID=[%s]')
pprint(r.json())
th = r.json()
for x in range(15):
    print '-',
print "\nShowing Specific Details"
for x in range(15):
    print '-',
cur_w = th['main']['temp']
cur_w = cur_w - 273
print "\nCurrent Temperature: %s" %cur_w