import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
class PeristalticPump:
    def __init__(self,pin_en,pin_dir,pin_pul):
        GPIO.setup([pin_en,pin_dir,pin_pul],GPIO.OUT,initial=0)
        self.pin_en=pin_en
        self.pin_dir=pin_dir
        self.pin_pul=pin_pul
	GPIO.output(self.pin_en,GPIO.LOW)
	GPIO.output(self.pin_dir,GPIO.HIGH)
    def burst(self,num):
	for i in range(0,round((200/6)*num)):
            GPIO.output(self.pin_pul,GPIO.HIGH)
            time.sleep(0.1)
            GPIO.output(self.pin_pul,GPIO.LOW)
            time.sleep(0.1)


