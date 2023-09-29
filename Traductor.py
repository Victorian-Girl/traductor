from tkinter import *
import tkinter
from translate import Translator


#Translator function
def translate():
    try:
        translator = Translator(from_lang=lan1.get(), to_lang=lan2.get())
        translation = translator.translate(var.get())
        var1.set(translation)
    except:
        label = Label(app, text="Enter valid input", fg="red", font=("Arial", 10, "bold"))
        label.grid(row=4, column=7)


# main window
app = tkinter.Tk()
app.geometry("490x150+700+250")
app.minsize(490, 150)
app.maxsize(490, 150)
app.title("Translator")


#variables for dropdown list
lan1 = StringVar(app)
lan2 = StringVar(app)

#choices to show in dropdown menu
choices = {'English', 'Hindi', 'Gujarati', 'Spanish', 'German', 'French', 'Portuguese', 'Chinese', 'Japanese'}
#default selection for dropdownlists
lan1.set('English')
lan2.set('French')

#creating dropdown and arranging in the grid
lan1menu = OptionMenu(app, lan1, *choices)
Label(app, text="Select a language").grid(row=0, column=1)
lan1menu.grid(row=1, column=1)

lan2menu = OptionMenu(app, lan2, *choices)
Label(app, text="Select a language").grid(row=0, column=9)
lan2menu.grid(row=1, column=9)

#Entry Box to take user input
Label(app, text="Enter text").grid(row=2, column=0)
var = StringVar()
textbox = tkinter.Entry(app, width=30, textvariable=var).grid(row=2, column=1)

#Entry to show output
#label can also be used
Label(app, text="Output").grid(row=2, column=7)
var1 = StringVar()
textbox1 = tkinter.Entry(app, width=30, textvariable=var1).grid(row=2, column=9)

#creating a button to call Translator function
b = Button(app, text='Translate', command=translate).grid(row=3, column=7)

app.mainloop()

