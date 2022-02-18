#code for cycling between colors, usefull in finding/fixing dead pixels
#fill in the setup and the code will do the rest

#import important libraries
import time, machine, neopixel, gc

#define what pins are what - setup
pin = 1                           #the gpio pin of the data to the strip
leds = 37                         # the # of leds
cycle_amount = 99                 #times to cycle before the code ends
sleep = 1                         #time between each change in color
#setup the strip
np = neopixel.NeoPixel(machine.Pin(pin), leds)

#fancy print statement
if sleep > 0:
    print("Sleep time is :", sleep)
else:
    print("Sleep time is", sleep,"of a second")

#main statement and end of documentation
for j in range(cycle_amount):
    print("Cycle",j + 1)                 #cycle number
    for i in range(leds):
        np[i] = (50 ,0 ,0)
    np.write()
    time.sleep(sleep)
    for i in range(leds):
        np[i] = (0 ,50 ,0)
    np.write()
    time.sleep(sleep)
    for i in range(leds):
        np[i] = (0 ,0 ,50)
    gc.collect()                 #garbage collect
    np.write()
    time.sleep(sleep)