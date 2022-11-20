import pandas as pd
import requests
import json
from urllib.request import urlopen

API_KEY = 'AIzaSyBl1Baq99DdgTQQ_yrfwrT_DmB3jAW8Qmw'


url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

city = data.get('city')





##location needs to be the google search, ie 'neurologists near me'

def getDocs(location):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # query = location

    r = requests.get(url + 'query=' + location +
                     '&key=' + API_KEY)

    x = r.json()
    y = x['results']

    hospitalNames = []
    hospitalAddress = []
    for i in range(len(y)):
        hospitalNames.append((y[i]['name']))
        hospitalAddress.append(y[i]['formatted_address'])
        if (i > 7):
            break

    # link for the static map
    link = getMap(hospitalAddress)

    data = pd.DataFrame({'Names': [],
                         'Address': []
                         })
    i = 0
    for name in hospitalNames:
        data.loc[i] = [hospitalNames[i], hospitalAddress[i]]
        i = i + 1

    return (data)


def getMap(addresses):
    url = 'https://maps.googleapis.com/maps/api/staticmap?center=' + city + '&zoom=11&size=1200x1200&markers=color:red'
    for i in addresses:
        url = url + '|' + i
    r = requests.get(url + '&key=' + API_KEY)
    return (url + '&key=' + API_KEY)
