from tkinter import *
import datetime

root = Tk()
root.maxsize(width=400, height=400)
root.minsize(width=400, height=400)

download_number = StringVar()
speed_number = StringVar()
var_dict = {0: 0, 1: 0, 2: 0, 3: 0}
my_list = []


# getting the button data
def get_buttons(var):
    var_dict[0] = var
    download = download_entry.get()
    var_dict[1] = download
    print(var_dict)


def get_buttons2(var):
    var_dict[2] = var
    speed = speed_entry.get()
    var_dict[3] = speed
    print(var_dict)
    for values in var_dict.values():
        my_list.append(values)
    my_time = download_time(my_list)
    output_panel(my_time)


def output_panel(input):
    my_time = input
    float_time = float(my_time)
    hours_to_add = datetime.timedelta(hours=float_time)
    current_time = datetime.datetime.now()
    output = "Your download should finish at {}\nIt looks like your download will take {} hours.".format(current_time + hours_to_add, hours_to_add)
    output_label = Label(output_frame, text=output, bg="pink", border=2, font=('Arial', 10))
    output_label.place(relx=0, rely=0, relwidth=1, relheight=1)


def download_time(argument_list):
    down_gb = argument_list[0]
    speed_gb = argument_list[2]
    down_num = float(argument_list[1])
    speed_num = float(argument_list[3])

    if down_gb == "GB" and speed_gb == "MB":
        time_hours = ((down_num * 1000) / speed_num) / 3600
    elif down_gb == "GB" and speed_gb == "KB":
        time_hours = ((down_num * (1000 * 1000)) / speed_num) / 3600
    elif down_gb == "MB" and speed_gb == "MB":
        time_hours = (down_num / speed_num) / 3600
    elif down_gb == "MB" and speed_gb == "KB":
        time_hours = ((down_num * 1000) / speed_num) / 3600
    elif down_gb == "KB" and speed_gb == "KB":
        time_hours = (down_num / speed_num) / 3600
    formatted = "{:.2f}".format(time_hours)
    return formatted


mainframe = Frame(root, width=400, height=400, bg="grey", border=15, relief=RAISED)
mainframe.pack()

# my frames to place widgets in
download_frame = Frame(mainframe, bg="grey", width=400, height=100)
download_frame.pack()
speed_frame = Frame(mainframe, bg="grey", width=400, height=100)
speed_frame.pack()
output_frame = Frame(mainframe, bg="grey", border=5, width=400, height=150, relief=SUNKEN)
output_frame.pack()

# the labels for the frames
download_label = Label(download_frame, text="Download Size", bg="grey", font=('Arial', 10))
download_label.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.15)
speed_label = Label(speed_frame, text="Speed", bg="grey", font=('Arial', 10))
speed_label.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.15)


download_entry = Entry(download_frame, textvariable=download_number, bg="pink")
# download_entry.bind('<Return>', get_data)
download_entry.place(relx=0.25, rely=0.3, relwidth=0.5)

speed_entry = Entry(speed_frame, textvariable=speed_number, bg="pink")
# speed_entry.bind('<Return>', get_data)
speed_entry.place(relx=0.25, rely=0.3, relwidth=0.5)

# the buttons for the file size types and data entry
button_kb = Button(download_frame, text="KB", width=6, height=1, bg="grey", command=lambda: get_buttons("KB"))
button_kb.place(relx=0.2, rely=0.7)
button_mb = Button(download_frame, text="MB", width=6, height=1, bg="grey", command=lambda: get_buttons("MB"))
button_mb.place(relx=0.4, rely=0.7)
button_gb = Button(download_frame, text="GB", width=6, height=1, bg="grey", command=lambda: get_buttons("GB"))
button_gb.place(relx=0.6, rely=0.7)
button_kb2 = Button(speed_frame, text="KB", width=6, height=1, bg="grey", command=lambda: get_buttons2("KB"))
button_kb2.place(relx=0.2, rely=0.7)
button_mb2= Button(speed_frame, text="MB", width=6, height=1, bg="grey", command=lambda: get_buttons2("MB"))
button_mb2.place(relx=0.4, rely=0.7)
button_gb2 = Button(speed_frame, text="GB", width=6, height=1, bg="grey", command=lambda: get_buttons2("GB"))
button_gb2.place(relx=0.6, rely=0.7)

root.mainloop()
