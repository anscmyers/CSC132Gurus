import tkinter as tk
from tkinter import*
window = Tk()
from requests import get
import json
from pprint import pprint
from haversine import haversine

from pynput.keyboard import Key, Listener



stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'

my_lat= 32.532470
my_lon= (92.639060)
my_location = (my_lon,my_lat)

all_stations = get(stations).json()['items']

def find_closest():
    smallest= 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station ['weather_stn_lat']
        station_loc = (station_lon, station_lat)
        distance = haversine(my_location,station_loc)
        if distance < smallest:
            smallest = distance
            closest_station = station ['weather_stn_id']
    return closest_station

closest_stn = find_closest()
print(closest_stn)
'''
closest_stn = 965816

monroe = get('https://monroe.weatherstem.com/api').json()
print(monroe)
'''

weather= weather + str(closest_stn)

my_weather= get(weather).json()['items']
pprint(my_weather)

pprint('Ground_Temp')
tempF = ((my_weather[0]['ground_temp'])*(9/5)) + 32
pprint('humidity')
humidity_num=(my_weather[0]['humidity'])
pprint("wind_speed")
wind_num=(my_weather[0]['wind_speed'])
pprint("rainfall")
rain_num =(my_weather[0]['rainfall'])


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master=master
        pad=3
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom

if my_weather[0]['wind_speed'] < 5:
    pass
if (my_weather[0]['wind_speed'] >= 5) and (my_weather[0]['wind_speed']<15):
    pass
if my_weather[0]['wind_speed'] > 15:
    pass

l1 = Label(window, text="Temperature (F)", font=('Courier',25))
l1.grid(row=0, column=0, sticky=N+S+E+W)
l2 = Label(window, text="Humidity (%)", font=('Courier',25))
l2.grid(row=1, column=0, sticky=N+S+E+W)
l3 = Label(window, text="Wind Speed (mph)", font=('Courier',25))
l3.grid(row=2, column=0, sticky=N+S+E+W)
l4 = Label(window, text=humidity_num, font=('Courier',25))
l4.grid(row=1, column=1, sticky=N+S+E+W)
l5 = Label(window, text=tempF, font=('Courier',25))
l5.grid(row=0, column=1, sticky=N+S+E+W)
l6 = Label(window, text=wind_num, font=('Courier',25))
l6.grid(row=2, column=1, sticky=N+S+E+W)
l7 = Label(window, text='Rainfall (in)', font=('Courier',25))
l7.grid(row=3, column=0, sticky=N+S+E+W)
l8 = Label(window, text=rain_num, font=('Courier',25))
l8.grid(row=3, column=1, sticky=N+S+E+W)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_rowconfigure(3, weight=1)



app=FullScreenApp(window)
window.mainloop()
'''

#def on_press(key):
 #   print('{0} pressed'.format(key))

#def on_release(key):
#    if key == Key.q:

#    elif key == Key.w:
#        pass
#    elif key == Key.e:
#        pass
#    elif key == Key.esc:
#        # stop listener
#        return False
#with Listener(
#        on_press=on_press,
#        on_release=on_release) as listener:
#    listener.join()
'''






#window.mainloop()

    

