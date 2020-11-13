from tkinter import *
import tkinter.messagebox as tsmg

#! Function and Element Details 
def get_details() :

    element = e1_value.get()
    periodic_dict = {"Hydrogen":"Symbol: H\nElement Number: 01 \nNumber Of Protons/Electrons: 01\nNumber Of Neutrons: 0\nDistribution Of Electrons: 1",
           "Helium":"Symbol: He\nElement Number: 02 \nNumber Of Protons/Electrons: 02\nNumber Of Neutrons: 02\nDistribution Of Electrons: 2",
           "Lithium":"Symbol: Li\nElement Number: 03 \nNumber Of Protons/Electrons: 03\nNumber Of Neutrons: 04\nDistribution Of Electrons: 2, 1",
           "Barylium":"Symbol: Be\nElement Number: 04 \nNumber Of Protons/Electrons: 04\nNumber Of Neutrons: 05\nDistribution Of Electrons: 2, 2",
           "Boron":"Symbol: B\nElement Number: 05 \nNumber Of Protons/Electrons: 05\nNumber Of Neutrons: 06\nDistribution Of Electrons: 2, 3",
           "Carbon":"Symbol: C\nElement Number: 06 \nNumber Of Protons/Electrons: 06\nNumber Of Neutrons: 06\nDistribution Of Electrons: 2, 4",
           "Nitrogen":"Symbol: N\nElement Number: 07 \nNumber Of Protons/Electrons: 07\nNumber Of Neutrons: 07\nDistribution Of Electrons: 2, 5",
           "Oxygen":"Symbol: O\nElement Number: 08 \nNumber Of Protons/Electrons: 08\nNumber Of Neutrons: 08\nDistribution Of Electrons: 2, 6",
           "Florine":"Symbol: F\nElement Number: 09 \nNumber Of Protons/Electrons: 09\nNumber Of Neutrons: 10\nDistribution Of Electrons: 2, 7",
           "Niyon":"Symbol: Ne\nElement Number: 10 \nNumber Of Protons/Electrons: 10\nNumber Of Neutrons: 10\nDistribution Of Electrons: 2, 8",
           "Sodium":"Symbol: Na\nElement Number: 11 \nNumber Of Protons/Electrons: 11\nNumber Of Neutrons: 12\nDistribution Of Electrons: 2, 8, 1",
           "Magnesium":"Symbol: Mg\nElement Number: 12\nNumber Of Protons/Electrons: 12\nNumber Of Neutrons: 12\nDistribution Of Electrons: 2, 8, 2",
           "Aluminum":"Symbol: Al\nElement Number: 13\nNumber Of Protons/Electrons: 13\nNumber Of Neutrons: 14\nDistribution Of Electrons: 2, 8, 3",
           "Silicon":"Symbol: Si\nElement Number: 14\nNumber Of Protons/Electrons: 14\nNumber Of Neutrons: 14\nDistribution Of Electrons: 2, 8, 4",
           "Phosphorus":"Symbol: P\nElement Number: 15\nNumber Of Protons/Electrons: 15\nNumber Of Neutrons: 16\nDistribution Of Electrons: 2, 8, 5",
           "Sulfur":"Symbol: S\nElement Number: 16\nNumber Of Protons/Electrons: 16\nNumber Of Neutrons: 16\nDistribution Of Electrons: 2, 8, 6",
           "Chlorine":"Symbol: Cl\nElement Number: 17\nNumber Of Protons/Electrons: 17\nNumber Of Neutrons: 18\nDistribution Of Electrons: 2, 8, 7",
           "Argon":"Symbol: Ar\nElement Number: 18\nNumber Of Protons/Electrons: 18\nNumber Of Neutrons: 22\nDistribution Of Electrons: 2, 8, 8",
           "Potassium":"Symbol: K\nElement Number: 19\nNumber Of Protons/Electrons: 19\nNumber Of Neutrons: 20\nDistribution Of Electrons: 2, 8, 8, 1",
           "Calcium":"Symbol: Ca\nElement Number: 20\nNumber Of Protons/Electrons: 20\nNumber Of Neutrons: 20\nDistribution Of Electrons: 2, 8, 8, 2"}

    if element in periodic_dict : 
        tsmg.showinfo(f'{element}', periodic_dict[element])
    else : 
        tsmg.showerror('Error!', 'Element Not Found!')
#! Setting Base Gui
gui = Tk()
gui.geometry('500x150')
gui.title('Peroidic Table')

#! Setting Frame 1, Label and Entry widget
f1 = Frame(gui)
Label(f1, text = "Enter A Element name", font = 'hack 10 italic').pack(fill = X)
e1_value = StringVar()
e1 = Entry(f1, textvariable = e1_value, justify = CENTER, font = 'hack 16 italic')
e1.pack()
Button(f1, text = 'Get Details', command = get_details).pack(pady = 10)
f1.pack(pady = 20)

#! Setting Icon
icon = PhotoImage(file = "perTable.png")
gui.wm_iconphoto(False, icon)
gui.configure(bg = 'black')

gui.mainloop()