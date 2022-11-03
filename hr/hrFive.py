if __name__ == '__main__':
    nm = []
    sc = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nm.append(name)
        sc.append(score)

    new_list = set(sc)
    new_list.remove(min(new_list))
    amt = (min(new_list))


//https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true