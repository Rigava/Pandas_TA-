import pandas as pd
import pandas_ta as ta
import yfinance
import requests,json
from IPython.display import Markdown, display
import html

ticker = yfinance.Ticker("RELIANCE.NS")
df = ticker.history(period="1y")
adx=df.ta.adx()
rsi=df.ta.rsi()
macd=df.ta.macd()
df=pd.concat([df,adx,rsi,macd],axis=1)
last_row=df.iloc[-1]

webhook_url = "https://discord.com/api/webhooks/970262509963591731/dlo67rPlslfcW516HAQlhy80YYk7RAaxKyDmV7CLnjaodmA2ebfqxMJy6OmJMdGt8xxd"


if last_row['ADX_14'] >= 25:
    if last_row['DMP_14'] > last_row['DMN_14']:
        msg = display(
            Markdown(f"<text style=color:green> Strong Uptrend : The adx is  {last_row['ADX_14']:.2f}</text>"))
        print(msg)
        payload = {
            "username": "stock_alert",
            "content": msg
        }
        requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    if last_row['DMP_14'] < last_row['DMN_14']:
        msg = display(Markdown(f"<text style=color:red> Strong Downtrend : The adx is {last_row['ADX_14']:.2f}</text>"))
        print(msg)
        payload = {
            "username": "stock_alert",
            "content": msg
        }
        requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
if last_row['ADX_14'] < 25:
    msg = f"No trend : The adx is{last_row['ADX_14']}"
    print(msg)

    payload = {
        "username": "stock_alert",
        "content": msg
    }
    requests.post(webhook_url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})