from microbit import *

minutes_to_go = 30

while True:
    for i in range(0, 2):
        display.scroll(">>> {} mins to go".format(minutes_to_go))
        sleep(1000)
    minutes_to_go -= 1
    sleep(59 * 1000)

