#!/usr/bin/env python 3.7 9
# script by Lubomir Karlik 
#   

import gpiod as GPIO
from time import sleep
import threading

import config as CFG
import nastavenia
global COUNTER, uSIVIERT, FIRSTRUN
COUNTER=0
uSIVIERT=0
FIRSTRUN=1

def waitForInterrupt(line):
    global COUNTER

    while(True):
        event = line.event_read()
        COUNTER = COUNTER + 1

chip = GPIO.Chip(CFG.gpiochip)
line = chip.get_line(CFG.geiger_gpioline)
nastavenia.write_api = nastavenia.client.write_api(write_options=nastavenia.SYNCHRONOUS)

line.request(consumer="counter.py", type=GPIO.LINE_REQ_EV_FALLING_EDGE)

IntThread = threading.Thread(target=waitForInterrupt, args=(line,))
IntThread.start()

while True :
#
#    nastavenia.write_api = nastavenia.client.write_api(write_options=nastavenia.SYNCHRONOUS)
#
    COUNTER=int(COUNTER*60/CFG.geiger_measure_int)
    uSIVIERT= round(COUNTER/CFG.divider,3)
    if FIRSTRUN==1 :
        FIRSTRUN=0
        COUNTER=0
        sleep(CFG.geiger_measure_int)
    else:
        p = nastavenia.Point(CFG.point).tag("location",CFG.location ).tag("hostname",CFG.hostname).tag("IP",CFG.ipaddr).tag("MAC",CFG.macaddr).field("uSiviert", uSIVIERT).field("radiation", COUNTER)
        retval=11								# exit code for error writing to DB
#        print (p)
        nastavenia.write_api.write(bucket=CFG.bucket,org=CFG.org,record=p )
        COUNTER = 0
        sleep(CFG.geiger_measure_int)