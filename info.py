from ui import *
from data_analysis import eda
import csv

score_list = []

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