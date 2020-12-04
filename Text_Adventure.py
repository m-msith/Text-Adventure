import tkinter as tk

class Text_Dungeon():

    def __init__(self, master=None):  
    
        self.master = master                               
        
        self.configure_window()
        self.create_widgets() 
        
    #set up the grid with desired dimensions that is populated by create_widgets
    def configure_window(self):
        
        #set the parent frame to expand when maximized
        self.master.grid_rowconfigure(0, weight=3)
        self.master.grid_rowconfigure(1, weight=1)        
        self.master.grid_columnconfigure(0, weight=1)        
        
        
    #make the meat and potatoes
    def create_widgets(self):        
        self.create_mainPrompt()
        self.create_userSelection()             
        
    #Top frame, holds text that is modified based on button choice
    def create_mainPrompt(self):
    
        #holding frame, top 3/4 of screen
        self.panel_one = tk.Frame(self.master, background='black')                 
        self.panel_one.grid(row=0,column=0,sticky='nsew')
        
        #set interior panel dimensions
        self.panel_one.grid_rowconfigure(0, weight=1)
        self.panel_one.grid_columnconfigure(0, weight=1)
           
        #the listbox that is contained by the panel one frame
        self.panel_one.mPrompt = tk.Listbox(self.panel_one, bg='black', 
        fg='white', highlightcolor='red', highlightbackground='red',
        activestyle='none', highlightthickness=10, selectbackground='black')
        
        #set to the only interior spot
        self.panel_one.mPrompt.grid(row=0, column=0, sticky='nsew')
        
        sb = tk.Scrollbar(self.panel_one.mPrompt)
        self.panel_one.mPrompt.configure(yscrollcommand=sb)
        
        
    def create_userSelection(self):
        
        #create text vars
        self.textvars = []
        for i in range(0, 4):
            self.textvars.append(tk.StringVar())
            self.textvars[i].set('nobadwordnobadwordnobadword') 
            
        
        #holding frame, bottom 1/4 of screen
        self.panel_two = tk.Frame(self.master, background='black')        
        self.panel_two.grid(row=1,column=0, sticky='nsew')
        
        #set interior panel column dimensions        
        self.panel_two.grid_columnconfigure(1, weight=1)
        
        cmdHandlers = []
        self.panel_two.buttons = []        
        self.panel_two.text_labels = []               
        
        for i in range(0,4):
          
            cmdHandlers.append(ButtonCmd(i, self.textvars[i], self.panel_one.mPrompt))
            
            self.panel_two.buttons.append(tk.Button(self.panel_two, text=str(i+1), 
            bg='black', fg="red", command=cmdHandlers[i].button_cmd))
            
            self.panel_two.text_labels.append(tk.Label(self.panel_two, 
            textvariable=self.textvars[i], bg='black', fg='white', anchor='nw'))
            
            self.panel_two.grid_rowconfigure(i, weight=1)
            self.panel_two.buttons[i].grid(row=i, column=0, sticky='nsew')                        
            self.panel_two.text_labels[i].grid(row=i, column=1, sticky='nsew')                                    
            
    
    def displayLoop(self):
        self.master.mainloop()
        

def runprog():
    root = tk.Tk()
    root.geometry('500x500')
    app = Text_Dungeon(master=root)    
    app.displayLoop()
    
 
#wrap a command in order to have it effect a variable source
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
            
    
if __name__ == "__main__":
    runprog()