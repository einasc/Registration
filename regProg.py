# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 12:42:37 2019

@author: einasc
"""
from Tkinter import *
import os
import io
import datetime


def write_group_to_file(group_number, students, bridge_weight, bridge_capacity, bridge_ratio):
    student_string = u""
    file_path = group_folder + "/" + group_number.get() + ".txt"
    group_file = io.open(file_path, "w")

    for i in range(len(students)):
        student_string = student_string + students[i][0].get() + u"," + students[i][1].get() + u"," + students[i][
            2].get() + u"\n"

    result_string = bridge_weight.get() + u"," + bridge_capacity.get() + u"," + bridge_ratio + u"\n"

    now = datetime.datetime.now()
    date_string = now.strftime("%x , %X, \n")

    group_string = student_string + result_string + date_string
    group_file.write(group_string)
    group_file.close()


def rolling_label(label_group):
    if len(label_group) >=3:
        label_group[len(label_group)-3].destroy()


def register_new_group(group_number, students, bridge_weight, bridge_capacity, bridge_ratio):
    write_group_to_file(group_number, students, bridge_weight, bridge_capacity, bridge_ratio)
    registration_label = Label(main_screen, text="Gruppe " + group_number.get() + " registrert", fg="#3E9651")
    registration_label.pack()
    label_group_register.append(registration_label)
    if len(label_group_register) >= 4:
        label_group_register[len(label_group_register)-4].destroy()
    screen2.destroy()
    screen1.destroy()


def student_summary(student_num, students):
    y_offset = student_num * 35
    x_name = 43
    x_course = 200
    x_study = 300

    Label(screen2, text=students[student_num - 1][0].get(), font=default_font).place(x=x_name, y=y_offset)
    Label(screen2, text=students[student_num - 1][1].get(), font=default_font).place(x=x_course, y=y_offset)
    Label(screen2, text=students[student_num - 1][2].get(), font=default_font).place(x=x_study, y=y_offset)


def verify_group(group_number):
    list_of_groups = os.listdir(group_folder)
    proceed = 1
    error_string = ""
    group = group_number.get()
    file_name = group + ".txt"
    if group == "dev":
        proceed = 1
    elif not group.isdigit():
        proceed = 2
        error_string = "Ugydlig gruppenummer"
    elif file_name in list_of_groups:
        proceed = 3
        error_string = "Gruppenummer opptatt"
    elif int(group) > max_group_number:
        proceed = 4
        error_string = "Ugyldig gruppenummer"
    return proceed, error_string


def development_default_group(students, bridge_weight, bridge_capacity):
    for student_num in range(5):
        students[student_num][0].set("Ola" + str(student_num))
        students[student_num][1].set("TKT4116")
        students[student_num][2].set("MTMEK")

    bridge_weight.set("100")
    bridge_capacity.set("200")


def make_confirm_group_dialog(group_number, students, bridge_weight, bridge_capacity):
    global screen2
    screen2 = Toplevel(main_screen)
    screen2.title("Bekreft gruppe")
    screen2.geometry("400x350")

    if group_number.get() == "dev":
        development_default_group(students, bridge_weight, bridge_capacity)

    Label(screen2, text="Gruppe " + group_number.get(), font=default_font).pack()

    for student_num in range(5):                            # Add summary rows for all students
        student_summary(student_num+1, students)

    if bridge_weight.get().isdigit() and (bridge_capacity.get()).isdigit():
        bridge_ratio = str(float(bridge_capacity.get()) / float(bridge_weight.get()))
    else:
        bridge_ratio = "Ugyldig"

    Label(screen2, text="Egenvekt: " + bridge_weight.get() + "g", font=default_font).place(x=200, y=240, anchor="w")
    Label(screen2, text="Kapasitet: " + bridge_capacity.get() + "g", font=default_font).place(x=200, y=240, anchor="e")
    Label(screen2, text="Forholdstall: " + bridge_ratio, font=default_font).place(x=200, y=270, anchor="center")

    proceed, error_string = verify_group(group_number)
    if proceed == 1:
        Button(screen2, text="Bekreft", font=default_font, width=40, height=1, command=lambda: register_new_group(group_number, students, bridge_weight, bridge_capacity, bridge_ratio)).place(x=200, y=300, anchor="center")
    else:
        Button(screen2, text=error_string, font=default_font, fg="red", width=40, height=1).place(x=200, y=300,anchor="center")


def student_entry(screen, student_num, group_list, default_course, default_study):
    name = StringVar()
    course = StringVar()
    study = StringVar()

    y_offset = (student_num - 1) * 70

    x_name = 43
    x_course = 400
    x_study = 600
    y_member_number = 110 + y_offset
    y_member_label = 130 + y_offset
    y_member_entry = 155 + y_offset

    participant_str = "Deltaker " + str(student_num)

    Label(screen, text=participant_str, font=default_font).place(x=x_name, y=y_member_number)

    Label(screen, text="Navn", font=default_font).place(x=x_name, y=y_member_label)

    name_entry = Entry(screen, textvariable=name, width=40, font=default_font)
    name_entry.place(x=x_name, y=y_member_entry)

    Label(screen, text="Fagkode", font=default_font).place(x=x_course, y=y_member_label)
    course_list = ['', 'TKT4116', 'TKT4123', 'TKT4126']
    course_drop_list = OptionMenu(screen, course, *course_list)
    course_drop_list.config(width=15)
    course.set(default_course)
    course_drop_list.place(x=x_course, y=y_member_entry)

    Label(screen, text="Studiekode", font=default_font).place(x=x_study, y=y_member_label)
    study_list = ['', 'MTBYGG', 'MTENERG', 'MTING', 'MTIØT', 'MTMART', 'MTMT', 'MTPETR', 'MTPROD', 'MTTEKGEO', 'BGEOL', 'Øvrige']
    study_drop_list = OptionMenu(screen, study, *study_list)
    study_drop_list.config(width=15)
    study.set(default_study)
    study_drop_list.place(x=x_study, y=y_member_entry)
    if group_list:      # Set entries if files is opened
        name.set(group_list[student_num-1][0])
        course.set(group_list[student_num-1][1])
        study.set(group_list[student_num-1][2])
    return name, course, study


def new_group_dialog(default_course, default_study):
    global screen1

    group_number = StringVar()
    bridge_weight = StringVar()
    bridge_capacity = StringVar()

    screen1 = Toplevel(main_screen)
    screen1.title("Registrer ny gruppe")
    screen1.geometry("800x700")

    Label(screen1, text="Gruppenummer", font=default_font).place(x=45, y=30)
    group_number_entry = Entry(screen1, textvariable=group_number, font=default_font)
    group_number_entry.place(x=45, y=55)

    students = list()
    empty_list = list()
    for student_num in range(5):
        students.append(student_entry(screen1, student_num+1, empty_list, default_course, default_study))

    Frame(screen1, height=1, width=800, bg="black").place(x=400, y=490, anchor="center")

    Label(screen1, text="Broens egenvekt [g]", font=default_font).place(x=45, y=505)
    bridge_weight_entry = Entry(screen1, textvariable=bridge_weight, font=default_font)
    bridge_weight_entry.place(x=45, y=530)

    Label(screen1, text="Broens kapasitet [g]", font=default_font).place(x=400, y=505)
    bridge_capacity_entry = Entry(screen1, textvariable=bridge_capacity, font=default_font)
    bridge_capacity_entry.place(x=400, y=530)

    Frame(screen1, height=1, width=800, bg="black").place(x=400, y=580, anchor="center")

    Button(screen1, text="Registrer", font=default_font, width=11, height=1, command=lambda: make_confirm_group_dialog(group_number, students, bridge_weight, bridge_capacity)).place(
        x=600, y=610)

    Button(screen1, text="Avbryt", font=default_font, width=11, height=1, command=lambda: close_screen(screen1)).place(
        x=45, y=610)


def read_group(group_number):
    file_name = "Grupper/" + group_number + ".txt"
    group_file = io.open(file_name, "r")
    group_text = group_file.read()
    group_lines = group_text.splitlines()
    group_list = list()
    for i in range(len(group_lines)):
        group_list.append(group_lines[i].split(","))
    group_file.close()
    return group_list


def close_screen(screen):
    screen.destroy()


def delete_group(group_number, screen):
    screen.destroy()
    os.remove("Grupper/"+group_number+".txt")
    edit_label = Label(screen3, text="Gruppe " + group_number + " slettet.", fg='red')
    edit_label.pack()

    label_group_edit.append(edit_label)
    if len(label_group_edit) >= 4:
        label_group_edit[len(label_group_edit)-4].destroy()

    screen4.destroy()


def register_edited_group(group_number, students, bridge_weight, bridge_capacity, bridge_ratio):
    write_group_to_file(group_number, students, bridge_weight, bridge_capacity, bridge_ratio)
    edit_label = Label(screen3, text="Gruppe " + group_number.get() + " endret", fg="#3E9651")
    edit_label.pack()

    label_group_edit.append(edit_label)
    if len(label_group_edit) >= 4:
        label_group_edit[len(label_group_edit)-4].destroy()

    screen4.destroy()
    screen6.destroy()


def confirm_edit_group_dialog(old_group_number, group_number, students, bridge_weight, bridge_capacity):
    global screen6
    screen6 = Toplevel(main_screen)
    screen6.title("Bekreft rediger gruppe")
    screen6.geometry("200x150")

    bridge_ratio = str(float(bridge_capacity.get()) / float(bridge_weight.get()))

    proceed, error_string = verify_group(group_number)

    if proceed == 3 and old_group_number == group_number.get():
        proceed = 1
        error_string = "oui "

    Label(screen6, text="Rediger gruppe " + group_number.get() + "?", font=default_font).pack()
    if proceed == 1:
        Button(screen6, text="Bekreft", font=default_font, width=20, height=1, command=lambda: register_edited_group(group_number, students, bridge_weight, bridge_capacity, bridge_ratio)).pack()
    else:
        Button(screen6, text=error_string, fg='red', font=default_font, width=20, height=1).pack()
    Button(screen6, text="Avbryt", font=default_font, width=20, height=1, command=lambda: close_screen(screen6)).pack()


def confirm_delete_group_dialog(group_number, students, bridge_weight, bridge_capacity):
    global screen5
    screen5 = Toplevel(main_screen)
    screen5.title("Slett gruppe")
    screen5.geometry("200x150")
    Label(screen5, text="Slette gruppe " + group_number + "?", font=default_font).pack()
    Button(screen5, text="Bekreft", font=default_font, width=11, height=1, command=lambda: delete_group(group_number, screen5)).pack()
    Button(screen5, text="Avbryt", font=default_font, width=11, height=1, command=lambda: close_screen(screen5)).pack()


def sort_list_of_groups(list_of_groups):
    new_list = []
    for group in list_of_groups:
        new_group = group.replace(".txt", "")
        if new_group.isdigit():
            new_list.append(new_group)
    new_list.sort(key=int)

    new_list[:] = [str(x) + ".txt" for x in new_list]
    list_of_groups = new_list
    return list_of_groups


def write_course_specific_report(course):
    list_of_groups = os.listdir(group_folder)
    list_of_groups = sort_list_of_groups(list_of_groups)

    full_string = u""
    for group in list_of_groups:
        group_number = group.replace(".txt", "")
        group_list = read_group(group_number)
        for i in range(5):
            if group_list[i][0]:
                if group_list[i][2] == course:
                    full_string = full_string + group_list[i][0] + u"," + group_list[i][2] + u"\n"

    file_path = "all_students.txt"
    all_group_file = io.open(file_path, "w")
    all_group_file.write(full_string)
    all_group_file.close()


def write_student_summary_file():
    list_of_groups = os.listdir(group_folder)
    list_of_groups = sort_list_of_groups(list_of_groups)

    full_string = u""
    for group in list_of_groups:
        group_number = group.replace(".txt", "")
        group_list = read_group(group_number)
        for i in range(5):
            if group_list[i][0]:
                full_string = full_string + group_list[i][0] + u"," + group_list[i][2] + u"\n"

    file_path = "all_students.csv"
    all_group_file = io.open(file_path, "w")
    all_group_file.write(full_string)
    all_group_file.close()


def write_group_summary_file():
    list_of_groups = os.listdir(group_folder)
    list_of_groups = sort_list_of_groups(list_of_groups)

    full_string = u""
    for group in list_of_groups:
        group_number = group.replace(".txt", "")
        group_list = read_group(group_number)
        full_string = full_string + group_number
        for i in range(5):
            full_string = full_string + u"," + group_list[i][0] + u"," + group_list[i][2]
        full_string = full_string + u"," + group_list[5][0] + u"," + group_list[5][1] + u"," + group_list[5][2] + u"," + group_list[6][0] + u"," + group_list[6][1]
        full_string = full_string + u"\n"
    file_path = "all_groups.txt"
    all_group_file = io.open(file_path, "w")
    all_group_file.write(full_string)
    all_group_file.close()


def write_summary_files(button):
    write_group_summary_file()
    write_student_summary_file()
    button.configure(text='Samlefil skrevet', fg='#3E9651')


def edit_group_dialog(old_group_number):
    global screen4
    group_list = read_group(old_group_number)

    group_number = StringVar()
    bridge_weight = StringVar()
    bridge_capacity = StringVar()

    screen4 = Toplevel(main_screen)
    screen4.title("Rediger gruppe")
    screen4.geometry("800x700")

    Label(screen4, text="Gruppenummer", font=default_font).place(x=45, y=30)
    group_number_entry = Entry(screen4, textvariable=group_number, font=default_font)
    group_number_entry.place(x=45, y=55)
    group_number.set(old_group_number)

    students = list()
    for student_num in range(5):
        students.append(student_entry(screen4, student_num+1, group_list, '', ''))

    Frame(screen4, height=1, width=800, bg="black").place(x=400, y=490, anchor="center")

    Label(screen4, text="Broens egenvekt [g]", font=default_font).place(x=45, y=505)
    bridge_weight_entry = Entry(screen4, textvariable=bridge_weight, font=default_font)
    bridge_weight_entry.place(x=45, y=530)
    bridge_weight.set(group_list[5][0])

    Label(screen4, text="Broens kapasitet [g]", font=default_font).place(x=380, y=505)
    bridge_capacity_entry = Entry(screen4, textvariable=bridge_capacity, font=default_font)
    bridge_capacity_entry.place(x=380, y=530)
    bridge_capacity.set(group_list[5][1])

    Frame(screen4, height=1, width=800, bg="black").place(x=400, y=580, anchor="center")

    Button(screen4, text="Registrer", font=default_font, width=11, height=1, command=lambda: confirm_edit_group_dialog(old_group_number, group_number, students, bridge_weight, bridge_capacity)).place(
        x=600, y=610)

    Button(screen4, text="Slett gruppe", font=default_font, width=11, height=1, command=lambda: confirm_delete_group_dialog(old_group_number, students, bridge_weight, bridge_capacity)).place(
        x=45, y=610)

    Button(screen4, text="Avbryt", font=default_font, width=11, height=1, command=lambda: close_screen(screen4)).place(
        x=45, y=660)


def open_group_verify(correct_password, password, open_group_number, open_button):
    list_of_groups = os.listdir(group_folder)
    error_string = ""
    file_name = open_group_number.get() + ".txt"
    if file_name in list_of_groups:
        group_proceed = 1
    else:
        error_string = error_string + "Ugyldig gruppe. "
        group_proceed = 0

    if password.get() == correct_password:
        password_proceed = 1
    else:
        error_string = error_string + "Ugyldig passord."
        password_proceed = 0

    proceed = group_proceed * password_proceed
    if proceed != 0:
        open_button.configure(text='Passord godkjent', fg='#3E9651')
        edit_group_dialog(open_group_number.get())
    else:
        open_button.configure(text=error_string, fg='red')


def open_group_main(correct_password):
    global screen3
    open_group_number = StringVar()
    password = StringVar()

    screen3 = Toplevel(main_screen)
    screen3.title("Åpne gruppe")
    screen3.geometry("300x320")

    Label(screen3, text="Åpne gruppe").pack()

    Label(screen3, text="").pack()
    Label(screen3, text="Skriv inn ønsket gruppenummer").pack()
    group_entry = Entry(screen3, textvariable=open_group_number)
    group_entry.pack()

    Label(screen3, text="").pack()
    Label(screen3, text="").pack()

    Label(screen3, text="Skriv inn passord for å redigere").pack()
    password_entry = Entry(screen3,show="*", textvariable=password)
    password_entry.pack()
    Label(screen3, text="").pack()
    open_button = Button(screen3, text="Åpne", width=30, height=1, command=lambda: open_group_verify(correct_password, password, open_group_number, open_button))
    open_button.pack()

    Button(screen3, text="Avbryt", width=30, height=1, command=lambda: close_screen(screen3)).place(x=150, y=300, anchor="center")


def main_dialog():
    global default_font
    global main_screen
    global group_folder
    global max_group_number
    global label_group_register
    global label_group_edit

    width_window = 300.0  # width for the Tk root
    height_window = 500.0  # height for the Tk root

    default_font = ("Calibri", 12)
    group_folder = "Grupper"
    max_group_number = 100
    correct_password = "TKT"
    #TODO: Redo option
    main_screen = Tk()
    #TODO: Centre all windows
#    main_screen.geometry("300x500")
    width_screen = main_screen.winfo_screenwidth()  # width of the screen
    height_screen = main_screen.winfo_screenheight()  # height of the screen

    # calculate x and y coordinates for the Tk root window
    x = (width_screen / 2.0) - (width_window / 2.0)
    y = (height_screen / 2.0) - (height_window / 2.0)
    main_screen.geometry('%dx%d+%d+%d' % (width_window, height_window, x, y))
    main_screen.title("Labregistrering 1.1")

    label_group_register = []
    label_group_edit = []
    # TODO: Find better option for global label_group_register

    default_course = StringVar()
    course_list = ['', 'TKT4116', 'TKT4123', 'TKT4126']
    course_drop_list = OptionMenu(main_screen, default_course, *course_list)
    course_drop_list.config(width=15)
    default_course.set('')

    default_study = StringVar()
    study_list = ['', 'MTBYGG', 'MTENERG', 'MTING', 'MTIØT', 'MTMART', 'MTMT', 'MTPETR', 'MTPROD', 'MTTEKGEO', 'BGEOL', 'Øvrige']
    study_drop_list = OptionMenu(main_screen, default_study, *study_list)
    study_drop_list.config(width=15)
    default_study.set('')

    Label(text="Labregistrering 1.1", bg="grey", fg='#922428', width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Ny gruppe", height="2", width="30", command=lambda: new_group_dialog(default_course.get(), default_study.get())).pack()
    Label(text="").pack()
    Button(text="Åpne gruppe", height="2", width="30", command=lambda: open_group_main(correct_password)).pack()

    Frame(main_screen, height=1, width=300, bg="black").place(x=150, y=240, anchor="center")

    Label(main_screen, text = "Hurtigvalg (valgfritt):", font=default_font).place(x=150, y=260, anchor="center")

    Label(main_screen, text="Fagkode", font=default_font).place(x=75, y=290, anchor="center")
    course_drop_list.place(x=75, y=320, anchor="center")

    Label(main_screen, text="Studiekode", font=default_font).place(x=225, y=290, anchor="center")
    study_drop_list.place(x=225, y=320, anchor="center")

    Frame(main_screen, height=1, width=300, bg="black").place(x=150, y=340, anchor="center")

    write_file_button = Button(text="Skriv samlefil", height="2", width="30", command=lambda: write_summary_files(write_file_button))
    write_file_button.place(x=150, y=380, anchor="center")

    Button(text="Avslutt", height="2", width="30", command=lambda: main_screen.destroy()).place(x=150, y=450, anchor="center")

# TODO: Vurder antall-studenter-option
# TODO: Fagspesifikk rapport-skriver

    main_screen.mainloop()


main_dialog()
