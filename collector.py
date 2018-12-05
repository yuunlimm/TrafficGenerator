import urllib2
import sys
import os.path
import time
from datetime import datetime

interval = 10.0
outputFile = 'data.txt'

if len(sys.argv) < 4:
    raise Exception("Not enough number of arguments passed")
if len(sys.argv) == 4:
    interval = float(sys.argv[3])
    address = sys.argv[1] + '/stats'

if os.path.isfile(outputFile):
    output = open(outputFile, 'r+')
    output.truncate(0)
else:
    output = open(outputFile, 'w')

while True:
    stats = urllib2.urlopen(address)
    line = stats.read().split("\n")

    for i in range(len(line)-1):
        digit = line[i].split(": ")
        if (i == 0):
            ts = int(digit[1])
            output.write(datetime.utcfromtimestamp(ts).strftime('%H:%M') + "\t")
        else:
            output.write(digit[1] + "\t")
            
    output.write("\n")
    time.sleep(interval)
