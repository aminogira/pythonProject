if __name__ == '__main__':
    lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lst.append([name, score])
    lst.sort(key=lambda row: (row[1]))
    min = -1
    foundSecond = False
    secondVal = 0
    secondLowest = []
    for nm, sc in lst:
        if min == -1:
            min = sc
        if foundSecond == False:
            if sc != min:
                foundSecond = True
                secondVal = sc
        if sc == secondVal:
            secondLowest.append(nm)
    secondLowest.sort()
    for n in secondLowest:
        print(n)

# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true
