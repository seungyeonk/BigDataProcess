import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

dict = dict()
fp = open(input_file)
for line in fp:
    line = line.strip()
    genre = line.split('::')[2]
    genres = genre.split('|')
    for genre in genres :
        if genre in dict:
            dict[genre] = dict[genre] + 1
        else:
            dict[genre] = 1
fp.close()
f = open(output_file, 'w')
for genre, count in dict.items():
    f.write(genre + ' ' + str(count) + '\n')
f.close()