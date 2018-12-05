all = ''
counter = 0
wr = open('../sequences/all.txt', 'w')
with open('../sequences/His68Leufs.txt', 'r') as f:
    for line in f:
        line = line.strip(' ')
        wr.write(line.strip('\n'))
        # for i in range(0, line.strip('\n'))
        # all += line.strip('\n')