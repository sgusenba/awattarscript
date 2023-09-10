import json
import configparser
import datetime
from ShellyControl import SheyllyControl
from TimeStampConverter import TimestampConverter 

# Create an instance of the class
converter = TimestampConverter()

shellycontrol = SheyllyControl()


# Open and load the JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

#loadthreshold
config = configparser.ConfigParser()
config.read('config.ini')
threshold = config.get('ischeap', 'threshold')


# Create a list of JSON objects from the items
cheap_list = []

#Iterate over the keys
now = datetime.datetime.now()

for key in data:
 starttime = float(key['start_timestamp'])
 endtme = float(key['end_timestamp'])
 marketprice = key['marketprice']
 if(float(marketprice)<=float(threshold)) :
  start = datetime.datetime.fromtimestamp(float(key['start_timestamp'])/1000)
  end = datetime.datetime.fromtimestamp(float(key['end_timestamp'])/1000)
  if(start <= now <= end) :
    print('is within range')
    shellycontrol.toggleState('on')
  else :
    shellycontrol.toggleState('off')
    print('shutting down shellys')
  cheap = {
     'starttime' : starttime,
     'endtime' : endtme,
     'marketprice':marketprice,
     'startstring':converter.epoch_to_datetime(starttime),
     'endstring': converter.epoch_to_datetime(endtme)
  }
  cheap_list.append(cheap)

# Convert the dictionary to a JSON string
json_str = json.dumps(cheap_list, indent=4, sort_keys=True)


# Write the JSON string to a file
with open('cheap.json', 'w') as f:
    f.write(json_str)
  
  
