def count_substring(string, sub_string):
    count = 0
    ii = 0
    ind=-1
    while ii < (len(string) - len(sub_string)):

        try:
            ind = string.index(sub_string, ii)
        except:
            ii=len(string)
            ind=-1

        if ind > -1:
            count = count + 1
            ii = ind + 1
        else:
            ii = ii + 1
    return count


if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    string = 'I am an Indian, by birth.'
    sub_string = 'Birth'
    count = count_substring(string, sub_string)
    print(count)


# I am an Indian, by birth.
# Birth