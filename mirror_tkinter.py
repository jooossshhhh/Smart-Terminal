# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 11:15:23 2022

@author: josh.smith
"""

# from tkinter import *

# class Window(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master = master
        
#         #widget can take whole window
#         self.pack(fill=BOTH,expand=1)
#         #self.grid(row=1,column=2)
#         #create the button and link it to def below
#         exitButton = Button(self,text='Exit',command = self.clickExitButton)
        
#         #coords for button
#         exitButton.place(x=160,y=200)
        
#         #text labels
#         text = Label(self,text='here we go')
#         text.place(x=70,y=90)
#     def clickExitButton(self):
#         exit()

# root= Tk()
# app = Window(root)
# root.wm_title('Tkinter window')
# root.geometry('320x200')

# root.mainloop()

import tkinter as tk
import pyautogui
import mirror_webscraping

#from star_trek import visual

w,t = mirror_webscraping.webscrape('Nashville')
# wh = pyautogui.size()

# window = tk.Tk()
#Show what key user just pressed on screen
# def handle_keypress(event):
#     """Print the character associated to the key pressed"""
#     print(event.char)
#     """print the typed character onto the gui"""
#     label = tk.Label(text='%s'%(event.char))
#     label.grid(row = 0,column = 0,sticky='n')
#Exit out of GUI   
# def clickExitButton(event):
#     print('yes')
#     window.destroy()
    
# window.columnconfigure(0,minsize=200)
# window.rowconfigure([0,1], minsize = 100)
# exitButton = tk.Button(text='exit')
# exitButton.grid(row = 1,column = 0,sticky='s')
# #close out of the window with exit button
# exitButton.bind('<Button-1>',clickExitButton)
# # Bind keypress event to handle_keypress()
# window.bind("<Key>", handle_keypress)

# window.mainloop()

window = tk.Tk()
# #for i in t:
window.columnconfigure(0,minsize = 300)#wh.width)
window.rowconfigure([0,1],minsize=200)#wh.height-300)
strin1=''
for j in w:
    strin1 +=j+'\n'
label2 = tk.Label(text=strin1, bg="black", fg="green")
label2.grid(row = 0, column =0, sticky = 'nw')
strin=''
for i in t:
    strin += i+'\n'
label1 = tk.Label(text=strin, bg="black", fg="green")
label1.grid(row = 1, column =0, sticky = 'sw')

#label1 = tk.Label(text = visual())
#label2.grid(row = 1, column = 0)

window.mainloop()

