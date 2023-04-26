import requests
import configparser

class SheyllyControl:
 def toggleState(self,onOff):
    config = configparser.ConfigParser()
    config.read('config.ini')
    # Set the IP address and credentials of your Shelly Plug
    username = "your_username"
    password = "your_password"
    
    ips = config.get('shellyips', 'ips').split(",")
    for ip in ips:
        # Set the URL of the REST API endpoint
        url = f"http://{ip}/relay/0?turn={onOff}"

        # Send the HTTP request
        #response = requests.get(url, headers=headers)
        response = requests.get(url)
        # Check the response status code
        if response.status_code == 200:
            print(f"Shelly Plug is turned {onOff}")
        else:
            print("Error occurred while turning the Shelly Plug")
