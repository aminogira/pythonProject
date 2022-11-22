def print_rangoli(size):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    al = alf[:size][::-1]
    lines=size*2-1
    width=lines*2-1
    nCha=0
    toNxtN=1
    for l in range(lines):
        nCha=nCha+toNxtN
        if(nCha>=len(al)): toNxtN=-1
        lineCharSet=al[:nCha] + al[::-1][(len(al)-nCha+1):]
        processedLineCharSet='-'.join(lineCharSet[i:i + 1] for i in range(0, len(lineCharSet), 1))
        print(processedLineCharSet.center(width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)





# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----


# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------