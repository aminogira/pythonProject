
def wrap(string, max_width):

    out = [string[i:i + max_width] for i in range(0, len(string), max_width)]
    i = 1
    ans = out[0]
    while i < len(out):
        ans = ans + '\n' + out[i]
        i = i +1
    return ans






if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)