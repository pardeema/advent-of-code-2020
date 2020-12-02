FILE='input.txt'


pt1=0
pt2=0
with open(FILE, 'r') as f:
    for line in f:
        policy, pw = line.split(':')
        num_policy, char_policy = policy.split()
        num_min, num_max = num_policy.split('-')
        num_min = int(num_min.strip())
        num_max = int(num_max.strip())
        pw=pw.strip()
        char_policy=char_policy.strip()
        if pw.count(char_policy) >= num_min and pw.count(char_policy) <= num_max:
            #Increment valid PW
            pt1+=1

        #Code reuse, but rename for pt2 - subtract 1 to index to 0
        pos1 = num_min-1
        pos2 = num_max-1
        logic1 = not pw[pos1] == char_policy and pw[pos2] == char_policy
        logic2 = pw[pos1] == char_policy and not pw[pos2] == char_policy
        if logic1 or logic2:
            pt2+=1

print("Pt 1: {}".format(pt1))
print("Pt 2: {}".format(pt2))


