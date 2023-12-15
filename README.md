# python_artnet
Easy-to-use and simple python receiver for Art-Net (that also implements device polling).

## Installaton
All you need to do is clone the repository and start using it!
``` bash
$ git clone https://github.com/sciencegey/python_artnet.git
$ cd python_artnet
$ python3 exampleReceiver.py
```

## Usage
All you need to do to start receiving data is import the module, start the listener, then check for received data whenever you want!
```python
import python_artnet as Artnet

# By default it will listen on 0.0.0.0 (all interfaces)
artNet = Artnet.Artnet()

# Fetch the latest packet we received.
artNetPacket = artNet.readPacket()
# And extract the DMX data from that packet.
dmxPacket = artNetPacket.data
# You'll also want to check that there *is* data in the packet;
# if there isn't then it returns None
# See the example for more information

# Close the listener nicely :)
artNet.close()
```

There are also plenty of arguments you can pass when you start the listner:

- **BINDIP** - Which IP address you want to *listen* on (usually a broadcast address). This is the only one you really ever need to change. *(Defaults to "" AKA 0.0.0.0 AKA all interfaces)*
- **PORT** - Which UDP port you want to listen on. Shouldn't need to ever 
change this. *(Defaults to 6454)*

<details>
<summary>The following are used for purely management purposes:</summary>

- **SYSIP** - What the IP address of your system is. Purely cosmetic and only used to identify the system to ArtNet controllers. *(Defaults to "10.10.10.1")*
- **MAC** - What the MAC address of your system is. Same as above. *(Defaults to ["AA","BB","CC","DD","EE","FF"])*
- **SWVER** - What version of Art-Net we're using. In this case, V1.4 *(Defaults to "14")*
- **SHORTNAME** and **LONGAME** - Used to see what devices are what on a controller. *(Shortname is truncated to 17 bytes long, longname is truncated to 63)*
- **OEMCODE** - What the Art-Net OEM code your device has. Only needs to be set if you have one. *(In hex)*
- **ESTACODE** - What the ESTA Manafacturer Code your device has. Only needs to be set if you have one. *(In hex)*
- **PORTTYPE** - Used to tell the controller what type of physical ports your device has. *(Defaults to [0x80,0x00,0x00,0x00])* *See the Art-Net documentation for more information*
- **REFRESH** - What the refresh rate (in Hz) of your device. *(Defaults to 44 (the max for DMX))*
- **DEBUG** - Used to turn on debug output. *(Defaults to False)*
</details>

Further information on how it all works can be found in the [Art-Net documentation](https://www.artisticlicence.com/WebSiteMaster/User%20Guides/art-net.pdf).
## License
This project is licensed under an MIT License (see the [LICENSE](LICENSE) file).