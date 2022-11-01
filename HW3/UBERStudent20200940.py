from datetime import datetime
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
days = ['MON', 'TUE', 'WED', 'THR', 'FRI', 'SAT', 'SUN']
d = dict()
fp = open(input_file)
for line in fp :
    line = line.strip()
    data = line.split(',')
    date = datetime.strptime(data[1], '%m/%d/%Y')
    data[1] = days[date.weekday()]
    data[2] = int(data[2])
    data[3] = int(data[3])
    uberKey = (data[0], data[1])
    uberValue = [data[2], data[3]]
    if uberKey in d:
        d[uberKey][0] += data[2]
        d[uberKey][1] += data[3]
    else:
        d[uberKey] = uberValue
fp.close()
f = open(output_file, 'w')
for key, count in d.items():
    f.write(key[0] + "," + key[1])
    f.write(" %d,%d\n" % (count[0], count[1]))
f.close()
