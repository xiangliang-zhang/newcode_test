def process_test(chs, index):
    res = ''
    times = 0
    while index < len(chs) and chs[index] != '}':
        if chs[index] == '{':
            str_test, end = process_test(chs, index + 1)
            res += getString(times, str_test)
            times = 0
            index = end + 1
        else:
            if '0' <= chs[index] <= '9':
                times = times * 10 + int(chs[index])
            if 'a' <= chs[index] <= 'z':
                res += chs[index]
            index += 1
    return res, index

def getString(times, base):
    res = ''
    for i in range(times):
        res += base
    return res

def decompress(str_input):
    return process_test(str_input, 0)[0]

print(decompress('3{a}25{b}'))