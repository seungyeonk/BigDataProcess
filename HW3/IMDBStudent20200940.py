import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
d = dict()
fp = open(input_file)
for line in fp:
    line = line.strip()
    g = line.split('::')[2]
    genres = g.split('|')
    for genre in genres :
        if genre in d:
            d[genre] = d[genre] + 1
        else:
            d[genre] = 1
fp.close()
f = open(output_file, 'w')
for genre, count in d.items():
    f.write(genre + ' ' + str(count) + '\n')
f.close()