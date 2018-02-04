from pip._vendor import requests
from django.contrib.auth.models import User

def send_sms(mobile, msg, sender="mKUMAR"):
    authkey = '171556AX34siFxz599f01a7'
    url = 'https://control.msg91.com/api/sendhttp.php?authkey=' + authkey + '&mobiles='
    url += mobile
    url += '&message=' + msg + '&sender=' + sender + '&route=4&country=91'
    print(url)
    print(requests.request('GET', url))
