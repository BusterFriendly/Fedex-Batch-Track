from Tkinter import *
from track import evaluate
from trackitall import evaluate_excel, get_list
import os
import tkMessageBox
dirname, filename= os.path.split(os.path.abspath(__file__))




master = Tk()
master.wm_title('Batch tracking')

#master.iconbitmap(default=str(dirname)+'/favicon.ico')

frame = Frame(master)


frame.pack()

def callback():
    trackingnumber = e.get()
    if e.get() == "":
        print 'Must Enter Tracking Number'
    else: 
        sdate, adate, iship =  evaluate(e.get())
        if iship:
            print 'Package is Shipped!'
            print 'Shipped on %s' %sdate
            print 'Arrived on %s' %adate
            message = str(trackingnumber)[:10]+'...'+'           '+str(sdate)+'           '+str(adate)+'         '+str(iship)
            xx = Label(master, text=message)
            xx.pack()
            
        else:
            if sdate != "":
                print 'Package is on its way!'
                print 'Shipped on %s' %sdate
                print "Estimated Delivery on %s" %adate
                message = str(trackingnumber)[:10]+'...'+'           '+str(sdate)+'           '+str(adate)+'         '+str(iship)
                xx = Label(master, text=message)
                xx.pack()
            else:
                print "Sorry, No Shipment found"
                message = 'Sorry, No shipment found'
                tkMessageBox.showinfo(trackingnumber, message)

def doexcel():
    name = f.get()
    try:
        column = int(h.get()) -1 
    except ValueError:
        tkMessageBox.showinfo('Column number error: ', 'Please enter a Number for column number')
        pass

    outputname = str(p.get())
    if name != "" and column != "" and outputname != "" and isinstance(column,int): 
        evaluate_excel(name, column, outputname)
        message = str(name)+' analysis complete! Saved as: ' + str(outputname) + '.xls'
        tkMessageBox.showinfo('Export Success!', message)


headers = 'Tracking                   Shipped                    Delivery                 isDelivered'

w = Label(master, text='Single Tracking #')
v = Label(master, text='Excel File Name (.xls)')
z = Label(master, text='Column number of Tracking #s')
o = Label(master, text='Output File name')
data_h = Label(master, text=headers)

e = Entry(master)
f = Entry(master)
h = Entry(master)
p = Entry(master)

b = Button(master, text="track", width=10, command=callback)
g = Button(master, text="process", width=10, command=doexcel)
q = Button(master, text = 'quit', width=10,  command = quit)
separator = Frame(height=2, bd=1, relief=SUNKEN)
separator_1 = Frame(height=2, bd=1, relief=SUNKEN)
separator_2 = Frame(height=2, bd=1, relief=SUNKEN)
separator_3 = Frame(height=2, bd=1, relief=SUNKEN)


w.pack()
e.pack()
b.pack()


separator.pack(fill=X, padx=5, pady=5)

v.pack()
f.pack()
z.pack()
h.pack()

o.pack()
p.pack()

g.pack()
separator_1.pack(fill=X, padx=5, pady=5)
q.pack()

separator_2.pack(fill=X, padx=5, pady=5)
data_h.pack()
separator_3.pack(fill=X, padx=5, pady=5)
master.mainloop()
