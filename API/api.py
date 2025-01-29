import requests
from datetime import datetime

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": "bitcoin,ethereum,litecoin",
    "vs_currencies": "usd,thb"
}

headers = {
    "User-Agent": "CryptoPriceFetcher/1.0 (https://yourwebsite.com)"
}

try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    
    data = response.json()

    btc_price_usd = data["bitcoin"]["usd"]
    eth_price_thb = data["ethereum"]["thb"]
    ltc_price_usd = data["litecoin"]["usd"]  

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    print(f"ข้อมูลล่าสุด ณ เวลา {current_time}")
    print(f"ราคาของ Bitcoin (BTC): ${btc_price_usd:.2f} USD")
    print(f"ราคาของ Ethereum (ETH): {eth_price_thb:.2f} บาท")
    print(f"ราคาของ Litecoin (LTC): ${ltc_price_usd:.2f} USD")

except requests.exceptions.RequestException as e:
    print(f"เกิดข้อผิดพลาดในการขอข้อมูลจาก API: {e}")
except ValueError:
    print("ไม่สามารถแปลงข้อมูล JSON ได้")
except KeyError as e:
    print(f"ข้อมูลไม่ครบถ้วน: {e}")
