import requests


URL = "https://api.coingecko.com/api/v3/simple/price"
PARAMS = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd",
    "include_24hr_change": "true",
    "include_market_cap": "true",
}

def format_price(coin, info):
    price  = info["usd"]
    change = info.get("usd_24h_change", 0)
    mcap   = info.get("usd_market_cap", 0)
    arrow  = "▲" if change > 0 else "▼"
    sign   = "+" if change > 0 else ""
    print(f"{coin.upper():12} ${price:>14,.2f}   "
          f"{arrow} {sign}{change:.2f}%   "
          f"mcap ${mcap/1e9:.1f}B")

def main():
    print(f"{'COIN':12} {'PRICE':>16}   {'24H':>9}   {'MARKET CAP':>14}")
    print("─" * 60)

    try:
        resp = requests.get(URL, params=PARAMS, timeout=10)

        if resp.status_code == 200:
            data = resp.json()
            for coin, info in data.items():
                format_price(coin, info)

        elif resp.status_code == 401:
            print("401 – check your API key")
        elif resp.status_code == 404:
            print("404 – endpoint not found, check URL")
        elif resp.status_code == 429:
            print("429 – rate limited, wait before retrying")
        else:
            print(f"Unexpected status: {resp.status_code}")

    except requests.exceptions.Timeout:
        print("Timed out after 10s – server too slow")
    except requests.exceptions.ConnectionError:
        print("Connection failed – check your internet")

if __name__ == "__main__":
    main()