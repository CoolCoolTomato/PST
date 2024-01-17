import base64


#  base85编码/解码
def base85_ed(s, mod):
    if mod == "e":
        s = s.encode('utf-8')
        return base64.b85encode(s)
    elif mod == "d":
        try:
            s = base64.b85decode(s)
        except Exception:
            return "格式不对QAQ"
        return s
    else:
        return "Error"


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


#  base32编码/解码
def base32_ed(s, mod):
    if mod == "e":
        s = s.encode('utf-8')
        return base64.b32encode(s)
    elif mod == "d":
        try:
            s = base64.b32decode(s)
        except Exception:
            return "格式不对QAQ"
        return s
    else:
        return "Error"


#  base16编码/解码
def base16_ed(s, mod):
    if mod == "e":
        s = s.encode('utf-8')
        return base64.b16encode(s)
    elif mod == "d":
        try:
            s = base64.b16decode(s)
        except Exception:
            return "格式不对QAQ"
        return s
    else:
        return "Error"

