from tkinter import *
from tkinter.scrolledtext import ScrolledText
import keyboard


root = Tk()
root.title('My Awesome App')
root.geometry("800x650")
root.after_id = None
count = 7


# ------------------------------------ FUNCTIONS ------------------------------------ #
def store():
	global textbox
	values = textbox.get("1.0", "end-1c")
	print(values)


def key_pressed(event):
	global count
	if keyboard.is_pressed:
		count = 7


def countdown():
	global count
	start_btn["state"] = DISABLED

	if count > 0:
		count -= 1
	if count == 6:
		timer_label.config(text="")
		root.after(1000, countdown)
	if count < 0 or count == 0:
		print(count)
		timer_label.config(text="")
		start_btn["state"] = NORMAL
		store()
		textbox.frame.destroy()
		root.after_id = None
	if 5 > count > 0 or count == 5 and count > 0:
		timer_label.config(text=f"{count} seconds to delete everything!", fg="red")
		print(count)
		root.after(1000, countdown)


def start_timer():
	global count
	global textbox
	count = 7

	textbox = ScrolledText()
	textbox.bind("<Key>", key_pressed)
	textbox.pack()

	if root.after_id is not None:
		root.after_cancel(root.after_id)
	countdown()


# ------------------------------------ LABELS AND BUTTONS ------------------------------------ #
label1 = Label(text="DON'T STOP WRITING", font=("Arial", 15))
label1.pack(pady=20)

label2 = Label(
	text="If you stop writing for more than 5 seconds, your text will be lost forever.",
	font=("Arial", 10, "italic")
)
label2.pack()

start_btn = Button(text="Start Writing", width=20, command=start_timer)
start_btn.pack(pady=10)

timer_label = Label(text="")
timer_label.pack(pady=10)

root.mainloop()
