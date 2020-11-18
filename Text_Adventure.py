import tkinter as tk

class Text_Dungeon(tk.Frame):
    def __init__(self, master=None):    
        self.maxrowval = 4
        self.minrowval = 0
        self.maxcolval = 1
        self.mincolval = 0
        
        self.minput = 0
        
        self.atext = tk.StringVar()
        self.btext = tk.StringVar()
        self.ctext = tk.StringVar()
        self.dtext = tk.StringVar()
        
        self.atext.set('nobadword')
        self.btext.set('nobadword')
        self.ctext.set('nobadword')
        self.dtext.set('nobadword')
        
        super().__init__(master)
        self.master = master
        self.grid()        
        
        self.configure_window()
        self.create_widgets() 
        
    #set up the grid with desired dimensions that is populated by create_widgets
    def configure_window(self):
        
        #set the parent frame to expand when maximized
        top=self.winfo_toplevel()
        top.rowconfigure(self.minrowval, weight=1)
        top.columnconfigure(self.mincolval, weight=1)        
        self.grid(sticky='nsew')        
        
        #configure the selection rows to be roughly 1/4 the screen with the main dialogue the other 3/4
        self.rowconfigure(self.minrowval, weight=16)
        for i in range(1, self.maxrowval + 1):
            self.rowconfigure(i, weight=1)
        
        #set the second column to expand while the first stays put
        self.columnconfigure(self.maxcolval, weight=1)

    def create_widgets(self):
        self.create_user_selButo()
        self.create_user_selText()
        self.create_mainPrompt()
        
    def create_mainPrompt(self):
        self.mPrompt = tk.Listbox(self, bg='black', fg='white', highlightcolor='red', highlightbackground='red',
        activestyle='none', highlightthickness=10, selectbackground='black')
        self.mPrompt.grid(row=0, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        sb = tk.Scrollbar(self.mPrompt)
        self.mPrompt.configure(yscrollcommand=sb)
        
    def create_user_selButo(self):
        self.butoA = tk.Button(self, text="A", bg='black', fg="red",
                              command=self.acmd)
        self.butoA.grid(row=(self.maxrowval-3), column=self.mincolval, sticky='ewns')
        self.butoB = tk.Button(self, text="B", bg='black', fg="red",
                              command=self.bcmd)
        self.butoB.grid(row=(self.maxrowval-2), column=self.mincolval, sticky='ewns')
        self.butoC = tk.Button(self, text="C", bg='black', fg="red",
                              command=self.ccmd)
        self.butoC.grid(row=(self.maxrowval-1), column=self.mincolval, sticky='ewns')
        self.butoD = tk.Button(self, text="D", bg='black', fg="red",
                              command=self.dcmd)
        self.butoD.grid(row=self.maxrowval, column=self.mincolval, sticky='ewns')
        
    def create_user_selText(self):
        self.textA = tk.Label(self, textvariable=self.atext, bg='black', fg='white', anchor='nw')
        self.textA.grid(row=(self.maxrowval-3), column=self.maxcolval, sticky='ewns')
        self.textB = tk.Label(self, textvariable=self.btext, bg='black', fg='white', anchor='nw')
        self.textB.grid(row=(self.maxrowval-2), column=self.maxcolval, sticky='ewns')
        self.textC = tk.Label(self, textvariable=self.ctext, bg='black', fg='white', anchor='nw')
        self.textC.grid(row=(self.maxrowval-1), column=self.maxcolval, sticky='ewns')
        self.textD = tk.Label(self, textvariable=self.dtext, bg='black', fg='white', anchor='nw')
        self.textD.grid(row=(self.maxrowval), column=self.maxcolval, sticky='ewns')

    def acmd(self):
        self.mPrompt.insert(self.minput, 'nafam' + '\n')
        self.minput += 1
        if 'FUCK' in self.atext.get():
            self.atext.set("nobadword")
        else:
            self.atext.set("FUCK A")
        
    def bcmd(self):
        if 'FUCK' in self.btext.get():
            self.btext.set("nobadword")
        else:
            self.btext.set("FUCK B")
        
    def ccmd(self):
        if 'FUCK' in self.ctext.get():
            self.ctext.set("nobadword")
        else:
            self.ctext.set("FUCK C")
        
    def dcmd(self):
        if 'FUCK' in self.dtext.get():
            self.dtext.set("nobadword")
        else:
            self.dtext.set("FUCK D")

class Choices_Var(tk.Scrollbar):
    pass


def runprog():
    root = tk.Tk()
    app = Text_Dungeon(master=root)
    app.mainloop()

if __name__ == "__main__":
    runprog()