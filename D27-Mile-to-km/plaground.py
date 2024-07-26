from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window =  Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=200)

# Label
my_label = Label(text="I am Label", font =("Arial", 24,"bold"))
# my_label.pack() # (side="Left") (side= "bottom") (expand="True")
# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=50,pady=50)
# my_label.grid(column=0,row=0)

# button
button = Button(text="Click me", command=button_clicked)
button.grid(column=1,row=1)
# can not use pack if we have grid function used

new_button = Button(text="Click me", command=button_clicked)
new_button.grid(column=2,row=0)

# entries
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)

# entry = Entry(width=30)
# entry.insert(END, string="some text to begin with.")
# print(entry.get())
# entry.pack()

# text
# text = Text(height=5,width=30)
# text.focus()
# text.insert(END, "Example of multi-line text entry.")
# print(text.get("1.0",END))
#
# text.pack()

# #spinbox
# def spinbox_used():
#     print(spinbox.get())
# spinbox=  Spinbox(from_=0,to=10,width=5,command=spinbox_used)
# spinbox.pack()
#
# # scale
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100,command=scale_used)
# scale.pack()
#
# # checkbutton
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is on?",variable=checked_state,command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()


window.mainloop()
