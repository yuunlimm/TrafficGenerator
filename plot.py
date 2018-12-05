import subprocess
import matplotlib.pyplot as plt

time = []
serverEroor = []
ok = []
notFound = []

with open('data.txt', 'r') as iFile:
    PastTimeLine = iFile.next().split("\t")
    # for i, line in enumerate(iFile):
    #     pass
    # if i < 6:
    #     raise Exception("not enough data to plot")
    for j, line in enumerate(iFile, 1):
        # every one minute 
        if j % 6 == 0:
            currentTimeLine = line.split("\t")
            time.append(currentTimeLine[0])

            serverEroor.append((int(currentTimeLine[1]) - int(PastTimeLine[1])) / 60)
            ok.append((int(currentTimeLine[2]) - int(PastTimeLine[2])) / 60)
            notFound.append((int(currentTimeLine[3]) - int(PastTimeLine[3])) / 60)
            # update the past time for next time differnce.
            PastTimeLine = currentTimeLine


# plt.plot(time, serverEroor, time, ok, time, notFound)
plt.plot(time, serverEroor, 'r--', label = '500s')
plt.plot(time, ok, 'b--', label = '200s')
plt.plot(time, notFound, 'g--', label = '404s')

plt.xlabel('Time')
plt.ylabel('RTS(1-minute rate)')
plt.savefig('graph.png')
