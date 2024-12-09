from gpiozero import Servo
from time import sleep

#50Hz
#typical for SG90 servos.
servo = Servo(17, min_pulse_width=1/1000, max_pulse_width=2/1000, frame_width=20/1000)

def _open():
    servo.min()
    sleep(5)

def _close():
    servo.max()
    sleep(1)


if __name__ == "__main__":
    _open()
    #_close()