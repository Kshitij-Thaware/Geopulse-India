#Functions to calcuulate latest prices and percentage changes

def calculate_changes(data):
    processed = {}

    #GOLD
    gold_close = data['gold']['Close']
    processed['gold_price'] = gold_close.iloc[-1]
    processed['gold_change'] = (
        (gold_close.iloc[-1] - gold_close.iloc[-2]) / gold_close.iloc[-2]
    ) * 100

    #OIL
    oil_close = data['oil']['Close']
    processed['oil_price'] = oil_close.iloc[-1]
    processed['oil_change'] = (
        (oil_close.iloc[-1] - oil_close.iloc[-2]) / oil_close.iloc[-2]
    ) * 100

    #USD/INR
    currency_close = data['usd_inr']['Close']
    processed['usd_inr'] = currency_close.iloc[-1]
    processed['currency_change'] = (
        (currency_close.iloc[-1] - currency_close.iloc[-2]) / currency_close.iloc[-2]
    ) * 100

    
    #NIFTY
    nifty_close = data['nifty']['Close']
    processed['nifty_price'] = nifty_close.iloc[-1]
    processed['nifty_change'] = (
        (nifty_close.iloc[-1] - nifty_close.iloc[-2]) / nifty_close.iloc[-2]
    ) * 100

    return processed