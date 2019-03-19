import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
'''Needs working on the find frm line number 172'''

class LiquidText:
    root = Tk()

    # default window width and height
    thisWidth = 300
    thisHeight = 300
    thisTextArea = Text(root)
    thisMenuBar = Menu(root)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.root.wm_iconbitmap("C:\\Users\\shrey\\Desktop\\L.png")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.root.title("Untitled - LiquidText")

        # Center the window
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.thisHeight / 2)

        # For top and bottom
        self.root.geometry('%dx%d+%d+%d' % (self.thisWidth,self.thisHeight,left, top))

        # To make the textarea auto resizable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.thisTextArea.grid(sticky=N + E + S + W)

        #open new file
        self.thisFileMenu.add_command(label="New",command=self.__newFile)

        #open a already existing file
        self.thisFileMenu.add_command(label="Open",command=self.__openFile)

        # save current file
        self.thisFileMenu.add_command(label="Save",command=self.__saveFile)

        #create a line in the dialog
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit",command=self.__quitApplication)
        self.thisMenuBar.add_cascade(label="File",menu=self.thisFileMenu)

        #cut
        self.thisEditMenu.add_command(label="Cut",command=self.cut)

        #copy
        self.thisEditMenu.add_command(label="Copy",command=self.copy)

        #paste
        self.thisEditMenu.add_command(label="Paste",command=self.paste)

        #find
        self.thisEditMenu.add_command(label="Find", command=self.find)

        #editing
        self.thisMenuBar.add_cascade(label="Edit",menu=self.thisEditMenu)

        # To create a feature of description of the LiquidText
        self.thisHelpMenu.add_command(label="About LiquidText",command=self.__showAbout)
        self.thisMenuBar.add_cascade(label="Help",menu=self.thisHelpMenu)

        self.root.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

    def __quitApplication(self):
        self.root.destroy()
        # exit()

    def __showAbout(self):
        showinfo("LiquidText", "This samll LiquidText was developed by Shreyas K Shastry")

    def __openFile(self):

        self.file = askopenfilename(defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # Try to open the file
            # set the window title
            self.root.title(os.path.basename(self.file) + " - LiquidText")
            self.thisTextArea.delete(1.0, END)

            file = open(self.file, "r")

            self.thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.root.title("Untitled - LiquidText")
        self.file = None
        self.thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files", "*.*"),("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:

                # Try to save the file
                file = open(self.file, "w")
                file.write(self.thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.root.title(os.path.basename(self.file) + " - LiquidText")


        else:
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def find(self):
        self.thisTextArea.event_generate("<<Find>>")
        '''win = self.root
        win.wm_title("Window")

        l = self.root.Label(win, text="Input")
        l.grid(row=0, column=0)

        b = self.root.Button(win, text="Okay", command=win.destroy)
        b.grid(row=1, column=0)'''

    def run(self):

        # Run main application
        self.root.mainloop()

    # Run main application


LiquidText = LiquidText(width=600, height=400)
LiquidText.run()
