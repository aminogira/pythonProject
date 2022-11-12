nn = int(input())
line = input()
list = [int(x) for x in line.split(" ")]
print(list)
t = tuple(list)
print(hash(t))

tt = (1, 2)
print(hash(tt))
//3713081631934410656
if __name__ == '__main__':
    n = int(input())
    integer_list = tuple(map(int, input().split()))
    print(hash(integer_list))


