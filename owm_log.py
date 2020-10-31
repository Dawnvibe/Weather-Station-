# Importing the Open Weather Maps Measurements
# To our Python Modules
import pyowm
import time

# Creating the Thermographic symbol to our Celcius
degree_sign = u'\N{DEGREE SIGN}'

# Creating the main script
owm = pyowm.OWM ('IN HERE WE ARE PUTTING OUR API KEY PROVIDED BY OWM')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Larissa, GR')
weather = observation.weather
status = weather.detailed_status
#temperature = weather.temperature('celsius')
#wind_dict_in_miles_per_h = mgr.weather_at_place('Larissa, GR').wind(unit='miles_hour')
one_call = mgr.one_call(lat=39.643452, lon=22.413208)
temperature = one_call.current.temperature('celsius').get('temp')
wind = one_call.current.wind('miles_hour').get('speed', 0)
humidity = one_call.current.humidity

# Converting the Miles measurements to Kilometers of the wind speed
# Open Weather Maps uses the miles metric
# But in Greece we are using the Kilometers/hour metric system
def mphtokmh(wind):
    kmh = wind * 1.68
    return kmh

#print(status)
#print(f'Temperature in Larisa City...{temperature}{degree_sign}C')
#print(f'The WindSpeed is...{mphtokmh(wind):.2f}Km/h')
#print(f'The Humidity is...{humidity}%')

# Creating a Loop for the script to refresh every 30 seconds
# So we can refresh the frames of the GUI everytime we want
running = True

#loop forever
while running:

    try:
        #read the humidity and temperature
        status = weather.detailed_status
        temperature = one_call.current.temperature('celsius').get('temp')
        wind = one_call.current.wind('miles_hour').get('speed', 0)
        humidity = one_call.current.humidity
        
        if status is not None and temperature is not None and wind is not None and humidity is not None:

            #print the Satellite Measurements
            print(status)
            print(f'Temperature in Larisa City...{temperature}{degree_sign}C')
            print(f'The WindSpeed is...{mphtokmh(wind):.2f}Km/h')
            print(f'The Humidity is...{humidity}%')
            print('\n')
            #save the Satellite Measurements in .txt file
            file = open('/home/weatherstation/Επιφάνεια εργασίας/WeatherStation/satellite_log.txt', 'a+')
            file.write(status)
            file.write('\n')
            file.write(f'Temperature in Larisa City...{temperature}{degree_sign}C')
            file.write('\n')
            file.write(f'The WindSpeed is...{mphtokmh(wind):.2f}Km/h')
            file.write('\n')
            file.write(f'The Humidity is...{humidity}%')
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