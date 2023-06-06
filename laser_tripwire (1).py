from gpiozero import LightSensor, Buzzer
from time import sleep
# alter if using a different pin
ldr = LightSensor(4)
# alter if using a different pin
buzzer = Buzzer(17) 
while True:
    sleep(0.1)
    if ldr.value < 0.8:  # adjust this to make the circuit more or less sensitive
        buzzer.on()
        # uncomment the next line to have the alarm trigger for 30 seconds.
        # sleep(30) 
    else:
        buzzer.off()
