from microbit import *

mins = 0
secs = 0

def start():
    display.clear()
    for j in range(0, 5):
        for i in range(0, 5):
            display.set_pixel(i, j, 9)
            sleep(100)

start()
while mins < 25:
    if button_a.is_pressed():
        mins = 0
        secn = 0
        start()
    (y, x) = divmod(mins, 5)
    s = int((60 - secs) / 10)
    display.set_pixel(x, y, s)
    secs += 1
    if (secs > 59):
        secs = 0
        mins += 1
    sleep(1 * 1000)
while True:
    display.scroll("End.")
    sleep(5 * 1000)
