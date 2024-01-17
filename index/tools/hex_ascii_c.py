import base64


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


