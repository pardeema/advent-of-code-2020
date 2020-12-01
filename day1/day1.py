FILE = 'input.txt'

with open(FILE, 'r') as f:
    l=f.read().split('\n')
    #quick cleanup
    l = [i for i in l if i !='']

for i in range(len(l)):
    for j in range(i+1, len(l)):
        a = int(l[i])
        b = int(l[j])
        if a + b == 2020:
            print("Part 1: {}".format(a*b))
            break

LENGTH = len(l)

for i in range(LENGTH):
    for j in range(i+1, LENGTH):
        for k in range (j+1, LENGTH):
            a = int(l[i])
            b = int(l[j])
            c = int(l[k])
            if a + b + c == 2020:
                print("Part 2: {}".format(a*b*c))
                break
