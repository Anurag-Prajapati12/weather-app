#Weather App
from tkinter import *
from PIL import ImageTk, Image
import requests
import json


root=Tk()
root.title("Weather App")
root.config(bg="#009999")


def unit():
    global temp
    temp=var.get()
    print(temp)
  
def weather():
    city=entry_city.get()
    try:
        api_requests=requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=ad692e548e95fcd217e74e5e0aaccac0")
        data=api_requests.json()
        print(data)
    except Exception:
        print("Error...")

    global temp
    temp=var.get()    
    if temp=='K':
        temprature=data["main"]["temp"]
        label_tempratureout.config(text=str(temprature)+"K")
    if temp=='°C':
        temprature=data["main"]["temp"]
        new_temp=temprature-273.15
        t=round(new_temp,2)
        label_tempratureout.config(text=str(t)+'°C')
    if temp=='F':
        temprature=data["main"]["temp"]
        new_temp=(temprature-273.15)*9/5+32
        t=round(new_temp,2)
        label_tempratureout.config(text=str(t)+'F')

    humidity=data["main"]["humidity"]
    label_humidityout.config(text=humidity)

    pressure=data["main"]["pressure"]
    label_pressureout.config(text=pressure)

    wind=data["wind"]["speed"]
    label_windout.config(text=wind)

    condition=data["weather"][0]["main"]
    label_conditionout.config(text=condition)
    
def clear():
    entry_city.delete(0,END)
    label_tempratureout.config(text="")
    label_humidityout.config(text="")
    label_pressureout.config(text="")
    label_windout.config(text="")
    label_conditionout.config(text="")
    

#cretaing wigdtes
label_heading=Label(root,text="WEATHER APP",height=3,width=25,font=(1),bd=1,relief="solid",bg="#FF6666")
label_city=Label(root,text="City =>",font=(10),bd=1,relief="solid",bg="#CCFF99",padx=10,pady=5)
label_temprature=Label(root,text="Temprature =>",font=(10),bd=1,relief="solid",bg="#CCFF99",padx=10,pady=5)
label_humidity=Label(root,text="Humidity =>",font=(10),bd=1,relief="solid",bg="#CCFF99",padx=10,pady=5)
label_pressure=Label(root,text="Pressure =>",font=(10),bd=1,relief="solid",bg="#CCFF99",padx=10,pady=5)
label_wind=Label(root,text="Wind speed =>",font=(10),bd=1,relief="solid",bg="#CCFF99",padx=10,pady=5)
label_tempratureout=Label(root,bg="#009999",font=(10))
label_humidityout=Label(root,bg="#009999",font=(10))
label_pressureout=Label(root,bg="#009999",font=(10))
label_windout=Label(root,bg="#009999",font=(10))
label_condition=Label(root,text="Condition =>",font=(10),bd=1,relief="solid",bg="#CCFF99",padx=10,pady=5)
label_conditionout=Label(root,font=(10),bg="#009999")

entry_city=Entry(root,font=(10),bg="#C0C0C0")
entry_city.focus()


button_unit=Button(root,text="Set Temp. unit",font=(10),command=unit,bg="#66B2FF")
button_weather=Button(root,text="Get Weather",font=(1),command=weather,bg="#66B2FF")
button_clear=Button(root,text="Clear",font=(1),command=clear,bg="#66B2FF")


var=StringVar()
var.set("K")
drop=OptionMenu(root,var,"°C","F","K")
drop.config(font=(3))
drop.config(bg="#009999")




#placing widgets
label_heading.grid(row=0,column=0,columnspan=3,padx=50,pady=10)
label_city.grid(row=1,column=0,padx=30,pady=30)
entry_city.grid(row=1,column=1,padx=30,pady=30)
button_unit.grid(row=1,column=2)
drop.grid(row=1,column=3)
label_temprature.grid(row=3,column=0,padx=20,pady=10)
label_humidity.grid(row=4,column=0,padx=20,pady=10)
label_pressure.grid(row=5,column=0,padx=20,pady=10)
label_wind.grid(row=6,column=0,padx=20,pady=10)
label_tempratureout.grid(row=3,column=1,padx=20,pady=10)
label_humidityout.grid(row=4,column=1,padx=20,pady=10)
label_pressureout.grid(row=5,column=1,padx=20,pady=10)
label_windout.grid(row=6,column=1,padx=20,pady=10)
button_weather.grid(row=2,column=1)
button_clear.grid(row=2,column=2)
label_condition.grid(row=7,column=0,padx=20,pady=10)
label_conditionout.grid(row=7,column=1,padx=20,pady=10)


root.mainloop()
