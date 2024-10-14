from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
root = Tk()


root.title("AI Assistant")
root.geometry("820x800")
root.resizable(False, False)
root.config(bg="#000000")

# ask function


def ask():
    ask_val = speech_to_text.speech_to_text()
    bot_val = action.Action(ask_val)
    text.insert(END, "User----> "+ask_val+"\n")
    if bot_val != None:
        text.insert(END, "BOT<----"+str(bot_val)+"\n")
    if bot_val == "Your system will shut down soon.":
        root.destroy()


# send function
def send():
    send = entry.get()
    bot = action.Action(send)
    text.insert(END, "User----> "+send+"\n")
    if bot != None:
        text.insert(END, "BOT<----"+str(bot)+"\n")
    if bot == "Your system will shut down soon.":
        root.destroy()


# send function
def delete():
    text.delete('1.0', "end")

# Frame


frame = LabelFrame(root, padx=100, pady=10, border=0)
frame.config(bg="#000000")

frame.grid(row=0, column=1, padx=55, pady=5)

# text label

text_label = Label(frame, text="AI Assistant", font=(
    "sans serif", 25, "bold"), fg="#fff", bg="#000")
text_label.grid(row=0, column=0, padx=20, pady=5)


# image

image = ImageTk.PhotoImage(Image.open("image/ai.gif"))
image_label = Label(frame, image=image,  bd=0, highlightthickness=0)
image_label.grid(row=1, column=0, pady=10)

# Adding some text widget

text = Text(root, font=("sans 10 bold"), bg="#000", fg="green")
text.grid(row=2, column=0)
text.place(x=220, y=460, width=375, height=100)


# entry widget
entry = Entry(root, justify=CENTER)
entry.place(x=230, y=600, width=350, height=30)


# button 1


Button1 = Button(root, text="ASK", bg="#356696", padx=40,
                 pady=16, borderwidth=2, relief=SOLID, command=ask)
Button1.place(x=190, y=670)

Button1 = Button(root, text="SEND", bg="#356696", padx=40,
                 pady=16, borderwidth=2, relief=SOLID, command=send)
Button1.place(x=350, y=670)

Button1 = Button(root, text="REMOVE", bg="#356696", padx=40,
                 pady=16, borderwidth=2, relief=SOLID, command=delete)
Button1.place(x=510, y=670)


root.mainloop()
