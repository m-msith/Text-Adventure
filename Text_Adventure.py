import tkinter as tk

class Text_Dungeon():

    def __init__(self, conductor=None):  
    
        self.conductor = conductor                               
        
        self.configure_window()
        self.create_widgets() 
        
    #set up the grid with desired dimensions that is populated by create_widgets
    def configure_window(self):
        
        #set the parent frame to expand when maximized
        self.conductor.grid_columnconfigure(0, weight=1)
        self.conductor.grid_rowconfigure(0, weight=3)
        self.conductor.grid_rowconfigure(1, weight=1)                        
        
        
    #make the meat and potatoes
    def create_widgets(self):        
        self.create_mainPrompt()
        self.create_userSelection()             
        
        
    #Top frame, holds text that is modified based on button choice
    def create_mainPrompt(self):
    
        #holding frame, top 3/4 of screen
        self.panel_one = tk.Frame(self.conductor, background='black')                 
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
        
        #add in a scrollbar 
        sb = tk.Scrollbar(self.panel_one.mPrompt)
        self.panel_one.mPrompt.configure(yscrollcommand=sb.set)
        
        
    def create_userSelection(self):
        
        #create text vars
        self.textvars = []
        for i in range(0, 20):
            self.textvars.append(tk.StringVar())
            self.textvars[i].set('nobadwordnobadwordnobadwordnobadwordnobad \
            nobadwordnobadwordnobadwordnobadwordnobadwordnobadwordnobadword \
            nobadwordnobadwordnobadwordnobadwordnobadwordnobadwordnobadword') 
            
        
        
        #holding canvas, bottom 1/4 of screen
        self.panel_two = tk.Canvas(self.conductor, background='green', highlightthickness=0)        
        self.panel_two.grid(row=1, column=0, sticky='nsew')                
        
        #frame inside the canvas to hold our button/label grid
        self.p2_frame = tk.Frame(self.panel_two, background='black')        
        
        #in the frame, want the label to expand, not button
        self.p2_frame.grid_columnconfigure(1, weight=1)     
        
        #variable size widget and command handlers
        cmdHandlers = []
        self.p2_frame.buttons = []        
        self.p2_frame.text_labels = []               
        
        for i in range(0,20):
          
            cmdHandlers.append(ButtonCmd(i, self.textvars[i], self.panel_one.mPrompt))
            
            self.p2_frame.buttons.append(tk.Button(self.p2_frame, text=str(i+1), 
            bg='black', fg="red", command=cmdHandlers[i].button_cmd))
            
            self.p2_frame.text_labels.append(WrappingLabel(self.p2_frame, 
            textvariable=self.textvars[i], bg='black', fg='white', anchor='nw'))
            
            #even row weights in the frame
            self.p2_frame.grid_rowconfigure(i, weight=1)
            self.p2_frame.buttons[i].grid(row=i, column=0, sticky='nsew')                        
            self.p2_frame.text_labels[i].grid(row=i, column=1, sticky='nsew')          
        
        #add the frame with all of it's children to the canvas
        self.win = self.panel_two.create_window(0, 0, window=self.p2_frame, anchor='nw')         
        
        #add a scroll bar so we don't bork our dimensions with different choice numbers
        self.sb2 = tk.Scrollbar(self.p2_frame, command=self.panel_two.yview)        
        #self.sb2.grid(row=0,column=2,rowspan=20, sticky="ns")
        self.panel_two.configure(yscrollcommand=self.sb2.set)                       
        
        self.panel_two.bind("<Enter>", self.BindUserScroll)
        self.panel_two.bind("<Leave>", self.UnbindUserScroll)
        self.panel_two.bind("<Configure>", self.FrameWidth)        
        self.p2_frame.bind("<Configure>", self.OnFrameConfigure)
        
        
    def OnMouseWheel(self, event):
        self.panel_two.yview_scroll(-1*(event.delta//120), "units")
        
    def BindUserScroll(self, event):
        self.conductor.bind_all("<MouseWheel>", self.OnMouseWheel)
        
    def UnbindUserScroll(self, event):
        self.conductor.unbind_all("<MouseWheel>")
        
    def FrameWidth(self, event):
        self.panel_two.itemconfig(self.win, width = event.width)
        
    def OnFrameConfigure(self, event):
        self.panel_two.configure(scrollregion=self.p2_frame.bbox("all"))#(0,0,0,self.p2_frame.winfo_height())
        
    def displayLoop(self):
        self.conductor.mainloop()
        

def runprog():
    root = tk.Tk()
    root.geometry('500x500')
    app = Text_Dungeon(conductor=root)    
    app.displayLoop()
    
class WrappingLabel(tk.Label):
    def __init__(self, conductor=None, **kwargs):
        tk.Label.__init__(self, conductor, **kwargs)
        self.bind('<Configure>', lambda e: self.config(wraplength=self.winfo_width()))
    
 
#wrap a command in order to have it effect a variable source
class ButtonCmd():
    
    def __init__(self, ID, Text_Var, Main_Prompt):
        self.ID = ID
        self.Text_Var = Text_Var
        self.Main_Prompt = Main_Prompt
    
    def button_cmd(self):
        
        innum = self.Main_Prompt.size()
        self.Main_Prompt.insert(innum + 1, 'nafam'+ str(innum) + '\n')   
        
        if 'duck' in self.Text_Var.get():
            self.Text_Var.set("nobadwordnobadwordnobadwordnobadwordnobadwordnobadwordnobadword \
            nobadwordnobadwordnobadwordnobadwordnobadwordnobadwordnobadword \
            nobadwordnobadwordnobadwordnobadwordnobadwordnobadwordnobadword")
        else:
            self.Text_Var.set("duck " + str(self.ID))
            
    
if __name__ == "__main__":
    runprog()