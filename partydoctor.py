import tkinter as tk

leave = False
counter = 0

window = tk.Tk()
window.geometry('600x500')
window['background'] = '#E47B7B'
welcome = tk.Label(
    text="Welcome to Party Doctor"
)
welcome.pack()

campus_question = tk.Label(
    text="Are you on campus currently?"
)
campus_question.pack()

frame = tk.Frame(master=window)


def on_campus():
    lb = tk.Listbox(window)
    lb.insert(1, "McMaster University")
    lb.insert(2, "Western University")
    lb.pack()
    yes['state'] = 'disabled'

yes = tk.Button(master=frame,text="Yes", command = on_campus)
yes.grid(column = 1,row=1)
no = tk.Button(master=frame,text="No")
no.grid(column = 2,row=1)

frame.pack()
window.mainloop()

