# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:42:37 2019

@author: einasc
"""
from Tkinter import *
import os
import io

    
def register_group():
    student_string = u""
    file_path = group_folder + "/" + group_number.get() + ".txt"
    file = io.open(file_path, "w")
    
    teststr = students[0][0].get()
    for i in range(len(students)):                
        student_string= student_string + students[i][0].get()+u","+students[i][1].get()+u","+students[i][2].get() + u"\n"

    file.write(student_string)
    file.close()
    
    Label(screen,text = "Gruppe "+group_number.get() + " registrert", fg="green").pack()
    screen2.destroy()
    screen1.destroy()    
    
def student_summary(student_num):
    y_offset        = (student_num)*35
    x_name          = 43
    x_course        = 200
    x_study         = 300
    
    Label(screen2,text = students[student_num-1][0].get(),font = default_font).place(x=x_name,y=y_offset)
    Label(screen2,text = students[student_num-1][1].get(),font = default_font).place(x=x_course,y=y_offset)
    Label(screen2,text = students[student_num-1][2].get(),font = default_font).place(x=x_study,y=y_offset)    
def verify_group():
    list_of_groups = os.listdir(group_folder)
    proceed = 1
    error_string = ""
    group = group_number.get()
    file_name = group + ".txt"
    if not group.isdigit():
        proceed = 2
        error_string = "Ugydlig gruppenummer"
    elif  file_name in list_of_groups:
        proceed = 3
        error_string = "Gruppenummer opptatt"        
    elif int(group) > max_group_number:
        proceed = 4        
        error_string = "Ugyldig gruppenummer"
    return proceed, error_string


def confirm_group():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Bekreft gruppe")
    screen2.geometry("400x350")    

    Label(screen2,text = "Gruppe " + group_number.get() ,font = default_font).pack()    
    
    student_summary(1)
    student_summary(2)
    student_summary(3)
    student_summary(4)
    student_summary(5)
    
    proceed, error_string = verify_group()
    if proceed == 1:    
        Button(screen2, text="Bekreft",font = default_font, width = 40, height = 1, command = register_group).place(x=200,y=300, anchor="center")
    else:
        Button(screen2, text = error_string,font = default_font, fg = "red", width = 40, height = 1).place(x=200,y=300, anchor="center")

def student_entry(student_num):

    name    = StringVar()
    course  = StringVar()
    study   = StringVar()
    
    y_offset        = (student_num-1)*70

    x_name          = 43
    x_course        = 390
    x_study         = 600
    y_member_number = 110 + y_offset
    y_member_label  = 130 + y_offset
    y_member_entry  = 155 + y_offset
    
    participant_str = "Deltaker " + str(student_num)
    
    Label(screen1,text = participant_str,font = default_font).place(x=x_name,y=y_member_number)
    
    Label(screen1,text = "Navn",font = default_font).place(x=x_name,y=y_member_label)
    name_entry = Entry(screen1,textvariable = name,width=50)
    name_entry.place(x=x_name,y=y_member_entry)    

    Label(screen1,text = "Fagkode",font = default_font).place(x=x_course,y=y_member_label)
    course_list = ['','TKT4116','TKT4118?','TKT4120?']
    droplist = OptionMenu(screen1,course,*course_list)
    droplist.config(width=15)
    course.set('') 
    droplist.place(x=x_course,y=y_member_entry)        
    
    Label(screen1,text = "Studiekode",font = default_font).place(x=x_study,y=y_member_label)    
    study_entry = Entry(screen1,textvariable = study,font = default_font)
    study_entry.place(x=x_study,y=y_member_entry)    
    
    return (name,course,study)
            
def new_group():
    global screen1
    global group_number
    global group_number_entry
    global students
    
    group_number = StringVar()    
    screen1 = Toplevel(screen)
    screen1.title("Registrer ny gruppe")
    screen1.geometry("800x700")
    
    Label(screen1,text = "Gruppenummer",font = default_font).place(x=45,y=30)
    group_number_entry = Entry(screen1, textvariable = group_number,font = default_font)
    group_number_entry.place(x=45,y=55)
    
    
    student1 = student_entry(1)
    student2 = student_entry(2)
    student3 = student_entry(3)
    student4 = student_entry(4)
    student5 = student_entry(5)
    
    students = (student1,student2,student3,student4,student5)
    Button(screen1, text="Registrer",font = default_font, width = 11, height = 1, command = confirm_group).place(x=600,y=610)

def verify_group_number():
    list_of_groups = os.listdir(group_folder)
    proceed = 1
    error_string = ""
    group = group_number.get()
    file_name = group + ".txt"
    if  file_name in list_of_groups:
        proceed = 3
        error_string = "Gruppenummer opptatt"        
    elif not group.isdigit():
        proceed = 2
        error_string = "Ugydlig gruppenummer"        
    elif int(group) > max_group_number:
        proceed = 4        
        error_string = "Ugyldig gruppenummer"
    return proceed, error_string

def read_group():
    print("Coming soon")
    # Les .txt fil
       
def show_group():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Registrer ny gruppe")
    screen4.geometry("800x700")
    # read_group() les inn gruppeinfo
    # Åpne student_entry() med default felt allerede fyllt inn
    # Samme procedyre som registrering
def open_group_verify():
    list_of_groups = os.listdir(group_folder)
    proceed = 1
    error_string = ""
    file_name = open_group_number.get() + ".txt"
    if  file_name in list_of_groups:
        group_proceed = 1
    else: 
        error_string = error_string + "Ugyldig gruppe. "
        group_proceed = 0        
        
    if password_entry.get() == password:
        password_proceed = 1        
    else: 
        error_string = error_string + "Ugyldig passord."
        password_proceed = 0          

    proceed = group_proceed * password_proceed        
    if proceed != 0:
        open_button.configure(text='Riktig',fg = 'green')        
        show_group()
    else:
        open_button.configure(text=error_string,fg = 'red')
        
        
  
def open_group_main():
    global screen3
    global password_entry 
    global open_button
    global open_group_number
    open_group_number = StringVar()
    password          = StringVar()    

    screen3 = Toplevel(screen)
    screen3.title("Åpne gruppe")
    screen3.geometry("300x250")

    Label(screen3,text = "Åpne gruppe").pack()    

    Label(screen3,text = "").pack()
    Label(screen3,text = "Skriv inn ønsket gruppenummer").pack()
    group_entry = Entry(screen3,textvariable = open_group_number)
    group_entry.pack()
    
    Label(screen3,text = "").pack()  
    Label(screen3,text = "").pack()      

    Label(screen3,text="Skriv inn passord for å redigere").pack()   
    password_entry = Entry(screen3,textvariable = password)
    password_entry.pack()
    
    open_button = Button(screen3,text = "Åpne", width = 40, height = 1, command = open_group_verify)
    open_button.pack()      

        
def main_screen():
    global default_font
    global screen
    global group_folder
    global max_group_number
    global password 
    
    
    default_font = ("Calibri", 12)
    group_folder = ("Grupper")
    max_group_number = 100
    password = "TKT"
    
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Labregistrering 1.0")
    Label(text="Labregistrering 1.0", bg = "grey", width="300", height="2",font =("Calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Ny gruppe",height="2",width="30", command=new_group).pack()
    Label(text="").pack()
    Button(text = "Åpne gruppe",height="2",width="30",command = open_group_main).pack()
    screen.mainloop()

main_screen()    