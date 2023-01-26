# write your code here!
import requests
import json


class CurrencyConverter:
    def __init__(self) -> None:
        self.owned_currency = input()
        self.interested_currency = ""
        self.amount_owned = 0
        self.cache = {}
        self.get_rates("usd")
        self.get_rates("eur")
        self.get_rates(self.owned_currency)

    def get_rates(self, new_rate) -> None:

        response = requests.get(
            url=f"http://www.floatrates.com/daily/{new_rate}.json"
        )
        self.cache.update(
            {
                f"{new_rate}": json.loads(response.text)
            }
        )

    def check_missing_rate(self, rate):
        try:
            print("Checking the cache...")
            self.cache[rate]
        except KeyError:
            print("Sorry, but it is not in the cache!")
            self.get_rates(rate)
        else:
            print("Oh! It is in the cache!")
        finally:
            print(f"""You received {self.convert_currency(
                self.owned_currency,
                self.interested_currency,
                self.amount_owned
            )} {rate.upper()}.""")

    def convert_currency(self, owned_currency, to_convert_currency, amount):
        rate = float(self.cache[owned_currency][to_convert_currency]['rate'])
        return round(amount * rate, 2)

    def main(self):
        while True:
            self.interested_currency = input()
            if self.interested_currency == "":
                break
            self.amount_owned = float(input())
            self.check_missing_rate(self.interested_currency)


if __name__ == '__main__':
    app = CurrencyConverter()
    app.main()
