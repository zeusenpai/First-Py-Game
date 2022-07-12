from tkinter import *
from main import play

def close():
    wnd.destroy()

def start():
    user_a = entry.get()
    user_b = entry2.get()
    play(user_a, user_b)
    close()

wnd = Tk()
wnd.config(background="black")
wnd.title("Pong!")
wnd.geometry("800x160")

label = Label(wnd, text="Pong!", font=('Courier', 24, "bold"), fg="#ffffff", bg="#000000")
label.config(text="Enter Player 1 Name: ", font=('Courier', 24, "bold"))
label.place(x=0,y=10)

entry = Entry(wnd, font=('Courier', 24, "bold"), fg="#ffffff", bg="#000000")
entry.place(x=400,y=10)

label2 = Label(wnd, text="Pong!", font=('Courier', 24, "bold"), fg="#ffffff", bg="#000000")
label2.config(text="Enter Player 2 Name: ", font=('Courier', 24, "bold"))
label2.place(x=0,y=60)

entry2 = Entry(wnd, font=('Courier', 24, "bold"), fg="#ffffff", bg="#000000")
entry2.place(x=400,y=60)

play_button = Button(wnd, text="Play", command=start, fg="#ffffff", bg="#000000")
play_button.place(x=380,y=120)

exit_button = Button(wnd, text="Exit", command=close, fg="#ffffff", bg="#000000")
exit_button.place(x=420,y=120)

wnd.mainloop()
close()
