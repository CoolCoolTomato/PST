import urllib.parse


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

