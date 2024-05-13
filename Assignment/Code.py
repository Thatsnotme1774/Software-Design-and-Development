
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter

root = customtkinter.CTk()
root.title("okkk")
#root.overrideredirect(True)
#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.geometry("1280x720")
root.minsize(width=640, height=480)
root.maxsize(width=3840, height = 2160)

start_display = False
option_display = False
quiz_display = False
learning_disalyze = False


#functions
def resize_image(number):
    global new_height, new_width, relativex, relativey, relative_scale
    new_width = number.width #sets new width depending on the  number given
    new_height = number.height
    relativex = new_width/1920 #since my laptop is 1920x1080
    relativey = new_height/1080 
    relative_scale = (relativex+relativey)/2 #the average relative scale

    if start_display == True:
        try:
            image = copy_of_image.resize((new_width, new_height)) #scales the background image
            photo = ImageTk.PhotoImage(image)
            label.config(image = photo)
            label.image = photo
            
            start_button.configure(font=("Arial",50*relative_scale), width=120, height=40 )
            geometric_prop.configure(font=("Segoe Script",50*relative_scale), width=202, height=169)
        except:
            pass


def list_file():
    global text_list
    file = open("Assignment\languages\english.txt")

    text_list = []

    for i in file.readlines():
        text = i.replace("\n", "")
        text_list.append(text)
    

def option():
    pass
def learning():
    pass
def quiz():
    pass
def start():
    global copy_of_image, image, photo, label, start_button, option_display,start_display,quiz_display,learning_display,geometric_prop
    option_display = False
    start_display = True
    quiz_display = False
    learning_display = False
    
    image = Image.open('Assignment\images\jackground1.png')
    copy_of_image = image.copy()
    photo = ImageTk.PhotoImage(image)
    label = ttk.Label(root, image = photo)
    label.bind('<Configure>', resize_image)
    label.pack(fill=BOTH, expand = YES)

    geometric_prop = customtkinter.CTkLabel(root, text=text_list[0], font=("Segoe Script", 50), bg_color="white", fg_color="white", text_color="black", wraplength=300)
    geometric_prop.place(relx=0.47, rely=0.38) 
                            
    start_button = customtkinter.CTkButton(master=root, text = text_list[1], font=("Ariel", 50) )
    start_button.place(relx=0.01, rely = 0.25) 
    
                            





list_file()

start()




#Label











root.mainloop()