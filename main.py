# https://learn.adafruit.com/adafruit-rfm69hcw-and-rfm96-rfm95-rfm98-lora-packet-padio-breakouts/circuitpython-for-rfm9x-lora

import time
import sys
import struct

import python_artnet as Artnet

debug = True

dmxChannels = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18],[19,20,21],[22,23,24],[25,26,27]]

### ArtNet Config ###
artnetBindIp = "0.0.0.0"
artnetPort = 6454
artnetUniverse = 0
estacode = 0x7FF0
oemcode = 0xabcd

ipAddress = (127,0,0,1)
ipAddressString = '.'.join(map(str, ipAddress))  # Convert ipAddress tuple to string
macAddress = "AA:BB:CC:DD:EE:FF".split(":")

### ArtNet Setup ###
# Sets debug in Artnet module. I know it's janky; it works so I don't care ;) 
# (unless YOU know a better way, then please tell me or fix it :])
Artnet.debug = debug
# Creates Artnet socket on the selected IP and Port
artNet = Artnet.Artnet(artnetBindIp,artnetPort,ipAddressString,macAddress,OEMCODE=oemcode,ESTACODE=estacode)

# This is so we can keep track of if it's time to do something
now = time.monotonic()

while True:
    try:
        # Receives an ArtNet packet
        artNetPacket = artNet.readPacket()
        if artNetPacket is not None and artNetPacket.data is not None:
            # Checks to see if the current packet is for the specified DMX Universe
            if artNetPacket.universe == artnetUniverse:
                # Stores the packet data array
                dmxPacket = artNetPacket.data
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        break

# Close the various connections cleanly so nothing explodes :)
artNet.close()
sys.exit()