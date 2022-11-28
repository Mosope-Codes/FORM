import pandas as pd
import csv
import ui

score_list = []

def get_info(): 
    first_name_info = ui.firstname.get()
    last_name_info = ui.lastname.get()
    matric_number_info = ui.matric_number.get()
    score_info = ui.score.get()
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




    
    
