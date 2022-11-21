from tkinter import *
import csv
from tkinter.filedialog import asksaveasfile
from statistics import mean

score_list = [11, 44, 66]

def stats(num):
    score_list.append(num)
    mean_score = mean(score_list)


def save_file():
   file = asksaveasfile(initialfile = 'score_sheet.csv',
defaultextension=".csv",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

def writeHeader():
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\score_sheet.csv","a",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow(["Firstname", "Lastname", "Matric Number", "Score"])
    File.close()

def appendInfo():
            
    first_name_info = firstname.get()
    last_name_info = lastname.get()
    matric_number_info = matric_number.get()
    score_info = score.get()
    
    person = {
        'firstName' : first_name_info,
        'lastName' : last_name_info,
        'matric': matric_number_info,
        'scorel': score_info
    }
    
    score_list.append(score_info)
    
    print(f"Firstname: {first_name_info} \nLastname: {last_name_info} \nMatric Number: {matric_number_info} \nScore: {score_info} \n ")
       
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\score_sheet.csv","a",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow([first_name_info, last_name_info, matric_number_info, score_info])
    File.close()          
    print(f"{str(matric_number_info)} has been recorded successfully")
    
    
   
    firstname_entry.delete(0, END)
    lastname_entry.delete(0, END)
    matric_number_entry.delete(0, END)
    score_entry.delete(0, END)
    
    return person

def addTOList():
    failedScore = []
    passedScore = []
    lists = appendInfo()
    print(lists['firstName'])
    # print(max(lists))
    # print(min(lists))
    # print(mean(lists))
    
    # for score in lists:
    #     if score < 40:
            
    #         failedScore.append(score)
    #         print(failedScore)
            
    #     if score >= 70:
    #         passedScore.append(score)
    #         print(passedScore)
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\passed.csv","a",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow([lists["firstName"], lists["lastName"], lists["matric"]])
    File.close()



screen = Tk()
screen.geometry("1000x1000")
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

submit = Button(screen, text = "Submit", width = "15", height = "1", command = lambda: [appendInfo()])
submit.place(x = 10, y = 330)

submit = Button(screen, text = "Mean", width = "15", height = "1", command = addTOList)
submit.place(x = 10, y = 360)






screen.mainloop()