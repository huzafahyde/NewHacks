import tkinter as tk


window = tk.Tk()
window.geometry('600x500')
window['background'] = '#E47B7B'

main_frame = tk.Frame(master=window)
yesno_frame = tk.Frame(master=main_frame)
number_frame = tk.Frame(master=main_frame)

welcome = tk.Label(
    text="Welcome to Party Doctor",
    master=main_frame
)
welcome.pack()

campus_question = tk.Label(
    text="Are you on campus currently?",
    master=main_frame
)
campus_question.pack()


lb = tk.Listbox(master=main_frame)

def on_campus():
    lb.insert(1, "McMaster University")
    lb.insert(2, "Western University")
    lb.insert(3, "Queens University")
    lb.insert(4, "University of Toronto")
    lb.insert(5, "University of Guelph")
    lb.pack()
    yes['state'] = 'disabled'

    confirm = tk.Button(text="select", command=choose_uni,master=main_frame)
    confirm.pack()


def choose_uni():
    for i in lb.curselection():
        print(lb.get(i))
    main_frame.destroy()
    yesno_frame.destroy()
    show_guesses()



yes = tk.Button(master=yesno_frame, text="Yes", command=on_campus)
yes.grid(column=1, row=1)
no = tk.Button(master=yesno_frame, text="No")
no.grid(column=2, row=1)


main_frame.pack()
yesno_frame.pack()

guess_frame = tk.Frame(master=window)

def show_guesses():
    guess_label = tk.Label(text="Which one of these is the person most likely suffering from")
    guess_label.pack()
    alc_poi = tk.Button(text='Alcohol Poisoning',master=guess_frame,command=show_response(1))
    alc_poi.grid(column=1, row=1)
    drug_over = tk.Button(text='Drug Overdose',master=guess_frame,command=show_response(2))
    drug_over.grid(column=2, row=1)
    choking = tk.Button(text='Choking',master=guess_frame,command=show_response(3))
    choking.grid(column=3, row=1)
    bleeding = tk.Button(text='Bleeding',master=guess_frame,command=show_response(4))
    bleeding.grid(column=4, row=1)
    other = tk.Button(text='Other or I do not know',master=guess_frame,command=show_response(5))
    other.grid(column=5, row=1)

    guess_frame.pack()

responses = []

#def show_response(ID):




window.mainloop()
