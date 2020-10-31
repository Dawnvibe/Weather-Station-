# Importing the Sensor to the Python Modules
import Adafruit_BMP.BMP085 as BMP085
import time

# Writing the basic script
sensor = BMP085.BMP085()
Temp = sensor.read_temperature()
Pressure = sensor.read_pressure()
Altitude = sensor.read_altitude()
Sealevel_Pressure = sensor.read_sealevel_pressure()

#print('Temp = {0:0.2f} *C'.format(sensor.read_temperature(), '\n'))
#print('Pressure = {0:1.0f} Pa'.format(sensor.read_pressure(), '\n'))
#print('Altitude = {0:0.2f} m'.format(sensor.read_altitude(), '\n'))
#print('Sealevel Pressure = {0:1.0f} Pa'.format(sensor.read_sealevel_pressure(), '\n'))

# Creating a Loop for the script to refresh every 30 seconds
# So we can refresh the frames of the GUI everytime we want
running = True

#loop forever
while running:

    try:
        #read the humidity and temperature
        sensor = BMP085.BMP085()
        Temp = sensor.read_temperature()
        Pressure = sensor.read_pressure()
        Altitude = sensor.read_altitude()
        Sealevel_Pressure = sensor.read_sealevel_pressure()

        if sensor is not None and Temp is not None and Pressure is not None and Altitude is not None and Sealevel_Pressure is not None:

            #print values
            print('Temp = {0:0.2f} *C\n'.format(sensor.read_temperature(), '\n'))
            print('Pressure = {0:1.0f} Pa\n'.format(sensor.read_pressure(), '\n'))
            print('Altitude = {0:0.2f} m\n'.format(sensor.read_altitude(), '\n'))
            print('Sealevel Pressure = {0:1.0f} Pa\n'.format(sensor.read_sealevel_pressure(), '\n'))
            print('\n')
            #save humidity in .txt file
            file = open('/home/weatherstation/Επιφάνεια εργασίας/WeatherStation/BMP180_Indoors_log.txt', 'a+')
            file.write('Temp = {0:0.2f} *C\n'.format(sensor.read_temperature(), '\n'))
            file.write('Pressure = {0:1.0f} Pa\n'.format(sensor.read_pressure(), '\n'))
            file.write('Altitude = {0:0.2f} m\n'.format(sensor.read_altitude(), '\n'))
            file.write('Sealevel Pressure = {0:1.0f} Pa\n'.format(sensor.read_sealevel_pressure(), '\n'))
            file.write('\n')
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