import tkinter as tk
from tkinter import*
import googletrans
from textblob import*
from tkinter import ttk, messagebox
import pyttsx3
from setuptools import setup


APP = ['main.py']
OPTIONS = {
    'argv_emulation': True,
}
setup(app=APP, options={'py2app':OPTIONS}, setup_requires=["py2app"])






# Setting up tkinter to be used as a GUI. Root is the name of the parent where everything will go to.
root = tk.Tk()

#language list and grabbing langauges

global language_list
languages= googletrans.LANGUAGES
language_list = list(languages.values())


#Variables
scale = 1
    #Canvas and Background Varaibles 
geo = "500x300" 
canvaswidth = 500
canvasheight = 300
canvascolor ="#F0F8FF" #light colour used for canvaas

    #Label
global startnum, prognum, termnum, APnum, GPnum, transmsg, errormsg #making them accessible globally (will be useful for translation)
startnum = "Starting Number"
prognum = "Increment"
termnum = "Number of Terms"
APnum = "Arithmetic Progression"
GPnum = "Geometric Progression"
transmsg = "Translate"
Errormsg =  "ERROR! TYPE INTEGERS IN ALL BOXES"
backup = "ERROR! TYPE INTEGERS IN ALL BOXES"


    #Label settings
labelback = "White" #color for Label background
labeltextcol = "Black" #text color used for labels
labelfont = "Arial" #font for label
labelsize = 200


    #Starting number settings for AP and GP
startnumsize = 10
startnumx = 20
startnumy = 20
startnumtx = 180
startnumty = 20

    #Number of terms settings for AP and GP
numOftermsize = 10
numOFtermx = 20
numOFtermy = 70
numofsumtx = 180
numofsumty = 70

    #Progression number settings for AP and GP
progressionnumsize = 10
progressionnumx = 20
progressionnumy = 120
progressionnumtx=180
progressionnumty =120

    #Language combo box
boxwid = 45
boxx=10 
boxy=160


    #translator button settings
transy =156
transx =265
transsize = 10

    #AP radio button settings
APy = 180
APx= 10
APsize = 10

    #GP radio button settings
GPy = 180
GPx = 220
GPsize = 10

#resolution slider
resx =210
resy = 210
reslen =150
reswid = 20


#speak
speaksize = 10
speakx = 210
speaky = 210



    #output
outx = 10
outy = 210
outwid = 190
outhei = 80

    #tts
global ttsbut
ttsbut = "Text to speech"

    #menu stuff
global optionbut
optionbut = "Options"
themebut ="Theme"
resbut = "Resolution Bar"
exitbut = "Exit"
lightbut = "Light mode"
darkbut = "Dark mode"

#Fucntions


def toggle_light_mode():
    global light_mode_var, dark_mode_var
    if light_mode_var.get() == False:
        dark_mode_var.set(True)
        dark_mode()
    else:
        dark_mode_var.set(False)
        light_mode()

def toggle_dark_mode():
    global light_mode_var, dark_mode_var
    if dark_mode_var.get() == False:
        light_mode_var.set(True)
        light_mode()
    else:
        light_mode_var.set(False)
        dark_mode()

def light_mode():
    global canvascolor, labelback, labeltextcol
    canvascolor = "#F0F8FF"
    labelback = "White"
    labeltextcol = "black"
    select_color = "white"  # Set the color of the dot for selected radio buttons
    # Update the colors for existing widgets
    frame.config(bg=canvascolor)
    Startingnum.config(bg=labelback, fg=labeltextcol)
    Numofterms.config(bg=labelback, fg=labeltextcol)
    Progressionnum.config(bg=labelback, fg=labeltextcol)
    AP.config(bg=canvascolor, fg = labeltextcol, activebackground=canvascolor, activeforeground=labeltextcol, selectcolor=select_color)
    GP.config(bg=canvascolor, fg =labeltextcol, activebackground=canvascolor, activeforeground=labeltextcol, selectcolor=select_color)
    trans.config(bg=canvascolor, fg="Black", activebackground=canvascolor, activeforeground=labeltextcol)
    ans.config(bg=labelback, fg=labeltextcol)
    speak.config(bg=labelback, fg=labeltextcol, activebackground=canvascolor, activeforeground=labeltextcol)

