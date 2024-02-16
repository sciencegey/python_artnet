import time
import sys
# import python_artnet as Artnet
import os

sys.path.append("../")
import python_artnet.python_artnet as Artnet

# def get_eth0_ip():
#     try:
#         # Get the IP address of the eth0 interface
#         eth0_ip = str(os.system("ip -4 -o addr show eth0 | awk '{print $4}' | cut -d '/' -f 1 "))
#         return eth0_ip
#     except (KeyError, IndexError, OSError) as e:
#         print(f"Error getting eth0 IP: {e}")
#         exit

debug = False

# You can choose between setting your own IP or if you run this on a Pi getting a IP automatically form eth0
# artnetBindIp = str(get_eth0_ip())
# artnetBindIp = "10.0.0.4"
artnetBindIp = "127.0.0.1"

artnetUniverse = 0

### Art-Net Setup ###
# Creates Artnet socket on the selected IP and Port
artNet1 = Artnet.Artnet(artnetBindIp, DEBUG=debug)
artNet2 = Artnet.Artnet(artnetBindIp, DEBUG=debug)

while True:
    try:
        # Read latest ArtNet packet
        artNet1Packet = artNet1.readPacket()
        artNet2Packet = artNet2.readPacket()
        # Print out the universe of said packet
        if artNet1Packet is not None and artNet1Packet.data is not None:
            print("My univ: " + str(artNet1Packet.universe))
            print("Packet: ", str(artNet1Packet.data[:6]))
        
        if artNet2Packet is not None and artNet2Packet.data is not None:
            print("My univ: " + str(artNet2Packet.universe))
            print("Packet: ", str(artNet2Packet.data[:6]))
        
        # Slow down there young fella
        time.sleep(0.1)
    # Big red stop button just in case
    except KeyboardInterrupt:
        break
    # Give me that exceptions
    except Exception as e:
        print("Exception: {1}", e)

# Bro, close dat shit! It is over for today! No more Mario Kart 8 Deluxe
artNet1.close()
artNet2.close()
sys.exit()