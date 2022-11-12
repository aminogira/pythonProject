if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    m1, m2, m3 = student_marks[query_name]
    avg = (m1 + m2 + m3) / 3

    print("{:.2f}".format(avg))
