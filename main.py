from gpiozero import LED
from time import sleep

led = LED(17)
number = int(input(f'Type the number of times you want the LED to blink '))

while number > 0:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    number -=1
print("Blinking completes")
print(f'It blinked {number} times')