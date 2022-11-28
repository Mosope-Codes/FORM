from tkinter import *
import csv
# from tkinter.filedialog import asksaveasfile
from statistics import mean
import pandas as pd

screen = Tk()
screen.geometry("500x500")
screen.title("CSC212 Form")

score_list = []

# def save_file():
#    file = asksaveasfile(initialfile = 'score_sheet.csv',
# defaultextension=".csv",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

def eda():
    calc = pd.read_csv('score_sheet.csv')
    maximum_score = calc.Score.max()
    average = calc.Score.mean()
    minimum_score = calc.Score.min()
    
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\eda.csv","w",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow(["Max Score", "Min Score", "Mean Score"])
        writer.writerow([maximum_score, minimum_score, average])
    File.close()
    
    
def get_info(): 
    first_name_info = firstname.get()
    last_name_info = lastname.get()
    matric_number_info = matric_number.get()
    score_info = score.get()
    score_list.append(score_info)

    person = {
        'firstName' : first_name_info,
        'lastName' : last_name_info,
        'matric': matric_number_info,
        'score': score_info
    }
    
    return person 

def student_info():
    student_detail = get_info()
    print(f"Firstname: {student_detail['firstName']} \nLastname: {student_detail['lastName']} \nMatric Number: {student_detail['matric']} \nScore: {student_detail['score']} \n ")
    
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\score_sheet.csv","a",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow([student_detail['firstName'], student_detail['lastName'], student_detail['matric'], student_detail['score']])
    File.close()
           
    print(f"{str(student_detail['matric'])} has been recorded successfully")
    
    eda()

    
    
    
    
    
    # scoreSheetEDA = open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\eda.csv","r",newline="\n")
    # with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\eda.csv","a",newline="\n") as File:
    #     writer = csv.writer(File)
    #     writer.writerow(["Max Score", "Min Score", "Mean Score"])
    #     writer.writerow([score_max, score_min, score_mean])
    # File.close()
    # scoreSheetEDA.close
    
    # # firstname_entry.delete(0, END)
    # # lastname_entry.delete(0, END)
    # # matric_number_entry.delete(0, END)
    # # score_entry.delete(0, END)
    
    # max_label = Label(text = f"Max:  {score_max}")
    # max_label.place(x = 10, y = 400)
    # min_label = Label(text = f"Min:  {score_min}")
    # min_label.place(x = 10, y = 420)
    # mean_label = Label(text = f"Mean:  {score_mean}")
    # mean_label.place(x = 10, y = 440)
    



def stats():
    
    lists = get_info()
    
    if lists["score"] < 40:   
        with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\failed.csv","a",newline="\n") as File:
            writer = csv.writer(File)
            writer.writerow([lists["firstName"], lists["lastName"], lists["matric"]])
        File.close()
        
    if lists["score"] >= 70: 
        with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\passed.csv","a",newline="\n") as File:
            writer = csv.writer(File)
            writer.writerow([lists["firstName"], lists["lastName"], lists["matric"]])
        File.close()










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

submit = Button(screen, text = "Submit", width = "15", height = "1", command = lambda: [student_info(), eda(), stats()])
submit.place(x = 10, y = 330)

submit = Button(screen, text = "Analysis", width = "15", height = "1", command = stats)
submit.place(x = 200, y = 330)






screen.mainloop()