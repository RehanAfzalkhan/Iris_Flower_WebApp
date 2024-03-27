# linear regression 21/03/2023(without Numpy,torch,tensorflow,etc..)
#least square method
import csv
import os
import json

import requests


class AlphaVantage:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = "https://www.alphavantage.co/query"

    def get_data(self, symbol, interval="monthly"):
        pararms = {"function": "WTI", "symbol": symbol, "apikey": self.api_key}
        # make a request to the API
        response = requests.get(self.base_url, pararms)

        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")
            return None


def save_data(fetched_data, symbol, directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

    filepath = f"{directory}/{symbol}_data.csv"
    with open(filepath, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "price"])
        for item in fetched_data["data"]:
            writer.writerow([item["date"], item["value"]])
        print(f"Data saved for {symbol}")


apikey = "YOUR_API_KEY"
symbols = ["WTI", "BRENT"]
interval = "daily"
directory = "data"

alpha_vantage = AlphaVantage(api_key=apikey)
for symbol in symbols:
    fetched_data = alpha_vantage.get_data(symbol, interval)
    save_data(fetched_data, symbol, directory)
