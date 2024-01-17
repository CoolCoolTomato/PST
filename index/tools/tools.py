import base64
import urllib.parse
import hashlib
import numpy as np


#  base64编码/解码
def base64_ed(s, mod):
    if mod == "e":
        s = s.encode('utf-8')
        return base64.b64encode(s)
    elif mod == "d":
        try:
            s = base64.b64decode(s)
        except Exception:
            return "格式不对QAQ"
        return s
    else:
        return "Error"


# url编码/解码
def url_ed(s, mod):
    if mod == "e":
        s = urllib.parse.quote(s)
        return s
    elif mod == "d":
        try:
            s = urllib.parse.unquote(s)
        except Exception:
            return "格式不对QAQ"
        return s
    else:
        return "Error"


#  md5加密
def md5_e(s):
    m = hashlib.md5()
    try:
        m.update(s.encode('utf-8'))
    except Exception:
        return "哪里出了点问题?"
    return m.hexdigest()


#  16进制和字符转换
def hex_ascii_c(s, mod):
    if mod == 'hta':
        try:
            s = base64.b16decode(s.upper())
            return str(s)[2:len(s)+2]
        except Exception:
            return "格式不对QAQ"
    elif mod == 'ath':
        s = s.encode().hex()
        return s
    else:
        return "Error"


# 希尔加密/解密
def hill_ed(s, mod_1, mod_2, key):
    if not s:
        return "请输入密文"
    if not key:
        return "请输入密钥"
    l = int(len(key) ** 0.5)
    if l ** 2 != len(key):
        return "请输入有效密钥"
    s = s.lower()
    key = key.lower()
    if len(s) % l == 0:
        s_w = len(s) // l
    else:
        s_w = len(s) // l + 1
    s_h = l
    ss = [[0 for _ in range(s_w)] for _ in range(s_h)]
    keys = [[0 for _ in range(l)] for _ in range(l)]
    if mod_2 == "0":
        for i in range(len(s)):
            x = i // l
            y = i % l
            ss[y][x] += (ord(s[i]) - 97)
        for i in range(len(key)):
            x = i // l
            y = i % l
            keys[y][x] += (ord(key[i]) - 97)
    elif mod_2 == "1":
        for i in range(len(s)):
            x = i // l
            y = i % l
            ss[y][x] += (ord(s[i]) - 96)
        for i in range(len(key)):
            x = i // l
            y = i % l
            keys[y][x] += (ord(key[i]) - 96)
    else:
        pass
    ss = np.array(ss)
    keys = np.array(keys)
    if mod_1 == "d":
        try:
            keys = np.linalg.inv(keys)
        except Exception:
            return "密钥不可逆QAQ"
    res = np.matmul(keys, ss)
    it = ""
    for i in range(s_w):
        for j in range(l):
            if mod_2 == "0":
                it += chr((int(res[j][i]) % 26) + 97)
            else:
                it += chr(((int(res[j][i]) - 1) % 26) + 97)
    return it


