# # Importing tkinter module
# from tkinter import *
# # from tkinter.ttk import *
 
# # creating Tk window
# master = Tk()
 
# # creating a Fra, e which can expand according
# # to the size of the window
# pane = Frame(master)
# pane.pack(fill = BOTH, expand = True)
 
# # button widgets which can also expand and fill
# # in the parent widget entirely
# # Button 1
# b1 = Button(pane, text = "Click me !",
#             background = "red", fg = "white")
# b1.pack(side = LEFT, expand = True, fill = BOTH)
 
# # Button 2
# b2 = Button(pane, text = "Click me too",
#             background = "blue", fg = "white")

 
# # Button 3
# b3 = Button(pane, text = "I'm also button",
#             background = "green", fg = "white")
# b3.pack(side = LEFT, expand = True, fill = BOTH)
# b2.pack(side = LEFT, expand = True, fill = BOTH)
# # Execute Tkinter
# master.mainloop()


# var = "Lord"
# print(f"{var} of lords \n love the way")

# for i in range(3):
#     print("yayy")
    
# from tkinter.filedialog import askopenfilename
# from tkinter.filedialog import asksaveasfilename

# filenameforReading = askopenfilename()
# print("You can read from " + filenameforReading)
 
# filenameforWriting = asksaveasfilename()
# print("You can write data to " + filenameforWriting)

from statistics import mean

food = []
food.append(1)
food.append(5)
food.append(9)
print(food)
print(max(food))
print(min(food))
print(sum(food))
print(mean(food))

def fix():
    food.append(22)

score_list = []
print(food)
def stats(num):
    score_list.append(num)
    mean_score = mean(score_list)
    print(mean_score)
    
stats()
