from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- WINDOW POPUP ------------------------------- #
def raise_above_all():
    if window.state() == "iconic":
        window.state("normal")

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    reps = 0
    timer = None


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    if timer is None:
        global reps
        reps += 1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 2 != 0:
            title_label.config(text="WORK", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
            count_down(work_sec)
        elif reps % 8 == 0:
            title_label.config(text="BREAK", font=(FONT_NAME, 50, "bold"), fg=RED, bg=YELLOW)
            count_down(long_break_sec)
        elif reps % 2 == 0:
            title_label.config(text="BREAK", font=(FONT_NAME, 50, "bold"), fg=PINK, bg=YELLOW)
            count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        timer = None
        raise_above_all()
        start_timer()
        marks = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            marks += "✔"
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# creating timer label
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

check_label = Label(font=(FONT_NAME, 15, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)
# creating button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

# creating canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

window.mainloop()
