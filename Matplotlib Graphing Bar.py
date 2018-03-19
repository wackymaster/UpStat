import csv
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename

save_png = True


def plot(x):
    # Get Name of Headers and Remove them to keep Data Fresh
    x_header = x[0]
    x = x[1:]
    # Remove Blank Values from List
    n = 0
    while n < len(x):
        if x[n] == '' or x[n] == '***':
            del x[n]
        else:
            n += 1
    x_values = list(set(x))
    objects = []
    i = 0

    while i < len(x_values):
        a = 0
        occurrences = 0
        while a < len(x):
            if x[a] == x_values[i]:
                occurrences += 1
            a += 1
        objects.append(occurrences)
        i += 1
    # Convert List to Numerical Values
    plt.title(x_header + ' Bar Graph')
    plt.bar(x_values, objects)
    plt.show()


def get(file_location, x_row):
    x = []
    with open(file_location, encoding='utf-8-sig') as csvfile:
        print('Receiving Data from CSV...')
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            x.append(row[x_row])
    print("Plotting...")
    plot(x)


# Finding the File Location for the CSV
def find():
    global file_location
    filename = askopenfilename()
    file_location = str(filename)


# When User hits finished, get the values from GUI and get the data
def finished():
    x_row = int(xRowEntry.get()) - 1
    get(file_location, x_row)


# Setup the GUI
if __name__ == '__main__':
    top = tkinter.Tk()
    top.resizable(width=False, height=False)
    top.geometry('{}x{}'.format(500, 500))

    xRow = Label(top, text="X Row")
    xRowEntry = Entry(top, bd=2)
    xRowEntry.insert(0, '')

    Find = tkinter.Button(top, text="Find CSV", command=find)
    Done = tkinter.Button(top, text="Done", command=finished)
    title = tkinter.Label(top, text="UP Stat Graphing", font=("Helvetica", 30))

    # Place Everything on Canvas Window
    Find.place(relx=0.15, rely=0.3)
    Done.place(relx=0.8, rely=0.8)
    title.place(relx=0.15, rely=0.1)
    xRow.place(relx=0.125, rely=0.45)
    xRowEntry.place(relx=0.15, rely=0.4, width=40)

    top.mainloop()
