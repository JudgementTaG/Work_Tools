import os 
import tkinter as tk
from os import system

dictionary = {
    "A" : "Alpha",
    "B" : "Bravo",
    "C" : "Charlie",
    "D" : "Delta",
    "E" : "Echo",
    "F" : "Foxtrot",
    "G" : "Golf",
    "H" : "Hotel",
    "I" : "Indigo",
    "J" : "Juliet",
    "K" : "Kilo",
    "L" : "Lima",
    "M" : "Mike",
    "N" : "November",
    "O" : "Oscar",
    "P" : "Papa",
    "Q" : "Quebec",
    "R" : "Romeo",
    "S" : "Sierra",
    "T" : "Tango",
    "U" : "Uniform",
    "V" : "Victor",
    "W" : "Whiskey",
    "X" : "X-Ray",
    "Y" : "Yankee",
    "Z" : "Zulu",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero",
    "!" : "Exclaimation Mark",
    '"' : "Double Quotes",
    "£" : "Pound Sign",
    "$" : "Dollar Sign",
    "¿" : "Inverted Question Mark"

}
window = tk.Tk()

def transmute():
    code = input_field.get()
    converted1 = converted2 = converted3 = converted4 = converted5 = converted6 = ""
    failed = []
    count = 0
    for letter in code:
        try:
            if count < 4:
                converted1 += str(dictionary[letter.upper()]) + ", "
            elif 3 < count < 8:
                converted2 += str(dictionary[letter.upper()]) + ", "
            elif 7 < count < 12:
                converted3 += str(dictionary[letter.upper()]) + ", "
            elif 11 < count < 16:
                converted4 += str(dictionary[letter.upper()]) + ", "
            elif 15 < count < 20:
                converted5 += str(dictionary[letter.upper()]) + ", "
            elif 19 < count < 24:
                converted6 += str(dictionary[letter.upper()]) + ", "
            count += 1
        except:
            failed.append(f"!!!  {letter} not found   !!!")

    for index,convert in enumerate([converted1,converted2,converted3,converted4,converted5,converted6]):
        if convert != "":
            if index == 0:    
                output_field.insert(index=f"{index}.0",chars=f"{convert}")
            else:
                output_field.insert(index=f"{index+1}.0",chars=f"\n{convert}")

    for fail in failed:
        output_field.insert(index="6.0",chars=f"\n{fail}")

def clear():
    input_field.delete("0",tk.END)
    output_field.delete("1.0",tk.END)

lines = [tk.Label(text="Phone Companion",height= 1,font=("Arial",14))]
buffer = [tk.Label(text="  "),tk.Label(text="  ")]
buttons = [tk.Button(text="Convert",width= 9,height= 2,command=transmute),tk.Button(text=" Clear ",width= 9,height= 2,command=clear)]


input_field = tk.Entry(width=40)
input_field.grid(row=0,column=1)

output_field = tk.Text(height= 6, width=40)
output_field.grid(row=1, column=1)

lines[0].grid(row=0,column=0)
for count,button in zip(enumerate(buttons),buttons):
    try:
        button.grid(row=count[0] + 1,column=0)
    except:
        pass

buffer[0].grid(row=0,column=2)
buffer[1].grid(row=3,column=0)
    
window.mainloop()