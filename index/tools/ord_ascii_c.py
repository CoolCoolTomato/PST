#  16进制和字符转换
def ord_ascii_c(s, mod):
    if mod == 'ota':
        try:
            res = ""
            s = s.split("/")
            for i in s:
                res += str(chr(int(i)))
            return res
        except Exception:
            return "格式不对QAQ"
    elif mod == 'ato':
        try:
            res = ""
            for x in s:
                res += (str(ord(x)) + "/")
            return res
        except Exception:
            return "格式不对QAQ"
    else:
        return "Error"


print(ord_ascii_c("97/98/99/100", "ota"))
