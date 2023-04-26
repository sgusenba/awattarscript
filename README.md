# awattarscript
This project serves as playground to toggle shelly devices on/off in based no hourly prices. If the price is considered to be cheap (done by a simple threshold logic) the shelly is turned on otherwise it is turned off. The price information is coming from https://www.awattar.at/services/api.

It consists of 3 scripts:

GetMarketData.py
It fetches the market data via a rest call from https://www.awattar.at/services/api and stores it in a data.json.

FindCheapTime.py
This script takes the data from data.json and does check via threshold (see config.ini) if the price is below the threshold if yes the timespan is written to cheap.json.

DoTheWork.py
As the name suggests this script does all the work.
It fetches all IPs which are provided in the config.ini file. Then it checks if the actual time is within a cheap time. If yes it turns on the shelly (no problem if you do that several times, if the state equals the last the shelly simple does not change the state. If no it turns off the shelly.

proposed execution interval
GetMarketData.py - hourly

FindCheapTime.py - hourly

DoTheWork.py - every minute

