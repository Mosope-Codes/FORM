from info import *
import pandas as pd
import csv



def eda():
    calc = pd.read_csv('score_sheet.csv')
    maxi = calc.Score.max()
    avg = calc.Score.mean()
    mini = calc.Score.min()
    
    with open("C:\\Users\\Mosope\\Desktop\\Projects\\FORM\\eda.csv","w",newline="\n") as File:
        writer = csv.writer(File)
        writer.writerow(["Max Score", "Min Score", "Mean Score"])
        writer.writerow([maxi, mini, avg])
    File.close()
    
    
def stats():
   
    lists = appendInfo()
    
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