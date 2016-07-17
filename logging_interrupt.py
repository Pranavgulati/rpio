from gpio_module import digitalReadWithInterrupt
import time

monitorThread8 = digitalReadWithInterrupt(8)
monitorThread10 = digitalReadWithInterrupt(10)

monitorThread8.start()
monitorThread10.start()
while 1:
	time.sleep(5)
	print("Main thread Running")
	monitorThread10.stop()
	time.sleep(5)
	monitorThread8.stop()
