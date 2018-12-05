import sys
import time
import random
import urllib2

url = sys.argv[1]
rps = int(sys.argv[2])
jitter = float(sys.argv[3])

if jitter < 0:
    jitter = 0.1
elif jitter > 1:
    jitter = 1.0

minRate = int(rps * (1.0 - jitter))
maxRate = int(rps * (1.0 + jitter))
while True:
    actualRate = random.randint(minRate, maxRate)
    start = time.time()

    for i in range(actualRate):
        chance = random.randint(0, 100)
        try:
            if chance in range(0, 10):
                urllib2.urlopen(url + '/yuun')
            elif chance in range(10, 15):
                urllib2.urlopen(url + '/fail')
            else:
                urllib2.urlopen(url)
        except urllib2.URLError:
            continue

    time.sleep(1-(time.time()-start))