def dark_mode():
    global canvascolor, labelback, labeltextcol
    canvascolor = "#333333"
    labelback = "Black"
    labeltextcol = "White"
    select_color = "black"  # Set the color of the dot for selected radio buttons
    # Update the colors for existing widgets
    frame.config(bg=canvascolor)
    Startingnum.config(bg=labelback, fg=labeltextcol)
    Numofterms.config(bg=labelback, fg=labeltextcol)
    Progressionnum.config(bg=labelback, fg=labeltextcol)
    AP.config(bg=canvascolor, fg=labeltextcol, activebackground=canvascolor, activeforeground= labeltextcol, selectcolor=select_color)
    GP.config(bg=canvascolor, fg =labeltextcol, activebackground=canvascolor, activeforeground=labeltextcol, selectcolor=select_color)
    trans.config(bg=canvascolor, fg= "white", activebackground=canvascolor, activeforeground= labeltextcol)
    ans.config(bg=labelback, fg=labeltextcol)
    speak.config(bg=canvascolor, fg=labeltextcol, activebackground=canvascolor, activeforeground= labeltextcol)
resolution_window = None
resolution_window_open = False
def openresolutionwindow(): #function that opens resolution window
    global resolution_slider, resolution_window, resvar
    if resvar.get():
        resolution_window = tk.Toplevel(root)  # Create a new Toplevel window
        resolution_window.title("Resolution Settings")
        resolution_window.geometry("300x100")  # Set the size of the window

        resolution_slider = tk.Scale(resolution_window, from_=0, to=5, orient=tk.HORIZONTAL, length=250, label="Resolution", width=20)
        resolution_slider.pack(pady=20)
        resolution_slider.bind("<Motion>", resolution_slider_change)
        resolution_window.protocol("WM_DELETE_WINDOW", close_resolution_window)
    else:
        close_resolution_window()

def close_resolution_window():
    global resolution_window, resvar
    resvar.set(False)
    if resolution_window:
        resolution_window.destroy()
def toggle_resolution_bar():
    if resolution_window_open:
        resolution_window.destroy()
    else:
        openresolutionwindow()

    if resolution_window_open:
        file_menu.entryconfig("Resolution Bar", label="Resolution Bar (Open)")
    else:
        file_menu.entryconfig("Resolution Bar", label="Resolution Bar")



def updateres(slider_value): #everytime the slider value changes, this command runs to change size of everything
    global canvaswidth, canvasheight, geo, startnumx, startnumy, startnumtx, startnumty, numOFtermx, numOFtermy, numofsumtx, numofsumty, progressionnumx, progressionnumy, progressionnumtx, progressionnumty, APx, APy, GPx, GPy, boxx, boxy, transx, transy, outx, outy, outwid, outhei

    canvaswidth = int(500 + (slider_value * 100)) #value of the slider is used for multiplication 
    
    # Limit the maximum height based on the screen's height so it doesnt multiply by the same factor as the width
    maxhei = root.winfo_screenheight() - 100  # Adjust the subtraction value as needed
    canvasheight = min(int(300 + (slider_value * 50)), maxhei) #adjusted value of height 
    
    geo = f"{canvaswidth}x{canvasheight}" #setting geometry to the new valus
    root.geometry(geo)
    root.maxsize(width=canvaswidth, height=canvasheight) #Setting new values
    root.minsize(width=canvaswidth, height=canvasheight) 
    
    #changing values according to slider
    startnumsize=int(10 + (slider_value*10))
    labelsize=int(200 + (slider_value*100))
    startnumtx=int(180+ (slider_value*70))
    numofsumty= min(int(70 + (slider_value * 10)), maxhei)
    progressionnumty = min(int(120 + (slider_value * 20)), maxhei)
    boxwid = int(45+ (slider_value*10))
    transnum=int(9 + (slider_value*1))
    boxy = min(int(160 + (slider_value * 35)), maxhei)
    transsize = int(10 + (slider_value*3))
    transx = int(265+ (slider_value*110))
    transy = min(int(156 + (slider_value * 32)), maxhei)
    APsize = int(10 + (slider_value*4))
    GPsize = int(10 + (slider_value*4))
    GPx = int(220+ (slider_value*50))
    APy =min(int(180 + (slider_value * 37)), maxhei) 
    GPy =min(int(180 + (slider_value * 37)), maxhei)
    outy= min(int(210 + (slider_value * 42)), maxhei)
    outwid = int(190+ (slider_value*100))
    speaksize =int(10 + (slider_value*4))
    speakx = int(210 + (slider_value*100))
    speaky =min(int(210 + (slider_value * 42)), maxhei)

    Startingnum.config(font=(startnum, startnumsize))
    StartingnumTxt.config(font=(startnum, startnumsize))
    StartingnumTxt.place(x=startnumtx, width=labelsize)

    Numofterms.config(font=(startnum, startnumsize))
    Numofterms.place(y=numofsumty)
    NumoftermsTxt.config(font=(startnum, startnumsize))
    NumoftermsTxt.place(x=startnumtx, y= numofsumty, width=labelsize)

    Progressionnum.config(font=(startnum, startnumsize))
    Progressionnum.place(y=progressionnumty)
    Progressionnumtxt.config(font=(startnum, startnumsize))
    Progressionnumtxt.place(x=startnumtx,y=progressionnumty, width=labelsize)


    
    translated.config(width=boxwid, font=(startnum, transnum)) #meant to be called box num but same thing
    translated.place(y=boxy)

    trans.config(font=(startnum, transsize))
    trans.place(y=transy, x=transx)
    
    AP.config(font=(labelfont, APsize))
    AP.place(y=APy,x=APx)
    GP.config(font=(labelfont, GPsize))
    GP.place(y=GPy,x=GPx)
    output.place(y=outy, width=outwid)
    
    speak.config(font=(labelfont, speaksize))
    speak.place(y=speaky, x=speakx)
    



