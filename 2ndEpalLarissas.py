# First started at Friday 01 November 2019
# Stopped 13 0f March 2019
# My best friend told me to
# Never stop until you are satisfied
# He also told me to K.I.S.S
# (Keep It Simple Stupid)
# Fist code is been scraped and shredded
# Second and last code (See Below)
# Started at 13 October 2020
# And been Delivered at 23 October 2020

# Importing Constants and Modules
from tkinter import *
from tkinter import Frame
from PIL import ImageTk,Image
import time

# Creating the main gui
root = Tk()
root.title("2ο ΕΠΑΛ Λαρισας...")
root.geometry('1024x768')
root.configure(background='powder blue')

# Importing the first frame
# With the 2nd EPAL Logo
frame1 = LabelFrame(root, text='Το Σχολειο Μας', bd=9)
my_img = ImageTk.PhotoImage(Image.open('/home/weatherstation/Επιφάνεια εργασίας/WeatherStation/2ο-ΕΠΑΛ-ΛΑΡΙΣΑΣ4.png'))
my_label = Label(image=my_img)
my_label.pack()
frame1.place(relx=0.35, rely=0.022, relheight=0.275)

# Creating the Clock Function
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day1 = time.strftime("%A")
    day2 = time.strftime("%d")
    month = time.strftime("%m")
    year = time.strftime("%Y")

    label1.config(text=hour + ":" + minute + ":" + second + "" + "")
    label1.after(1000, clock)
    label2.config(text=day1 + " " + " " + " " + day2 + " " + "/" + " " + month + " " + "/" + " " + year)

# Putting the clock inside a secondary frame
frame2 = LabelFrame(root, text='Ωρα & Ημερομηνια', bd=9)
label1 = Label(frame2, width="35", height="1", text="", bg="white", fg="black", font=(33))
label1.config(font=("Helvetica", 11), padx='3', pady='7')
label1.pack(side=LEFT)
label2 = Label(frame2, width="35", height="1", text="", bg="white", fg="black", font=(33))
label2.config(font=("Helvetica", 11), padx='3', pady='7')
label2.pack(side=RIGHT)
#frame2.pack(padx='7', ipadx='7', ipady='7', pady='7')
frame2.place(relx=0.233, rely=0.244, relheight=0.1, relwidth=0.508)

clock()
# Closing the entire Clock function

# Importing the 1st measurement from the DHT-22 Sensor
# It's going to measure the Temperature and the Humidity inside the Electronics Lab
def open_txt1():
    text_file1 = open("dht22_Indoors_log.txt", "r")
    text1 = text_file1.read()
    my_text1.insert(1.0, text1)
    text_file1.close()

# Importing the 2ndary measurement from the DS18B20 Sensor
# It's been produced by Maxim Intagrated Products Inc.
# Also it's more accurate than the DHT-22 (it gives +-0.5 Celcius)
# From -10 Celcius to +85 Celcius
def open_txt2():
    text_file2 = open("ds18b20_Indoors_log.txt", "r")
    text2 = text_file2.read()
    my_text2.insert(1.0, text2)
    text_file2.close()

# Creating the frames that are going to Host the measurements from the sensors
frame3 = LabelFrame(root, text='Εσωτερικοι Αισθητηρες', bd=9)
label3 = Label(frame3, text="DHT-22", bg="white", fg="black")
label3.config(font=("Helvetica", 11))
label3.pack()
my_text1 = Text(frame3, width=40, height=2, font=('Helvetica', 11), bg="white", fg="black")
my_text1.pack()
dht22_button = Button(frame3, text="Load DHT-22", command=open_txt1)
dht22_button.pack()

label4 = Label(frame3, text="Ds18b20", bg="white", fg="black")
label4.config(font=("Helvetica", 11))
label4.pack()
my_text2 = Text(frame3, width=40, height=1, font=('Helvetica', 11), bg="white", fg="black")
my_text2.pack()
ds18b20_button = Button(frame3, text="Load Ds18b20", command=open_txt2)
ds18b20_button.pack()
frame3.place(relx=0.033, rely=0.378, relheight=0.544, relwidth=0.275)

# Importing the BMP-180 Sensor measurements
# We are going to use it as the external Thermometer and Altitude meter
# By extending cables to the nearest window of the Lab
# the first choice was to use an ESP-8266 for the external measurements
# but 2 of the ESP's are D.O.A
def open_txt3():
    text_file3 = open("BMP180_Indoors_log.txt", "r")
    text3 = text_file3.read()
    my_text3.insert(1.0, text3)
    text_file3.close()

# Creating the Central Frame for the BMP-180
frame4 = LabelFrame(root, text='Εξωτερικοι Αισθητηρες', bd=9)
label5 = Label(frame4, text="BMP-180", bg="grey", fg="white")
label5.config(font=("Helvetica", 11))
label5.pack()
my_text3 = Text(frame4, width=40, height=5, font=('Helvetica', 11), bg="grey", fg="black")
my_text3.pack()
bmp180_button = Button(frame4, text="Load BMP-180", command=open_txt3)
bmp180_button.pack()
frame4.place(relx=0.35, rely=0.378, relheight=0.544, relwidth=0.275)

# And lastly we are using the Open Weather Maps for our Satellite Measurements
def open_txt4():
    text_file4 = open("satellite_log.txt", "r")
    text4 = text_file4.read()
    my_text4.insert(1.0, text4)
    text_file4.close()

# And the last frame for the OWM
frame5 = LabelFrame(root, text='Δορυφόρος', bd=9)
label6 = Label(frame5, text="Open Weather Maps", bg="black", fg="green")
label6.config(font=("Helvetica", 11))
label6.pack()
my_text4 = Text(frame5, width=40, height=5, font=('Helvetica', 11), bg="black", fg="green")
my_text4.pack()
owm_button = Button(frame5, text="Load Owm", command=open_txt4)
owm_button.pack()
frame5.place(relx=0.683, rely=0.378, relheight=0.544, relwidth=0.275)

# Closing everything to our Root GUI and making it to loop
root.mainloop()

# This code is been funded by Noesis S.A
# And belongs to the Greek Ministry Of Education
# with the Management for Secondary Education of Larissa
# lastly to the 2nd EPAL Larissas
# And all of it's parts
# This code is been developed by Dawnvibe
# For any infringement please contact me at dawnvibe2@gmail.com
# Or contact 2ndepallarissas@protonmail.com

# Inspired by Vasilis Tiles (chron.vas@outlook.com)