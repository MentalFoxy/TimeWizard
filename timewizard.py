import tkinter as tk
from datetime import datetime, timedelta

# initialize alarm_time with a default value
alarm_time = None

def time():
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%A, %d %B %Y")
    clock.config(text = current_time)
    date_label.config(text = current_date)
    if alarm_time:
        if current_time == alarm_time:
            alarm_label.config(text = "Alarm!! Wake Up")
    clock.after(1000, time)

def set_alarm():
    global alarm_time
    alarm_time = alarm_entry.get()
    alarm_time = alarm_time.strip()
    alarm_label.config(text = "Alarm set for " + alarm_time)

root = tk.Tk()
root.title("Digital Clock")

clock = tk.Label(root, font= ("calibri", 40, "bold"),
             background = "purple",
             foreground = "white")

clock.pack(anchor = "center", side = 'top')

date_label = tk.Label(root, font = ("calibri", 20, "bold"),
                      background = "purple",
                      foreground = "white")
date_label.pack(anchor = "center", side = 'bottom')

alarm_label = tk.Label(root, font = ("calibri", 20, "bold"),
                      background = "purple",
                      foreground = "white")
alarm_label.pack()

alarm_entry = tk.Entry(root, font = ("calibri", 20, "bold"),
                      background = "white",
                      foreground = "black")
alarm_entry.pack()

alarm_button = tk.Button(root, text = "set alarm", command = set_alarm)
alarm_button.pack()

time()
root.mainloop()

