#!/usr/bin/python
import sys
import usb.core
import usb.util
# decimal vendor and product values
a = [[0x1bcf,0x053a],[0x192f,0x0716]]
ID = 0
idVendor = a[ID][0]
idProduct = a[ID][1]

dev = usb.core.find(idVendor=idVendor, idProduct=idProduct)
# or, uncomment the next line to search instead by the hexidecimal equivalent
#dev = usb.core.find(idVendor=0x45e, idProduct=0x77d)
# first endpoint
interface = 1
endpoint = dev[0][(0,0)][0]
# if the OS kernel already claimed the device, which is most likely true
# thanks to http://stackoverflow.com/questions/8218683/pyusb-cannot-set-configuration
#if dev.is_kernel_driver_active(interface) is True:
  # tell the kernel to detach
#  dev.detach_kernel_driver(interface)
  # claim the device
#  usb.util.claim_interface(dev, interface)
collected = 0
attempts = 100
while collected < attempts :
    try:
        data = dev.read(endpoint.bEndpointAddress,endpoint.wMaxPacketSize)
        collected += 1
        print data
    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue
# release the device
#usb.util.release_interface(dev, interface)
# reattach the device to the OS kernel
#dev.attach_kernel_driver(interface)
