import json
import requests
from flask_babel import _
from hashlib import md5
import urllib
import random
from flask import current_app

appid = '20190905000332169'
secretKey = 'ebrdSdr1hxg0fNH9poSI'

def translate(text, source_language, dest_language):
    if 'MS_TRANSLATOR_KEY' not in current_app.config or not current_app.config['MS_TRANSLATOR_KEY']:
        return _('Error: the translate service is not configured.')
    salt = random.randint(32768,65535)
    sign = appid + text + str(salt) + secretKey
    sign = sign.encode('utf-8')
    m1 = md5(sign)
    r = requests.get('https://api.fanyi.baidu.com/api/trans/vip/translate?q={}&from={}&to={}&appid={}&salt={}&sign={}'.format(
                            text,  source_language, dest_language,appid,salt,sign))
    if r.json()['error_code'] != 52000:
        return _('Error : the translate service failed.{}'.format(r.json()['error_code']))
    return json.loads(r.json()['trans_result'])
