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

lb = tk.Listbox(window)

def on_campus():
    lb.insert(1, "McMaster University")
    lb.insert(2, "Western University")
    lb.pack()
    yes['state'] = 'disabled'

    confirm = tk.Button(text="select", command=choose_uni)
    confirm.pack()


def choose_uni():
    for i in lb.curselection():
        print(lb.get(i))


yes = tk.Button(master=frame, text="Yes", command=on_campus)
yes.grid(column=1, row=1)
no = tk.Button(master=frame, text="No")
no.grid(column=2, row=1)



frame.pack()
window.mainloop()
