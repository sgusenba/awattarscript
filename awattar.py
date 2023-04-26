import requests

class AwattarAPI:
    def __init__(self):
        self.base_url = "https://api.awattar.at/v1/"

    def _make_request(self, endpoint, params=None):
        response = requests.get(self.base_url + endpoint, params=params)
        response.raise_for_status() # Raise an exception if the response is not ok
        return response.json()

    def get_market_data(self, market_zone="AT", resolution="PT15M"):
        params = {
            "marketzone": market_zone,
            "resolution": resolution
        }
        return self._make_request("marketdata", params=params)
