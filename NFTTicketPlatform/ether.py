import json
import requests

# from etherscan import Etherscan
# eth = Etherscan("HTUYSM4PWUIX7UWMMNBRSUHWBKKN1QIIR3")

def getEtherRate():
    url='https://api.etherscan.io/api?module=stats&action=ethprice&apikey=YourApiKeyToken'
    HTML = requests.get(url).json()
    print(HTML)
    etherrate = float(HTML['result']['ethusd'])
    print(etherrate)
    print(HTML['result']['ethusd'])
    return etherrate



def getUSDTW():
    r=requests.get('https://tw.rter.info/capi.php')
    currency=r.json()
    USDTWRate =float(currency['USDTWD']['Exrate'])
    print("USDTWRate:"+str(USDTWRate))
    return USDTWRate


