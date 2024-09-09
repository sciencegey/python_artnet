import time
import sys
sys.path.insert(0, '..')
from python_artnet import python_artnet as Artnet

debug = True

# What DMX channels we want to listen to
dmxChannels = [1,2,3,4,5,6]

### ArtNet Config ###
artnetBindIp = "0.0.0.0"
artnetUniverse = 0

### Art-Net Setup ###
# Sets debug in Art-Net module.
# Creates Artnet socket on the selected IP and Port
artNet = Artnet.Artnet(artnetBindIp, DEBUG=debug)

while True:
    try:
        # First get the latest Art-Net data
        artNetBuffer = artNet.readBuffer()
        # And make sure we actually got something
        if artNetBuffer is not None:
            # Get the packet from the buffer for the specific universe
            artNetPacket = artNetBuffer[artnetUniverse]
            # And make sure the packet has some data
            if artNetPacket.data is not None:
                # Stores the packet data array
                dmxPacket = artNetPacket.data
                sequenceNo = artNetPacket.sequence
                
                # Then print out the data from each channel
                print("Sequence no: ", sequenceNo)
                print("Received data: ", end="")
                for i in dmxChannels:
                    # Lists in python start at 0, so to access a specific DMX channel you have to subtract one
                    print(dmxPacket[i-1], end=" ")
                
                # Print a newline so things look nice :)
                print("")
                
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        break

# Close the various connections cleanly so nothing explodes :)
artNet.close()
sys.exit()