def resolution_slider_change(event): #changes the animation so it looks like the slider moved
    slider_value = resolution_slider.get()
    updateres(slider_value)






def translate():
    global startnum, termnum, prognum, APnum, GPnum, transmsg, Errormsg, from_languge_key, to_languge_key, ttsbut, optionbut
    try:
        if original.get() == translated.get(): #just a quick fix that retranslates it back to english
            Startingnum.config(text=startnum)
            Progressionnum.config(text=prognum)
            Numofterms.config(text=termnum)
            AP.config(text=APnum)
            GP.config(text=GPnum)
            trans.config(text=transmsg)
            speak.config(text=ttsbut)
            
            if ans.get("1.0", "end-1c") == Errormsg:
                ans.config(state=NORMAL)
                ans.delete("1.0", tk.END)  # Clear the answer
                ans.insert(tk.END, backup)
                ans.config(state=DISABLED)
            else:
                Errormsg=backup
        else:                                 #for every other language, this works
        #getting languges 
       #From languge 
            for key, value in languages.items():
                if (value == original.get()):
                    from_languge_key =key
        #TO langauge 
            for key, value in languages.items():
                if (value == translated.get()):
                    to_languge_key =key  
        
            #translating starting number
            words1 = TextBlob(startnum) #turn og text into textblob
            words1 = words1.translate(from_lang=from_languge_key , to=to_languge_key)
            
            Startingnum.config(text=words1)

            #translating progression number
            words2 = TextBlob(prognum) #turn og text into textblob
            words2 = words2.translate(from_lang=from_languge_key , to=to_languge_key)
            
            Progressionnum.config(text=words2)

            #translating number of terms
            words3 = TextBlob(termnum) #turn og text into textblob
            words3 = words3.translate(from_lang=from_languge_key , to=to_languge_key)
            Numofterms.config(text=words3)

            #translating the AP button
            words4 = TextBlob(APnum) #turn og text into textblob
            words4 = words4.translate(from_lang=from_languge_key , to=to_languge_key)
            AP.config(text=words4)

            #translating the GP button
            words5 = TextBlob(GPnum) #turn og text into textblob
            words5 = words5.translate(from_lang=from_languge_key , to=to_languge_key)
            GP.config(text=words5)

            #translating the Translate button
            words6 = TextBlob(transmsg) #turn og text into textblob
            words6 = words6.translate(from_lang=from_languge_key , to=to_languge_key)
            trans.config(text=words6)

            #text to speech
            words8 = TextBlob(ttsbut)
            words8 = words8.translate(from_lang=from_languge_key , to=to_languge_key)
            speak.config(text=words8)

            #menu texts
            

            
            

            if ans.get("1.0", "end-1c") == Errormsg:
                ans.config(state=NORMAL)
                ans.delete("1.0", tk.END)  # Clear the answer
                words7 = TextBlob(backup) #turn og text into textblob
                Errormsg = words7.translate(from_lang=from_languge_key , to=to_languge_key)
                ans.insert(tk.END, Errormsg)
                ans.config(state=DISABLED)
            
            elif ans.get("1.0", "end-1c") == backup: #this fixed a bug
                ans.config(state=NORMAL)
                ans.delete("1.0", tk.END)  # Clear the answer
                words7 = TextBlob(backup) 
                Errormsg = words7.translate(from_lang=from_languge_key , to=to_languge_key)
                ans.insert(tk.END, Errormsg)
                ans.config(state=DISABLED)
            else:
                words7 = TextBlob(backup)
                Errormsg = words7.translate(from_lang=from_languge_key , to=to_languge_key)
            



    except Exception as e:
        messagebox.showerror("Translate Error", e)

        

