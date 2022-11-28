from ui import *
from statistics import mean




score_list = []            
first_name_info = firstname.get()
last_name_info = lastname.get()
matric_number_info = matric_number.get()
score_info = score.get()
score_list.append(score_info)

def appendInfo():
       
    person = {
        'firstName' : first_name_info,
        'lastName' : last_name_info,
        'matric': matric_number_info,
        'score': score_info
    }
       
    print(f"Firstname: {first_name_info} \nLastname: {last_name_info} \nMatric Number: {matric_number_info} \nScore: {score_info} \n ")
       
       
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\score_sheet.csv","a",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow([first_name_info, last_name_info, matric_number_info, score_info])
    File.close()
          
    print(f"{str(matric_number_info)} has been recorded successfully")
    eda()
    
    return person