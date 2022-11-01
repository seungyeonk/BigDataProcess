from datetime import datetime
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

day = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
dict = dict()
fp = open(input_file)
for line in fp :
    line = line.strip()
    data = line.split(',')
    date = datetime.strptime(data[1], '%m/%d/%Y')
    data[1] = day[date.weekday()]
    data[2] = int(data[2])
    data[3] = int(data[3])
    key = (data[0], data[1])
    value = [data[2], data[3]]

    if key in dict:
        dict[key][0] += data[2]
        dict[key][1] += data[3]
    else:
        dict[key] = value
fp.close()
f = open(output_file, 'w')
for key, cnt in dict.items():
    f.write(key[0] + "," + key[1])
    f.write(" %d,%d\n" % (cnt[0], cnt[1]))
f.close()
