def print_rangoli(size):
    print('-'*50)
    alf = 'abcdefghijklmnopqrstuvwxyz'
    al = alf[:size][::-1]

    width=(size*2-1)*2-1
    print(width)
    for a in al:
        print(a)




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