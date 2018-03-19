import csv
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
from collections import OrderedDict
save_png = True


def plot(x, y, z):
    # Get Name of Headers and Remove them to keep Data Fresh
    x_header, y_header, z_header = x[0], y[0], z[0]
    x, y, z = x[1:], y[1:], z[1:]
    plt.title(x_header + ' vs. ' + y_header + ' vs. ' + z_header)
    plt.xlabel(x_header)
    plt.ylabel(y_header)
    # Remove Blank Values from List
    n = 0
    while n < len(x):
        if x[n] == '':
            del x[n]
            del y[n]
            del z[n]
        else:
            n += 1
    # Convert List to Numerical Values
    x = [float(i) for i in x]
    y = [float(n) for n in y]
    i = 0

    while i < len(x):
        plt.scatter(x[i], y[i], label=z[i])
        i += 1
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())
    plt.show()


def get(file_location, x_row, y_row, z_row):
    x, y, z = [], [], []
    with open(file_location, encoding='utf-8-sig') as csvfile:
        print('Receiving Data from CSV...')
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            x.append(row[x_row])
            y.append(row[y_row])
            z.append(row[z_row])
    print("Plotting...")
    plot(x, y, z)


# Finding the File Location for the CSV
def find():
    global file_location
    filename = askopenfilename()
    file_location = str(filename)


# When User hits finished, get the values from GUI and get the data
def finished():
    x_row = int(xRowEntry.get()) - 1
    y_row = int(yRowEntry.get()) - 1
    z_row = int(zRowEntry.get()) - 1
    get(file_location, x_row, y_row, z_row)


# Setup the GUI
if __name__ == '__main__':
    top = tkinter.Tk()
    top.resizable(width=False, height=False)
    top.geometry('{}x{}'.format(500, 500))

    xRow = Label(top, text="X Row")
    xRowEntry = Entry(top, bd=2)
    xRowEntry.insert(0, '')
    yRow = Label(top, text="Y Row")
    yRowEntry = Entry(top, bd=2)
    yRowEntry.insert(0, '')
    zRow = Label(top, text="Z Row")
    zRowEntry = Entry(top, bd=2)
    zRowEntry.insert(0, '')

    Find = tkinter.Button(top, text="Find CSV", command=find)
    Done = tkinter.Button(top, text="Done", command=finished)
    title = tkinter.Label(top, text="UP Stat Graphing", font=("Helvetica", 30))

    # Place Everything on Canvas Window
    Find.place(relx=0.15, rely=0.3)
    Done.place(relx=0.8, rely=0.8)
    title.place(relx=0.15, rely=0.1)
    xRow.place(relx=0.125, rely=0.45)
    xRowEntry.place(relx=0.15, rely=0.4, width=40)
    yRow.place(relx=0.3, rely=0.45)
    yRowEntry.place(relx=0.3, rely=0.4, width=40)
    zRow.place(relx=0.475, rely=0.45)
    zRowEntry.place(relx=0.475, rely=0.4, width=40)
    top.mainloop()
