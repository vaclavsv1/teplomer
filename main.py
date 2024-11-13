from machine import Pin
import dht
import time

sensor = dht.DHT11(Pin(0))

while True:
    try:
        sensor.measure()
        temperature = sensor.temperature()  
        humidity = sensor.humidity()        

        print("Teplota: {:.1f}°C, Vlhkost: {:.1f}%".format(temperature, humidity))

    except OSError as e:
        print("Chyba při čtení z čidla:", e)

    time.sleep(5)