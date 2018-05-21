import psutil
from socket import *


class Network:

    def Host(self):
        host = psutil.net_io_counters(pernic=True)
        return host

    def Ethernet(self):
        host0 = self.Host()
        host0 = host0['Ethernet']
        return host0[0], host0[1]

    def WiFi(self):
        host1 = self.Host()
        host1 = host1['Wi-Fi']
        return host1[0], host1[1]


class LiveCon:

    def Speed(self):
        uspeed0, dspeed0 = Network().Ethernet()
        uspeed1, dspeed1 = Network().WiFi()

        if dspeed1 is 0 and dspeed0 is 0:
            return 0
        elif dspeed0 is 0:
            return dspeed1, uspeed1
        else:
            return dspeed0, uspeed0

    def connSpeed(self):
        UpSpeed, DownSpeed = self.Speed()
        return UpSpeed//8, DownSpeed//8


up, down = 0, 0
for i in range(0,1):
    u, d = LiveCon().connSpeed()
    print((u-up), (d-down))
    up, down = u, d