def clear():
    pass

def Arithmetic():
    ans.config(state=tk.NORMAL)  # Resets the state of text widget
    ans.delete(1.0, tk.END)  # Clear the previous output


    if not (StartingnumTxt.get().isdecimal() and Progressionnumtxt.get().isdecimal() and NumoftermsTxt.get().isdecimal()): #Checks whether the values are integers or not
            ans.config(state=NORMAL)
            ans.insert(tk.END, Errormsg) #IF they aren't then it gives an error
            ans.config(state=DISABLED)
            
    else:                                                          #Else does the calculation
        final = 0
        tempnum = 1
        list = []
        first = int(StartingnumTxt.get())
        prog = int(Progressionnumtxt.get())
        while tempnum <= int(NumoftermsTxt.get()):
            final = first + (tempnum - 1)*prog
            tempnum += 1
            list.append(str(final))
        ans.insert(tk.END, " ".join(list)) #Adds the number to the end
        ans.config(state=tk.DISABLED)  # Make the Text widget read-only


def Geometric():
    ans.config(state=tk.NORMAL)  # Resets the state of text widget
    ans.delete(1.0, tk.END)  # Clear the previous output

    if not (StartingnumTxt.get().isdecimal() and Progressionnumtxt.get().isdecimal() and NumoftermsTxt.get().isdecimal()): #Checks whether the values are integers or not
            ans.config(state=NORMAL)
            ans.insert(tk.END, Errormsg) #IF they aren't then it gives an error
            ans.config(state=DISABLED)
        
    else:                                                          #Else does the calculation




        final = 0
        tempnum = 1
        list = []
        first = int(StartingnumTxt.get())
        prog = int(Progressionnumtxt.get())
        while tempnum <= int(NumoftermsTxt.get()):
            final = first *(prog**(tempnum-1))
            tempnum += 1
            list.append(str(final))
        ans.insert(tk.END, " ".join(list)) #adds the number to the end
        ans.config(state=tk.DISABLED)  # Make the Text widget read-only



def destroy():
    root.destroy()
def tts():
    engine=pyttsx3.init()
    engine.say("In the first box, type the starting number. In the second box, type the number of terms. In the third box, type the incremental number. Make sure they are all integers")
    engine.runAndWait()

