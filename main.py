'''
the main file
main author:ben song
other files author: @techwithtim
requirements: look at requirements.txt
'''


from tkinter import *
from tkinter.constants import *
from network import Network
import server

network = Network()
reply = network.send('Hello').decode()

root = Tk()
root.title('FreeChat 1.0')
root.configure(background='midnight blue')
chat = 'freechat.txt'

def send():
    network.send(write.get()).decode()
    text.insert(END, str(write.get()) + '\n')
    with open(chat, 'w') as file:
        file.write(write.get())
def random_chat():
    global chat
    text.delete(0.0, END)
    chat = 'random_chat.txt'
    with open(chat) as file:
        for line in file:
            text.insert(END, str(line) + '\n')
def free_chat():
    global chat
    text.delete(0.0, END)
    chat = 'freechat.txt'
    with open(chat) as file:
        for line in file:
            text.insert(END, str(line) + '\n')

text = Text(root, width=75, height=75, font=('Arial', 35))
text.grid(row=1, column=1)
write = Text(root, width=50, font=('Arial', 35))
write.grid(row=0, column=1, columnspan=2)
submit = Button(root, text='Submit', command=send())
submit.grid(row=1, column=2)
sidebar = Frame(root, width=44, bd=10)
sidebar.grid(row=0, column=0, rowspan=2)
btnfree = Button(sidebar, bd=10, font=('Arial', 35), text='Free chat', width=40, height=30, command=free_chat)
btnfree.grid(row=0, column=0)
btnrd = Button(sidebar, bd=10, font=('Arial', 35), text='Random chat', width=40, height=30, command=random_chat)
btnrd.grid(row=0, column=1)



root.mainloop()
