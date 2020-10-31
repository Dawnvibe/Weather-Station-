# Importing the sensor to Python modules
from w1thermsensor import W1ThermSensor
import time

# Writing the script
ds18b20 = W1ThermSensor()
ds18b20_temp = ds18b20.get_temperature()

#print("The temperature is %s celsius" % ds18b20_temp)

# Creating a Loop for the script to refresh every 30 seconds
# So we can refresh the frames of the GUI everytime we want
running = True

#loop forever
while running:

    try:
        #read the humidity and temperature
        ds18b20_temp = ds18b20.get_temperature()

        if ds18b20_temp is not None:

            #print humidity
            print('Temperature2={0:0.1f}*C\n' .format(ds18b20_temp))
            #save humidity in .txt file
            file = open('/home/weatherstation/Επιφάνεια εργασίας/WeatherStation/ds18b20_Indoors_log.txt', 'a+')
            file.write(f'Temperature2={ds18b20_temp:0.1f}*C\n' + '\n')
            time.sleep(60)
            
        else:
            print('Failed to get reading. Try again!')
            time.sleep(60)
            
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