import sys
import lcm

from lcmtypes import gps_imu_info_t

#from exlcm import example_t

#if len(sys.argv) < 2:
#    sys.stderr.write("usage: read-log <logfile>\n")
#    sys.exit(1)

log = lcm.EventLog("lcmlog-2019-04-28.04", "r")

for event in log:
    if event.channel == "GPS_DATA":
        msg = gps_imu_info_t.decode(event.data)

#        print("Message:")
        print("   longitude   = %s" % str(msg.longitude))
#        print("   position    = %s" % str(msg.position))
#        print("   orientation = %s" % str(msg.orientation))
#       print("   ranges: %s" % str(msg.ranges))
#        print("")
