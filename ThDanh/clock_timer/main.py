from distutils import command
from tkinter import *
import time
from playsound import playsound
from datetime import date, datetime


# use Tkinter GUI
root = Tk()
root.geometry('400x300')
root.resizable(0,0)
root.config(bg='blanched almond')
root.title('Clock Timer')

curr_date =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_date.place(x=120 , y=60)

# Datetime Module
def date_today():
  today = date.today().strftime("%B %d, %Y")
  curr_date.config(text = today)
  curr_date.after(1000,date_today)

date_today()

Label(root, text = "iWatch", font = 'arial 20 bold', bg = 'papaya whip').pack()
Label(root, font ='arial 15 bold', text = 'The Time Now :', bg = 'papaya whip').place(x=40 ,y=100)

curr_time =Label(root, font ='arial 15 bold', text = '', fg = 'gray25' ,bg ='papaya whip')
curr_time.place(x=200 , y=100)

def clock():
  clock_time = time.strftime('%H:%M:%S %p')
  curr_time.config(text = clock_time)
  curr_time.after(1000,clock)

clock()


# code to set countdown timer
secs = StringVar()
Entry(root, textvariable= secs, width=2, font='arial 12').place(x=260,y=155)
secs.set('00')

mins = StringVar()
Entry(root, textvariable= mins, width=2, font='arial 12').place(x=235,y=155)
mins.set('00')

hours = StringVar()
Entry(root, textvariable= hours, width=2, font='arial 12').place(x=210,y=155)
hours.set('00')


def countdown():
  times = int(hours.get())*3600 + int(mins.get())*60 + int(secs.get())
  while times > -1:
    minute,second = (times // 60 , times % 60)

    hour = 0
    if minute > 60:
      hour , minute = (minute // 60 , minute % 60)

    secs.set(second)
    mins.set(minute)
    hours.set(hour)

    root.update()
    time.sleep(1)

    if(times == 0):
      playsound('sounds/Military_Countdown_Sound.mp3')
      secs.set('00')
      mins.set('00')
      hours.set('00')
    
    times -= 1

Label(root, font='arial 15 bold', text = 'Set Countdown:', bg='papaya whip').place(x=40,y=150)
Button(root, text='START', fg = "blue", bd='5', command=countdown, bg = 'antique white', font = 'arial 10 bold').place(x=320, y=150)

# code to set alarm clock
mins1 = StringVar()
Entry(root, textvariable= mins1, width=2, font='arial 12').place(x=235,y=205)
mins1.set('00')

hours1 = StringVar()
Entry(root, textvariable= hours1, width=2, font='arial 12').place(x=210,y=205)
hours1.set('00')

nowHour = StringVar()
nowMin = StringVar()

def alarm():
  alarmTimer = int(hours1.get())*3600 + int(mins1.get())*60
  while True:
    localtime = time.localtime(time.time())
    nowHour.set(localtime.tm_hour)
    nowMin.set(localtime.tm_min)
    
    nowTimer = int(nowHour.get())*3600 + int(nowMin.get())*60

    root.update()
    time.sleep(1)
    if(nowTimer == alarmTimer):
      #print("Wake Up!!!")
      playsound('sounds/Loud_Alarm_iPhone_Shape_Of_You.mp3')
      mins1.set('00')
      hours1.set('00')
      break

Label(root, font='arial 15 bold', text = 'Set Alarm Timer:', bg='papaya whip').place(x=40,y=200)
Button(root, text='ALARM', fg = "blue", bd='5', command=alarm, bg = 'antique white', font = 'arial 10 bold').place(x=320, y=200)

root.mainloop()