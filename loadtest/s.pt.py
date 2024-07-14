from locust import HttpUser, task, between
from Rail import RailUrl


class RailTest(HttpUser, RailUrl):
    host = "https://apirail.flytoday.ir"

    # wait_time = between(1, 5)

    @task
    def search__test(self):
        res = self.client.post(RailTest.search_url,
                               json=RailTest.search_payload,
                               headers=RailTest.search_headers)

        if res.status_code != 200:
            print(res.status_code, end="")
            print(res.content)
        else:
            None

    @task
    def train_price__test(self):
        train_price = []
        res = self.client.get(RailTest.train_price_url,
                              headers=RailTest.train_price_header)
        if res.status_code != 200:
            print(res.status_code, end="")
            print(res.content)
        else:
            None

    @task
    def search_summry__test(self):
        search_summry = []
        res = self.client.post(RailTest.search_summry_url,
                               json=RailTest.search_summry_payload,
                               headers=RailTest.search_summry_header)
        if res.status_code != 200:
            print(res.status_code, end="")
            print(res.content)
        else:
            None

    # def revalidate__test(self):
    #     pass

# ------------------------------------------------------------------------------------------------
from datetime import datetime


class RailUrl:

    search_movedate = datetime.now().strftime("%Y-%m-%d")

    # Get
    train_price_url = "/api/rails/train-price/v1?fromStation=1&amp;toStation=161"
    train_price_header = {
        'Key': 'Zmx5VG9kYXktMjAyMjEyMzQ1Ng==',
        'User-Agent': 'QATeam',
        'Content-Type': 'application/json'
    }

    search_summry_url = "/api/rails/search/summary/v1"
    search_summry_payload = [
        {
            "fromStation": 1,
            "toStation": 161,
            "moveDate": search_movedate,
            "carInclude": False,
            "sexCode": 3
        }
    ]
    search_summry_header = {
        'Key': 'Zmx5VG9kYXktMjAyMjEyMzQ1Ng==',
        'User-Agent': 'QATeam',
        'Content-Type': 'application/json'
    }

    search_url = "/api/rails/search/v1"

    search_payload = {

        "tripType": "OneWay",
        "isRoundTrip": False,
        "count": 0,
        "offset": 0,
        "queries": [
            {
                "fromStation": 1,
                "toStation": 191,
                "moveDate": search_movedate,
                "carInclude": False,
                "sexCode": 3,
                "compartmentCapacity": 4,
                "passengerCount": 1,
                "isExclusive": False,
                "tarrif": 1
            }
        ]
    }

    search_headers = {
        'Key': 'Zmx5VG9kYXktMjAyMjEyMzQ1Ng==',
        'User-Agent': 'QATeam',
        'Content-Type': 'application/json'
    }

    revalidate_url = "/api/rails/search/v1"
    revalidate_payload = {}
    revalidate_header = {}
