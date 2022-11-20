x, y =  input().split()
nLine=int(x)
width=int(y)

topLines = int((nLine-1)/2)
mid = (width-1)/2

nMidSimbole=1
for i in range(topLines):
    print(('.|.'* nMidSimbole).center(width, '-'))
    nMidSimbole=nMidSimbole+2

print('WELCOME'.center(width,'-'))

for i in range(topLines):
    nMidSimbole = nMidSimbole - 2
    print(('.|.'* nMidSimbole).center(width, '-'))


