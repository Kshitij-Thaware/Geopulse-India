# yfinance is used to fetch market data

import yfinance as yf


def fetch_market_data():
    tickers = {
        "gold": "GC=F",
        "oil": "CL=F",
        "usd_inr": "INR=X",
        "nifty": "^NSEI"
    }

    market_data = {}

    for name, symbol in tickers.items():

        data = yf.download(
            symbol,
            period = "2mo",
            interval = "1d"
        )

        market_data[name] = data

    return market_data