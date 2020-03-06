import lcmtypes
import lcm
import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
log = lcm.EventLog('D:\\changeline\\lcmlog-2019-06-25.11', "r")
f = open('speed11.txt', "w")
t = []
v = []
a = 0
event_msg = []
for event in log:
    msg = [event.eventnum, event.timestamp, log.tell()]
    event_msg.append(msg)
    if event.channel == "VEHICLE_STATUS":
        msg = lcmtypes.vehicle_status_t.decode(event.data)
        if a == 0:
            tmp = msg.utime
            a += 1
        t.append((msg.utime  - tmp)/1000000)
        f.write(str(msg.utime/1000000) + '\t')
        v.append(msg.speo)
        f.write(str(msg.speo) + '\n')


plt.plot(t, v, color='y', label='行驶速度', marker='.')
plt.legend(loc='best')
plt.title("行驶速度波动")
plt.xlabel('时间 （秒）')
plt.ylabel('行驶速度 （km/h）')
plt.show()
f.close