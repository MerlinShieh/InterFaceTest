import hashlib
import json
import hmac


def getSign(message, key='abc123'):
    key = bytes(key, encoding='utf8')

    message = json.dumps(message)
    message = bytes(message, encoding='utf8')
    mac = hmac.new(key, message, hashlib.sha1)
    mac.digest()

    return mac.hexdigest()
