import tkinter as tk

class Text_Dungeon(tk.Frame):
    def __init__(self, master=None):    
        self.maxrowval = 4
        self.minrowval = 0
        self.maxcolval = 1
        self.mincolval = 0
        
        self.textvars = []
        self.minput = 0                
        
        for i in range(0, 4):
            self.textvars.append(tk.StringVar())
            self.textvars[i].set('nobadword')                
        
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
        self.create_mainPrompt()
        self.create_user_selButo()
        self.create_user_selText()                
        
    def create_mainPrompt(self):
        self.mPrompt = tk.Listbox(self, bg='black', fg='white', highlightcolor='red', highlightbackground='red',
        activestyle='none', highlightthickness=10, selectbackground='black')
        self.mPrompt.grid(row=0, column=0, columnspan=2, sticky=tk.N+tk.S+tk.E+tk.W)
        sb = tk.Scrollbar(self.mPrompt)
        self.mPrompt.configure(yscrollcommand=sb)
        
    def create_user_selButo(self):
        
        self.buttons = []
        self.cmdHandlers = []
        
        for i in range(0,4):
            self.cmdHandlers.append(ButtonCmd(i, self.textvars[i], self.mPrompt))
            self.buttons.append(tk.Button(self, text=str(i+1), bg='black', fg="red", command=self.cmdHandlers[i].button_cmd))
            self.buttons[i].grid(row=i+1, column=self.mincolval, sticky='ewns')
            
        
    def create_user_selText(self):
        
        self.text_labels = []
        
        for i in range(0,4):
            self.text_labels.append(tk.Label(self, textvariable=self.textvars[i], bg='black', fg='white', anchor='nw'))
            self.text_labels[i].grid(row=i+1, column=self.maxcolval, sticky='ewns')
              

class Choices_Var(tk.Scrollbar):
    pass
    
class ButtonCmd():
    
    def __init__(self, ID, Text_Var, Main_Prompt):
        self.ID = ID
        self.Text_Var = Text_Var
        self.Main_Prompt = Main_Prompt
    
    def button_cmd(self):
    
        innum = self.Main_Prompt.size()
        self.Main_Prompt.insert(innum + 1, 'nafam' + '\n')        
        if 'FUCK' in self.Text_Var.get():
            self.Text_Var.set("nobadword")
        else:
            self.Text_Var.set("FUCK " + str(self.ID))
 


def runprog():
    root = tk.Tk()
    app = Text_Dungeon(master=root)
    app.mainloop()

if __name__ == "__main__":
    runprog()