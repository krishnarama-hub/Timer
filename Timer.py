from tkinter import *

import math

PINK="#e2979c"
RED="#e7305b"
GREEN="#9bdeac"
YELLOW="#f7f5dd"
FORNT_NAME="Courier"
WORK_MIN=25
SHORT_BREAK_MIN=5
LONG_BREAK_MIN=20
timer=None

def reset_timer():
    window.after_cancel(timer)

    canvas.itemconfig(text_canvas,text="00:00")

    label.config(text="Timer")

    check.config(text="")

    global reps

    reps=0


reps=0

window=Tk()

window.title("Time Watch")

def star_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break__sec = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break)
        label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        countdown(short_break__sec)
        label.config(text="Break", fg=PINK)

    else:
        countdown(work_sec)
        label.config(text="Work", fg=GREEN)

def countdown(count):

    count_min=math.floor(count/60)

    count_sec=count % 60

    if count_sec<10:

        count_sec=f"0{count_sec}"

    if count_min==0:

        count_min="00"

    canvas.itemconfig(text_canvas, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer

        timer=window.after(1000, countdown, count - 1)

    else:
        star_timer()

        mark=""

        for _ in range(math.floor(reps/2)):

            mark+="✓"

        check.config(text=mark)



window.config(bg=YELLOW)

label=Label(text="Timer",font=(FORNT_NAME,35,"bold"),bg=YELLOW,fg=GREEN)

label.grid(column=1,row=0)

window.config(padx=100,pady=100,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

tomato_img=PhotoImage(file=r"C:\Users\shali\Desktop\GITHUB_PROJECTS\Timer\tomato.png")

canvas.create_image(100,110,image=tomato_img)

text_canvas=canvas.create_text(100,130,text="00:00",fill="white",font=(FORNT_NAME,35,"bold"))

canvas.grid(column=1,row=1)

start=Button(text="Start",command=star_timer)

reset=Button(text="reset",command=reset_timer)

start.grid(column=0,row=3)

reset.grid(column=3,row=3)

check=Label(text="",bg=YELLOW,fg=GREEN,font=("Arial",20,"bold"))

check.grid(column=1,row=3)




window.mainloop()