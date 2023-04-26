from awattar import AwattarAPI
import json
import datetime
from TimeStampConverter import TimestampConverter 

awattar = AwattarAPI()

market_zone = "AT"
resolution = "PT15M"

market_data = awattar.get_market_data(market_zone, resolution)

data = market_data['data']


# Convert the dictionary to a JSON string
json_str = json.dumps(data, indent=4, sort_keys=True)


# Write the JSON string to a file
with open('data.json', 'w') as f:
    f.write(json_str)


# Create an instance of the class
converter = TimestampConverter()


# Iterate over the keys
for key in data:
 starttime = float(key['start_timestamp'])
 endtme = float(key['end_timestamp'])
 marketprice = key['marketprice']
 # Convert an epoch timestamp to a datetime string
 start_string = converter.epoch_to_datetime(starttime)
 end_string = converter.epoch_to_datetime(endtme)
 # Print the result
 print('von',start_string,' bis ',end_string, ' kosten ', marketprice)  # Output: 2021-04-23 09:15:40


# Iterate over the values
#for value in market_data.values():
  #  print(value)

# Iterate over the key-value pairs
#for key, value in market_data.items():
  #  print(key, value)

