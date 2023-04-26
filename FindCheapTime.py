import json
import configparser
from TimeStampConverter import TimestampConverter 

# Create an instance of the class
converter = TimestampConverter()

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

for key in data:
 starttime = float(key['start_timestamp'])
 endtme = float(key['end_timestamp'])
 marketprice = key['marketprice']
 if(float(marketprice)<=float(threshold)) :
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
  
  
