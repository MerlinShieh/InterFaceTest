import hashlib
import json
import hmac

import configparser
config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')


def getSign(message, key=config.get('Country', 'Key')):
    key = bytes(key, encoding='utf8')
    message = json.dumps(message, separators=(',', ':'))
    message = bytes(message, encoding='utf8')
    mac = hmac.new(key, message, hashlib.sha1)
    mac.digest()

    return mac.hexdigest()

if __name__=="__main__":
    message = {"language": "zh_CN", "productId": "061410"}
    print(config.get('Country', 'Key'))
    print(getSign(message))