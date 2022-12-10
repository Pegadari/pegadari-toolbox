from insecticide import heartbeat

from time import sleep
last_pulse = 0
for i in range(50):
    sleep(0.5)
    last_pulse = heartbeat(5, last_pulse, i, "test")