from ast import Add
from msilib import add_stream
import tkinter
window = tkinter.Tk()
window.title("GUI")
Electricty_EmissionIndex=0.85
LPG_EmissionIndex=2.296
DIESEL_EmissionIndex=2.653 
PETROL_EmissionIndex=2.983



# creating a function called say_hi()

def Take_input():
    INPUT1 = int(inputtxt1.get("1.0", "end-1c"))
    INPUT2 = int(inputtxt2.get("1.0", "end-1c"))
    INPUT3 = int(inputtxt3.get("1.0", "end-1c"))
    INPUT4 = int(inputtxt4.get("1.0", "end-1c"))


   
    #print(INPUT1)
    Electricty=INPUT1*Electricty_EmissionIndex
    LPG=INPUT2*LPG_EmissionIndex
    DIESEL=INPUT3*DIESEL_EmissionIndex 
    PETROL=INPUT4*PETROL_EmissionIndex 
    float(Add) = Electricty + LPG + DIESEL + PETROL
    Output1.insert("KGs of CO2",Add)
   


l1 = tkinter.Label(text = "How much electricity do you use(in KWh/Yr)?")
inputtxt1 = tkinter.Text(window, height = 1, width = 10, bg = "grey")

l2 = tkinter.Label(text = "How much LPG do you use(in Kg/Yr)?")
inputtxt2 = tkinter.Text(window, height = 1, width = 10, bg = "grey")

l3 = tkinter.Label(text = "How much Diesel do you use(in Litres/Yr)?")
inputtxt3 = tkinter.Text(window, height = 1, width = 10, bg = "grey")

l4 = tkinter.Label(text = "How much Petrol do you use(in Litres/Yr)?")
inputtxt4 = tkinter.Text(window, height = 1, width = 10, bg = "grey")

Output1 = tkinter.Text(window, height = 5, width = 25, bg = "grey")
 
l1.pack()
inputtxt1.pack()

l2.pack()
inputtxt2.pack()

l3.pack()
inputtxt3.pack()

l4.pack()
inputtxt4.pack()


tkinter.Button(window, text = "Submit", command = Take_input).pack()


Output1.pack()
window.mainloop()