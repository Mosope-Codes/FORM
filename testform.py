import xlwt

import tkinter as tk
root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing details
cid_var = tk.StringVar()
cname_var = tk.StringVar()
caddr_var = tk.StringVar()
cstate_var = tk.StringVar()
ccity_var = tk.StringVar()
cmobile_var = tk.StringVar()
cgender_var = tk.StringVar()
cage_var = tk.StringVar()

# defining a function that will
# get the details and
# print them on the screen
def submit():
    cid = cid_var.get()
    cname = cname_var.get()
    caddr = caddr_var.get()
    cstate = cstate_var.get()
    ccity = ccity_var.get()
    cmobile = cmobile_var.get()
    cgender = cgender_var.get()
    cage = cage_var.get()

    workbook = xlwt.Workbook()

#Naming the sheet in the excel
    sheet = workbook.add_sheet("Contact Details")

    sheet.write(0, 0, 'Contact Details')
    sheet.write(1, 0, 'Contact ID')
    sheet.write(2, 0, 'Name')
    sheet.write(3, 0, 'Address')
    sheet.write(4, 0, 'State')
    sheet.write(5, 0, 'City')
    sheet.write(6, 0, 'Mobile No')
    sheet.write(7, 0, 'Gender')
    sheet.write(8, 0, 'Age')

    sheet.write(1, 1, cid)
    sheet.write(2, 1, cname)
    sheet.write(3, 1, caddr)
    sheet.write(4, 1, cstate)
    sheet.write(5, 1, ccity)
    sheet.write(6, 1, cmobile)
    sheet.write(7, 1, cgender)
    sheet.write(8, 1, cage)
    
#saving the data to excel
    workbook.save("ContactDetails.xls")

    cid_var.set("")
    cname_var.set("")
    caddr_var.set("")
    cstate_var.set("")
    ccity_var.set("")
    cmobile_var.set("")
    cgender_var.set("")
    cage_var.set("")

cid_label = tk.Label(root, text='Contact ID', font=('calibre', 10, 'bold'))
cname_label = tk.Label(root, text='Contact Name', font=('calibre', 10, 'bold'))
caddr_label = tk.Label(root, text='Contact Address', font=('calibre', 10, 'bold'))
cstate_label = tk.Label(root, text='State', font=('calibre', 10, 'bold'))
ccity_label = tk.Label(root, text='City', font=('calibre', 10, 'bold'))
cmobile_label = tk.Label(root, text='Mobile Number', font=('calibre', 10, 'bold'))
cgender_label = tk.Label(root, text='Gender', font=('calibre', 10, 'bold'))
cage_label = tk.Label(root, text='Age', font=('calibre', 10, 'bold'))

cid_entry = tk.Entry(root, textvariable=cid_var, font=('calibre', 10, 'normal'))
cname_entry = tk.Entry(root, textvariable=cname_var, font=('calibre', 10, 'normal'))
caddr_entry = tk.Entry(root, textvariable=caddr_var, font=('calibre', 10, 'normal'))
cstate_entry = tk.Entry(root, textvariable=cstate_var, font=('calibre', 10, 'normal'))
ccity_entry = tk.Entry(root, textvariable=ccity_var, font=('calibre', 10, 'normal'))
cmobile_entry = tk.Entry(root, textvariable=cmobile_var, font=('calibre', 10, 'normal'))
cgender_entry = tk.Entry(root, textvariable=cgender_var, font=('calibre', 10, 'normal'))
cage_entry = tk.Entry(root, textvariable=cage_var, font=('calibre', 10, 'normal'))

#submit button
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
cid_label.grid(row=0, column=0)
cname_label.grid(row=1, column=0)
caddr_label.grid(row=2, column=0)
cstate_label.grid(row=3, column=0)
ccity_label.grid(row=4, column=0)
cmobile_label.grid(row=5, column=0)
cgender_label.grid(row=6, column=0)
cage_label.grid(row=7, column=0)

cid_entry.grid(row=0, column=1)
cname_entry.grid(row=1, column=1)
caddr_entry.grid(row=2, column=1)
cstate_entry.grid(row=3, column=1)
ccity_entry.grid(row=4, column=1)
cmobile_entry.grid(row=5, column=1)
cgender_entry.grid(row=6, column=1)
cage_entry.grid(row=7, column=1)

sub_btn.grid(row=8, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()