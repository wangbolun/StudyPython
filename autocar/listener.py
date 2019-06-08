import lcm
from lcmtypes import gps_imu_info_t

def my_handler(channel, data):
    msg = gps_imu_info_t.decode(data)
#    print("Received message on channel \"%s\"" % channel)
    print("   longitude   = %s" % str(msg.longitude))
#    print("   position    = %s" % str(msg.position))
#    print("   orientation = %s" % str(msg.orientation))
#    print("   ranges: %s" % str(msg.ranges))
#    print("   name        = '%s'" % msg.name)
#    print("   enabled     = %s" % str(msg.enabled))
#    print("")

lc = lcm.LCM()
subscription = lc.subscribe("GPS_DATA", my_handler)


try:
    while True:
        lc.handle()
except KeyboardInterrupt:
    pass

#lc.unsubscribe(subscription)
