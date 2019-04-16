import requests, random


class RouterService:
    """docstring for RouterController"""

    def __init__(self, ip, port=8080, user="root", pwd="admin"):
        self.url = "http://{}:{}".format(ip, port)
        self.auth = "luci_username={}&luci_password={}".format(user, pwd)
        self.session = requests.Session()

    def getStock(self):
        try:
            url = self.url + "/cgi-bin/luci/?" + self.auth
            response = self.session.post(url, allow_redirects=False, timeout=(3, 5))
            code = response.status_code
            self.stock = (
                response.headers["Location"]
                if "Location" in response.headers
                else "No Number"
            )
            return response.status_code
        except Exception as e:
            self.stock = "Connection Failed"
            return 500

    def getSignalQuality(self):
        try:
            cache = random.random()
            url = "{}{}?status=1&_={}{}&self.auth".format(
                self.url, self.stock, cache, self.auth
            )
            response = self.session.post(url, allow_redirects=False, timeout=(3, 5))
            json_data = response.json()
            quality = [
                json_data["wifinets"][0]["networks"][0]["quality"],
                json_data["wifinets"][1]["networks"][0]["quality"],
            ]
            return response.status_code, quality
        except Exception as e:
            return 500, "Connection Failed"
