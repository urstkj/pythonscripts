import requests
import json
from time import sleep
i = 1
while True:
    otp = requests.get('https://crg.delhivery.com/otp/generate?phone=7014683236')
    otpstatus = json.loads(otp.content.decode('utf-8'))
    print(i)
    print(otpstatus['message'])
    sleep(1)
    i = i+1
