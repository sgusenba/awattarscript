import configparser
import json
import datetime
from ShellyControl import SheyllyControl

config = configparser.ConfigParser()
config.read('config.ini')


shellycontrol = SheyllyControl()

# Open and load the JSON file
with open('cheap.json', 'r') as f:
    cheap = json.load(f)

# Get the current time

now = datetime.datetime.now()

for key in cheap:
 starttime = datetime.datetime.fromtimestamp(float(key['starttime'])/1000)
 endtme = datetime.datetime.fromtimestamp(float(key['endtime'])/1000)
 if(starttime <= now <= endtme) :
    print('is within range')
    shellycontrol.toggleState('on')
 else :
    shellycontrol.toggleState('off')
    print('shutting down shellys')
    


