def hex_utf8(s,  mod):
    if mod == "uth":
        res = []
        for i in s:
            res.append(hex(ord(i))[2:].zfill(4).upper() + '/')
        return ''.join(res)
    elif mod == "htu":
        res = []
        s = s.replace("/", "")
        for i in zip(*[iter(s)] * 4):
            res.append(chr(int(''.join(i), 16)))
        return ''.join(res)
    else:
        return "Error"

