from tkinter import *
import data_analysis



screen = Tk()
screen.geometry("500x500")
screen.title("CSC212 Form")

heading = Label(text="CSC Form", bg="grey", width="1000", height="2")
heading.pack()

first_name_label = Label(text = "Firstname")
first_name_label.place(x = 10, y = 50)
last_name_label = Label(text = "Lastname")
last_name_label.place(x = 10, y = 120)
matric_number_label = Label(text = "Matric Number")
matric_number_label.place(x = 10, y = 190)
score_label = Label(text = "Score")
score_label.place(x = 10, y = 260)

firstname = StringVar()
lastname = StringVar()
matric_number = IntVar()
score = IntVar()

firstname_entry = Entry(textvariable = firstname, width = 50)
firstname_entry.place(x = 10, y = 80)
lastname_entry = Entry(textvariable = lastname, width = 50)
lastname_entry.place(x = 10, y = 150)
matric_number_entry = Entry(textvariable = matric_number, width = 50)
matric_number_entry.place(x = 10, y = 220)
score_entry = Entry(textvariable = score)
score_entry.place(x = 10, y = 290)

submit = Button(screen, text = "Submit", width = "15", height = "1", command = lambda: [data_analysis.student_info(), data_analysis.eda(), data_analysis.stats()])
submit.place(x = 10, y = 330)


screen.mainloop()

