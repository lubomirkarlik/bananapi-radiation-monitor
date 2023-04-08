#!/usr/bin/env python 3.7 9
# script by Lubomir Karlik 
#   

from influxdb_client import WritePrecision, InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
import socket
import subprocess
import config as CFG
import uuid
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('localhost',8086))

if result > 0:
    # InfluxDB is not running   
    sys.exit(1)
else:
#
    sock.close()


client = InfluxDBClient(url=CFG.url, token=CFG.token, org=CFG.org, debug=False)
query_api = client.query_api()
  
def getNetworkIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    s.connect(('<broadcast>', 0))
    return s.getsockname()[0]
CFG.ipaddr= (getNetworkIp())

def get_mac_address(ip_address):
    arp_command = ['arp', '-n', ip_address]
    output = subprocess.check_output(("arp", "-a")).decode()
    mac_address = output.split()[3]
    return mac_address

s = "%012x" % uuid.getnode()
CFG.macaddr = s[0:2]+":"+s[2:4]+":"+s[4:6]+":"+s[6:8]+":"+s[8:10]+":"+s[10:12]
