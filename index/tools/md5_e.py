import hashlib


#  md5加密
def md5_e(s):
    m = hashlib.md5()
    try:
        m.update(s.encode('utf-8'))
    except Exception:
        return "哪里出了点问题?"
    return m.hexdigest()
