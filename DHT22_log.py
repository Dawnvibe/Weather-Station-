# Importing the sensor to the Python Modules
import Adafruit_DHT
import time

# Writing the basic script
DHT22Sensor = Adafruit_DHT.DHT22
DHTpin = 16
humidity, temperature = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)

# Creating a Loop for the script to refresh every 30 seconds
# So we can refresh the frames of the GUI everytime we want
running = True

# new .txt file created with header
file = open('/home/weatherstation/Επιφάνεια εργασίας/WeatherStation/dht22_Indoorslog.txt', 'a+')
file.write(f'Temp={temperature:0.1f}*C Humidity={humidity:0.1f}%' + '\n')

#loop forever
while running:

    try:
        #read the humidity and temperature
        humidity, temperature = Adafruit_DHT.read_retry(DHT22Sensor, DHTpin)

        if humidity is not None and temperature is not None:

            #print humidity
            print('Temp={0:0.1f}*C Humidity={1:0.1f}%' .format(temperature, humidity))
            #save humidity in .txt file
            file = open('/home/weatherstation/Επιφάνεια εργασίας/WeatherStation/dht22_Indoors_log.txt', 'a+')
            file.write(f'Temp={temperature:0.1f}*C\nHumidity={humidity:0.1f}%')
            time.sleep(30)

        else:
            print('Failed to get reading. Try again!')
            time.sleep(30)

    except KeyboardInterrupt:
        print ('Program stopped')
        running = False
        file.close()
# Closing the script

# This code is been funded by Noesis S.A
# And belongs to the Greek Ministry Of Education
# with the Management for Secondary Education of Larissa
# lastly to the 2nd EPAL Larissas
# And all of it's parts
# This code is been developed by Dawnvibe
# For any infringement please contact me at dawnvibe2@gmail.com
# Or contact 2ndepallarissas@protonmail.com

# Inspired by Vasilis Tiles (chron.vas@outlook.com)