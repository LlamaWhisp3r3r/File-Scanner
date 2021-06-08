"""File Scanner & Copier

This program copies and pastes pictures from the computer to a usb drive
The drive will need to be porvided via entering it in the terminal upon startup

Created by:
Nathan Turner

Last Updated By:
7-2-2019

Contact Info:
nathanturner270@gmail.com

Feel free to edit the code as you feel. This program is free to use and easy to use.

"""






from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.messagebox
import time
import os
from os.path import expanduser
import shutil





the_list = {
            'Pictures': ['.jpg', '.tif', '.png', '.gif'],
            'Documents': ['.doc', '.docx', '.pdf'],
            'Powerpoints': ['.ppt', '.pps', '.pptx', '.ppsx', '.sldx'],
            'Excels': ['.xls', '.xlsx', '.xlw']}    




class Main:

    """

    Main Class that holds all the code.
    Easier to trasfer variables

    """

    def __init__(self, master):
        #Creates main GUI Interface
        frame = Frame(master)
        frame.pack()

    def startup(self):

           #Used a frame to pack the stuff into so I could easily destroy it
        self.main_frame = Frame(root)
        
        self.lbl = Label(self.main_frame, 
                         text='File Scanner', 
                         font='Times 32', 
                         anchor=N)
                         
        self.lbl2 = Label(self.main_frame,
                          text='Version 1.1',
                          font='Times 12',
                          anchor=N)
        
        self.lbl3 = Label(self.main_frame,
                          text='Created By:  Nathan Turner\n        AKA. MC Sunburn\n',
                          anchor=N)
                          
        self.bt = Button(self.main_frame,
                         text='Continue',
                         command=self.setupScreen)
                         
        self.bt2 = Button(self.main_frame,
                          text='Quit',
                          command=root.destroy)
                          
        self.space = Label(self.main_frame,
                           text='',
                           width=50)
        

        self.main_frame.pack()
        self.lbl.pack()
        self.lbl2.pack()
        self.lbl3.pack()
        self.space.pack()
        self.bt.pack(side=LEFT)
        self.bt2.pack(side=RIGHT)




    def setupScreen(self):
    
        """
        
        Startup screen. Just checks for avaiable USB devices in a pretty easy way
        Than puts the active one's on the screen
        
        """
    
    
        self.iseusb = os.path.isdir('E:/')
        self.isdusb = os.path.isdir('D:/')
        self.isfusb = os.path.isdir('F:/') 
        self.isgusb = os.path.isdir('G:/')
        
    
        self.main_frame.destroy()
        
        self.startframe = Frame(root)
        self.startframe.pack()
        
        self.toplbl = Label(self.startframe,
                            text="File Scanner",
                            font='Times 32',
                            anchor=N,
                            justify=CENTER)
        
        self.toplbl.pack()
        
        self.line = Label(self.startframe,
                          text='-'*50)
        self.line.pack()
        
        self.sublbl = Label(self.startframe,
                            text='\nPlease Select The USB Drive You Want To Copy To\n\tPick One Or Else It Will Crash\n')
        self.sublbl.pack()
            
        
        #Checks to see if any usb's are avaiable
        if self.iseusb == True:
        
            self.checkvar1 = IntVar()
            
            self.echeck = Checkbutton(self.startframe,
                                      text='E:/',
                                      variable=self.checkvar1)
            self.echeck.pack()
            
            
            
        if self.isdusb == True:
            
            self.checkvar2 = IntVar()
            
            self.dcheck = Checkbutton(self.startframe,
                                      text='D:/',
                                      variable=self.checkvar2)
            self.dcheck.pack()
            
            
            
        if self.isfusb == True:
            
            self.checkvar3 = IntVar()
            
            self.fcheck = Checkbutton(self.startframe,
                                      text='F:/',
                                      variable = self.checkvar3)
            self.fcheck.pack()
            
        
        if self.isgusb == True:
            
            self.checkvar4 = IntVar()
            
            self.gcheck = Checkbutton(self.startframe,
                                      text='G:/',
                                      variable= self.checkvar4)
            self.gcheck.pack()
            
            
        
        self.space = Label(self.startframe,
                           text='',
                           width=50)
        self.space.pack()
        
        
        self.ac = Button(self.startframe, text='Accept', command=self.usbstart)
        self.ac.pack(side=LEFT)
        
        self.de = Button(self.startframe, text='Quit', command=root.destroy)
        self.de.pack(side=RIGHT)

    
    def usbstart(self):
    
        """
        
        Simple logic that checks to see if the check boxes are checked
        If not it doesn't do anything
        
        """
        
        
        
        if self.iseusb == True: 
            if self.checkvar1.get() == 1:
            
                eusb_path = 'E:/'
                self.documentchose(eusb_path)
            
        if self.isdusb == True:
            if self.checkvar2.get() == 1:
        
                dusb_path = 'D:/'
                self.documentchose(dusb_path)
            
        if self.isfusb == True: 
            if self.checkvar3.get() == 1:
        
                fusb_path = 'F:/'
                self.documentchose(fusb_path)
                    
        if self.isgusb == True:
            if self.checkvar4.get() == 1:
                
                gusb_path = 'G:/'
                self.documentchose(gusb_path)
            
            
            
      

    def documentchose(self, usb_path):
    
        """
        
        Samething as the usb start screen
        lets you pick the option of files you want to copy
        Must only pic one or else...
        
        """
        
        self.usb_path = usb_path

        
        self.startframe.destroy()
        
        self.docframe = Frame(root)
        self.docframe.pack()
        
        self.toplbl = Label(self.docframe,
                            text="File Scanner",
                            font='Times 32',
                            anchor=N,
                            justify=CENTER)
        
        self.toplbl.pack()
        
        self.line = Label(self.docframe,
                          text='-'*50)
        self.line.pack()
        
        
        self.mes = Label(self.docframe,
                         text="\nPlease Select What You Want To Copy\n        Pick One Or Else It Will Crash\n")
        self.mes.pack()
        
        self.docvar = IntVar()
        self.docbt = Checkbutton(self.docframe, text='Documents', variable=self.docvar)
        self.docbt.pack()
        
        self.picvar = IntVar()
        self.picbt = Checkbutton(self.docframe, text='Pictures', variable=self.picvar)
        self.picbt.pack()
        
        self.excvar = IntVar()
        self.excbt = Checkbutton(self.docframe, text='Excel Sheets', variable=self.excvar)
        self.excbt.pack()
        
        self.ppvar = IntVar()
        self.ppbt = Checkbutton(self.docframe, text='Power Points', variable=self.ppvar)
        self.ppbt.pack()
        
        self.space = Label(self.docframe,
                           text='',
                           width=50)
        self.space.pack()
        
        self.accept = Button(self.docframe, text='Accept', command=self.doccheck)
        self.accept.pack(side=LEFT)
        self.quit = Button(self.docframe, text='Quit', command=root.destroy)
        self.quit.pack(side=RIGHT)

    
    def doccheck(self):
    
        if self.docvar.get() == 1:
            
            self.filecreate('Documents')
            
        if self.excvar.get() == 1:

            self.filecreate('Excels')
            
        if self.ppvar.get() == 1:
            
            self.filecreate('Powerpoints')
            
        if self.picvar.get() == 1:
            
            self.filecreate('Pictures')
    

    def filecreate(self, doctype):
    
        """
        
        Creates a file of the users choosing.
        Than checks to see if that works. If not
        than the user as to try something else
        
        """
        
        self.doctype = doctype
        
        self.docframe.destroy()
        
        self.fileframe = Frame(root)
        self.fileframe.pack()
        
        self.toplbl = Label(self.fileframe,
                            text="File Scanner",
                            font='Times 32',
                            anchor=N,
                            justify=CENTER)
        
        self.toplbl.pack()
        
        self.line = Label(self.fileframe,
                          text='-'*50)
        self.line.pack()
         
        self.lbl = Label(self.fileframe, text='\nPlease Enter The Name That You Want Your Backup File To Have\n\n')
        self.lbl.pack()
        
        self.lbl2 = Label(self.fileframe, text='File Name ')
        self.lbl2.pack(side=LEFT)
        
        self.en = Entry(self.fileframe)
        self.en.pack(side=LEFT)
        
      
        
        self.accept = Button(self.fileframe, text='Accept', command=self.entrycheck)
        self.accept.pack(side=LEFT)
        self.quit = Button(self.fileframe, text='Quit', command=root.destroy)
        self.quit.pack(side=RIGHT)
        

         
         
    def entrycheck(self):
    
        """
        Checks the name the user gave the machine
        than see's if it's already taken
        """
    
            
        
        self.filepath = self.usb_path + self.en.get()
        self.homepath = expanduser("~")
        isdir = os.path.isdir(self.filepath)
        
        if isdir == True:
            
            tkinter.messagebox.showerror('ERROR', 'FILE ALREADY EXISTS\nPLEASE USE A DIFFERENT NAME')
            self.fileframe.destroy()
            self.filecreate(self.doctype)
            
        
        os.mkdir(self.filepath)
        self.walk()
        
        
    def walk(self):
    
        """
        Prep for the main walking machine.
        had to add it before because it wasn't loading because of the for loop
        in the main walking machine
        """
    
        self.fileframe.destroy()
        
        self.walkframe = Frame(root)
        self.walkframe.pack()
        
        self.toplbl = Label(self.walkframe,
                            text="File Scanner",
                            font='Times 32',
                            anchor=N,
                            justify=CENTER)
        
        self.toplbl.pack()
        
        self.line = Label(self.walkframe,
                          text='-'*50)
        self.line.pack()
        
        self.lbl = Label(self.walkframe, text='\nScanning For Files....\nThis May Take A Little Bit\nOnce You Hit Copy\n', justify=CENTER)
        self.lbl.pack()
        
        pb = ttk.Progressbar(self.walkframe, orient="horizontal", length=200, mode="determinate")
        pb.pack()
        pb.start()
        
        
        
        self.file = the_list[self.doctype]

        self.bt = Button(self.walkframe, text='Copy Files', command=self.walking)
        self.bt.pack(side=LEFT)
        self.bt2 = Button(self.walkframe, text='Cancel', command=root.destroy)
        self.bt2.pack(side=RIGHT)
        
        
  
        
    def walking(self):
    
        """
        
        main walking brain. It walks the whole path of every directory and file
        in the current user.
        
        """
        
    
        os.chdir(self.homepath)
    
        new_path = self.homepath + '\.webrendererswing6'        #these are the directories that I don't want it to scan
        bad_path = self.homepath + '\AppData'
        
        for dirpath, dirnames, filenames in os.walk(self.homepath):
        
            if bad_path not in dirpath and new_path not in dirpath:
     
                for files in filenames:        
                
                    fm = os.path.splitext(files)    #checks if the end of the file as the same ending as the files we are looking for.       
                    is_file = fm[1]
                    file_source = os.path.join(dirpath, files)
                

                
                    if is_file in self.file:     
                
                        try:
                            #copies file if possible, if not than it throws an exception and keeps on going
                            shutil.copy2(file_source, self.filepath)
                            
                        
                        
                        except Exception:
                            continue
        
        
                
        self.final()



    def final(self):
    
        """
        
        The Final frame that says thank you and goodbye
        if user wants to restart than it goes to restart function
        
        """
        
        self.walkframe.destroy()
        
        self.finallyframe = Frame(root)
        self.finallyframe.pack()
        
        self.toplbl = Label(self.finallyframe,
                            text="File Scanner",
                            font='Times 32',
                            anchor=N,
                            justify=CENTER)
        
        self.toplbl.pack()
        
        self.line = Label(self.finallyframe,
                          text='-'*50)
        self.line.pack()
        
       
        self.lbl = Label(self.finallyframe, text='\nThank You For Using File Scanner\n')
        self.lbl.pack()        
        
        self.bt = Button(self.finallyframe, text='Restart', command=self.restart)
        self.bt.pack(side=LEFT)
        self.bt2 = Button(self.finallyframe, text='Close', command=root.destroy)
        self.bt2.pack(side=RIGHT)
        
        
    def restart(self):
    
        #I only needed to add this because i couldn't call a functions that hasn't been called yet
        
        self.finallyframe.destroy()
        self.startup()


        
        
        
        

 
        
#Initializes the root and the main frame of the whole program than puts everything in a loop        
root = Tk()
start = Main(root)
start.startup()
root.mainloop()