def calculator():
    
    root.title("AP and GP calculator")
    root.geometry(geo)
    root.maxsize(width=canvaswidth, height=canvasheight)
    root.minsize(width=canvaswidth, height=canvasheight)
    root.tk.call('tk', 'scaling', scale)






    global ans, frame
    #Setting up the frame
    frame = tk.Frame(root, bg=canvascolor) #was going to use canvas but frame seemed better
    frame.pack(fill=tk.BOTH, expand=True) #fills horizontal and vertical and also expands it

    #Menu
    global menubar
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    global file_menu 

        #Adding a file button
    file_menu = tk.Menu(menubar, tearoff=0) #makng a parent 
    menubar.add_cascade(label=optionbut, menu=file_menu) #naming the parent file
    
        #making the themes menu a parant 
    theme_menu =tk.Menu(file_menu, tearoff=0) 
        #adding the themes menu
    file_menu.add_cascade(label=themebut, menu=theme_menu)
    global resvar
    resvar = tk.BooleanVar(value=False) #just to keep in track of the tick
    file_menu.add_checkbutton(label=resbut, command=openresolutionwindow, variable=resvar)
    





        #exit button
    file_menu.add_cascade(label=exitbut, command=destroy)

    global light_mode_var, dark_mode_var
    light_mode_var = tk.BooleanVar(value=True)  # Initially, light mode is on
    dark_mode_var = tk.BooleanVar(value=not light_mode_var.get()) #does the opposite of light_mode_var, so if light mode var is off this will be on

    
    theme_menu.add_checkbutton(label=lightbut, command=toggle_light_mode ,onvalue = True,offvalue = False, variable=light_mode_var)
    theme_menu.add_checkbutton(label=darkbut, variable=dark_mode_var, command=toggle_dark_mode)



    
    #Labels
        #Starting number

    global Startingnum
    Startingnum = tk.Label(frame, text=(startnum), font=(labelfont, startnumsize), bg=labelback, fg=labeltextcol)
    Startingnum.place(x=startnumx, y=startnumy)

        #Number of Terms
    global Numofterms
    Numofterms = tk.Label(frame, text=(termnum), font=(labelfont, numOftermsize), bg=labelback, fg=labeltextcol)
    Numofterms.place(x=numOFtermx, y=numOFtermy)
    
        #Progression Number
    global Progressionnum
    Progressionnum =tk.Label(frame, text=(prognum), font=(labelfont, progressionnumsize), bg=labelback, fg=labeltextcol)
    Progressionnum.place(x=progressionnumx, y=progressionnumy)

    #Entries 

    global StartingnumTxt
    StartingnumTxt = tk.Entry(frame, font=(labelfont, startnumsize), bg=labelback, fg=labeltextcol)
    StartingnumTxt.place(x=startnumtx, y=startnumty, width=labelsize)

    global NumoftermsTxt
    NumoftermsTxt = tk.Entry(frame, font=(labelfont, numOftermsize), bg=labelback, fg=labeltextcol)
    NumoftermsTxt.place(x=numofsumtx, y=numofsumty, width=labelsize)

    global Progressionnumtxt
    Progressionnumtxt = tk.Entry(frame, font=(labelfont, progressionnumsize), bg=labelback, fg=labeltextcol)
    Progressionnumtxt.place(x=progressionnumtx, y=progressionnumty, width=labelsize)


    #Radiobuttons


    global AP, GP, trans, APvar, GPvar

    ranvar = tk.IntVar(value=0)  # Variables to store the selected value for AP radio button
    ranvar = tk.IntVar(value=0) # value = 0 makes it unselected when code is launched
    AP = tk.Radiobutton(frame, text="Arithmetic Progression", command=Arithmetic, value=1, font=(labelfont, APsize), bg=canvascolor, fg="black", variable=ranvar)
    AP.place(x=APx, y=APy)
    GP = tk.Radiobutton(frame, text="Geometric Progression", command=Geometric, value=2, font=(labelfont, GPsize), bg=canvascolor, fg="black", variable=ranvar)
    GP.place(x=GPx, y=GPy)

    #buttons
    global speak
    trans = tk.Button(frame, text="Translate", command=translate, font=(labelfont, transsize), bg=canvascolor, fg="black")
    trans.place(x=transx,y=transy)
    speak = tk.Button(frame, text="Text to Speech", command=tts, font=(labelfont, speaksize),  bg=canvascolor, fg="black")
    speak.place(x=speakx,y=speaky)
    #Textbox
    original_text = Text(frame)
    translated_text = Text(frame)


    #Combo Box
    global original
    
    original = ttk.Combobox(frame, width=boxwid, value=language_list)
    original.current(21)
    
    global translated
    translated = ttk.Combobox(frame, width=boxwid, value=language_list)
    translated.current(26)
    translated.place(x=boxx,y=boxy)
    translated.config(state='readonly')

    #output 

        #Frame for the output
    global output
    output = tk.Frame(frame, bg=canvascolor)
    output.place(x=outx, y=outy, width=outwid, height=outhei)
   
        #Answer label placed in the output frame
    global ans
    ans = tk.Text(output, font=(labelfont, 15), wrap=tk.NONE, fg="black")#wrap basically choses what to do when the text goes over the box, in this case it is set to none as we will be using a scroll bar.
    ans.pack(side=tk.LEFT, fill=tk.BOTH, expand=True) #side command moves it all the way to the left of the output frame, fill makes sure that both horizontal and vertical axises are occupied and expand makes it useable when expanded

        #Scroll bar used in the answer
    scroll = tk.Scrollbar(output, command=ans.yview)#the scrollbar is set so that it will be vertical
    scroll.pack(side=tk.RIGHT, fill=tk.Y)#goes to the right side of the frame and fills the y axis
 
    ans.config(yscrollcommand=scroll.set, wrap=tk.WORD) #sets up the scrollbar and wraps the text with a word boundary
    

    #global resolution_slider
    #resolution_slider = tk.Scale(frame, from_=0, to=5, orient=tk.HORIZONTAL, length=reslen, label="Resolution", width=reswid)
    #resolution_slider.place(x=resx, y=resy)
    #resolution_slider.bind("<Motion>", resolution_slider_change)  # Bind to the slider's value change event







    root.mainloop()

    







if __name__ == "__main__": #checks if it is the main program
    calculator()