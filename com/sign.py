"""
这个是用来做签名了，如果不需要或者签名方式不对，重写这个方法就行

"""

import hashlib
import json
import hmac
import configparser

config = configparser.ConfigParser()
config.read('../config/config.ini', encoding='UTF-8')


def getSign(msg, key=config.get('sign', 'key')):
    key = bytes(key, encoding='utf8')
    mac = hmac.new(key, bytes(json.dumps(msg, separators=(',', ':')), encoding='utf8'), hashlib.sha1)
    mac.digest()
    return mac.hexdigest()


if __name__ == "__main__":
    message = {"language": "zh_CN", "productId": "061410"}
    print(getSign(message))
