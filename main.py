import os, shutil, ctypes, subprocess, sys, webbrowser
from tkinter import *
from tkinter import messagebox
import tkinter
import tkinter.ttk as ttk
from traceback import format_exc

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    finally:   
        return os.path.join(base_path, relative_path)

FNULL = open(os.devnull, 'r')

def is_admin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin
#константа сосет!!!
error_log = ""
error_num = 0
unexpected_errors = 0

console_log = ""
console_num = 0

files_removed = 0
files_replaced = 0


def Increase_Progressbar():
    progressvalue0.set(progressvalue0.get()+125)
    label2["text"] = str(progressvalue0.get()/10)

def run_getter():
    global files_removed, files_replaced, error_num, error_log, console_log
    try:
        Get_Minecraft()
    except Exception as err_:
        text = format_exc()
        text2.insert(END, text)
        w4.deiconify()
        button0["state"]=DISABLED
        return 0
    text = f"Script Executed\n{files_removed}/2 files removed\n{files_replaced}/2 files replaced\n{error_num} errors occured"
    text0.delete(0.0, END)
    text0.insert(END, error_log)
    text1.delete(0.0, END)
    text1.insert(END, console_log)
    label5["text"] = text
    w5.deiconify()

def get_minecraft():
    global command1, command2, error_log, console_log, error_num, console_num, \
        unexpected_errors, files_removed, files_replaced, FNULL
    os.chdir("assets")

    button0.pack_forget()
    frame0.pack(side=TOP)
    button0.pack(side=TOP, pady=20)
    button0.config(state=DISABLED)

    #outp = os.popen(command1 % path_to_system32).read()
    #outp = subprocess.Popen(command1 % path_to_system32, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    proc = subprocess.run(command1 % path_to_system32, capture_output=True, shell=True, stdin=FNULL)
    outp = proc.stdout.decode("utf-8")
    console_log += f"Command log {console_num}:\n"
    console_log += outp
    console_num += 1
    Increase_Progressbar()

    #outp = os.popen(command2 % path_to_system32).read()
    #outp = subprocess.Popen(command2 % path_to_system32, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    proc = subprocess.run(command2 % path_to_system32, capture_output=True, shell=True, stdin=FNULL)
    outp = proc.stdout.decode("utf-8")
    console_log += f"Command log {console_num}:\n"
    console_log += outp
    console_num += 1
    Increase_Progressbar()

    try:
        os.remove(path_to_system32)
        files_removed += 1
    except FileNotFoundError as e:
        full_exc = format_exc()
        error_log += f"Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
    except Exception as err_:
        error_name = err_.__class__.__name__
        full_exc = format_exc()
        error_log += f"[UNEXPECTED ERROR] {error_name} Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
        unexpected_errors += 1
    Increase_Progressbar()

    try:
        shutil.copy(resource_path("assets/x64/System32/Windows.ApplicationModel.Store.dll"), path_to_system32)
        files_replaced += 1
    except FileNotFoundError as e:
        full_exc = format_exc()
        error_log += f"Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
    except Exception as err_:
        error_name = err_.__class__.__name__
        full_exc = format_exc()
        error_log += f"[UNEXPECTED ERROR] {error_name} Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
        unexpected_errors += 1
    Increase_Progressbar()


    
    proc = subprocess.run(command1 % path_to_syswow64, capture_output=True, shell=True, stdin=FNULL)
    outp = proc.stdout.decode("utf-8")
    console_log += f"Command log {console_num}:\n"
    console_log += outp
    console_num += 1
    Increase_Progressbar()

    #outp = os.popen(command2 % path_to_syswow64).read()
    #outp = subprocess.Popen(command2 % path_to_syswow64, shell=True, stdout=subprocess.PIPE, bufsize=-1)
    proc = subprocess.run(command2 % path_to_syswow64, capture_output=True, shell=True, stdin=FNULL)
    outp = proc.stdout.decode("utf-8")
    console_log += f"Command log {console_num}:\n"
    console_log += outp
    console_num += 1
    Increase_Progressbar()

    try:
        os.remove(path_to_syswow64)
        files_removed += 1
    except FileNotFoundError as e:
        full_exc = format_exc()
        error_log += f"Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
    except Exception as err_:
        error_name = err_.__class__.__name__
        full_exc = format_exc()
        error_log += f"[UNEXPECTED ERROR] {error_name} Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
        unexpected_errors += 1
    Increase_Progressbar()

    try:
        shutil.copy(resource_path("assets/x64/SysWOW64/Windows.ApplicationModel.Store.dll"), path_to_syswow64)
        files_replaced += 1
    except FileNotFoundError as e:
        full_exc = format_exc()
        error_log += f"Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
    except Exception as err_:
        error_name = err_.__class__.__name__
        full_exc = format_exc()
        error_log += f"[UNEXPECTED ERROR] {error_name} Error {error_num}:\n"
        error_log += full_exc + "\n"
        error_num += 1
        unexpected_errors += 1
    Increase_Progressbar()

command1 = "takeown /f %s"
command2 = "icacls %s /grant *S-1-3-4:F /t /c /l /q"
path_to_system32 = "C:/Windows/System32/Windows.ApplicationModel.Store.dll"
path_to_syswow64 = "C:/Windows/SysWOW64/Windows.ApplicationModel.Store.dll"

#icon = "assets/icon.ico"
icon = resource_path("assets/icon.ico")

w = Tk()
w.title("Minecraft-Inator (Minecraft Windows 10 Ownership)")
w.geometry("500x350")
w.iconbitmap(icon)

label0 = Label(text="  ● Runned as Admin.", fg="green")
label0.pack(anchor=NW)

frame2 = Frame()

label1 = Label(frame2, text="Minecraft Windows 10 Edition\nOwnership taker", justify=CENTER)
label1.pack(anchor=CENTER)

#label2 = Label(frame2, text="https://github.com/Andrevinder", justify=CENTER, fg="#0e04c7")
#label2.pack(anchor=CENTER, pady=3)
#label2.bind("<Enter>", hoverlink)
#label2.bind("<Leave>", unhoverlink)



button4 = Button(frame2, text="https://github.com/Andrevinder", fg="#0e04c7", borderwidth=0, font=("TkDefaultFont", "10", "underline"), \
                    activeforeground="#c7041e", command=lambda: webbrowser.open("https://github.com/Andrevinder", new=2))
button4.pack(anchor=CENTER, pady=3)

frame2.pack(pady=30)

frame0 = Frame()
#frame0.pack(side=TOP)

progressvalue0 = IntVar()
progressbar0 = ttk.Progressbar(frame0, maximum=1000, variable=progressvalue0, length=400)
progressbar0.pack(side=LEFT)
label2 = Label(frame0, text = "0%")
label2.pack(side=LEFT)

button0 = ttk.Button(text="Get Minecraft", command=Run_Getter)
#button0.pack(side=TOP, pady=20)
button0.pack(side=TOP)


w2 = Toplevel()
w2.iconbitmap(icon)
w2.protocol("WM_DELETE_WINDOW", lambda: w2.withdraw())
w2.title("Error Log")
w2.geometry("400x400")
w2.withdraw()
#w2.deiconify()
text0 = Text(w2)
text0.place(relwidth=1, relheight=1)
text0.insert(END, error_log)

w3 = Toplevel()
w3.iconbitmap(icon)
w3.protocol("WM_DELETE_WINDOW", lambda: w3.withdraw())
w3.title("Console Log")
w3.geometry("400x400")
w3.withdraw()
text1 = Text(w3)
text1.place(relwidth=1, relheight=1)
text1.insert(END, console_log)

w4 = Toplevel()
w4.iconbitmap(icon)
w4.geometry("200x230")
w4.title("Unexpected Error While Running")
w4.withdraw()
label3 = Label(w4, text = "An unexpected error occured \nwhile running function.")
label3.pack(side=TOP)
label4 = Label(w4, text = "Error details:")
label4.pack(side=TOP, anchor=W)
text2 = Text(w4)
text2.pack(side = TOP, fill = BOTH)

w5 = Toplevel()
w5.iconbitmap(icon)
w5.geometry("200x170")
w5.resizable(0, 0)
w5.title("Operation Success")
w5.withdraw()
label5 = Label(w5, text = f"Script Executed\n{files_removed}/2 files removed\n{files_replaced}/2 files replaced\n{error_num} errors occured", justify=CENTER)
label5.pack(side=TOP)
frame1 = Frame(w5)
frame1.pack(side=TOP, fill=BOTH)
button1 = ttk.Button(frame1, text="open error log", command=lambda: w2.deiconify())
button1.grid(row=0, column=0)
button2 = ttk.Button(frame1, text="open console log", command=lambda: w3.deiconify())
button2.grid(row=0, column=1)
button3 = ttk.Button(frame1, text="quit program", command=lambda: w.destroy())
button3.grid(row=1, columnspan=2)

else:
    label0["fg"] = "red"
    label0["text"] = "  ● No Admin permissions."
    w.update()
    w.update_idletasks()
    messagebox.showerror("Permission Error", "Please, quit the program and run it with administrator permissions")
    quit()

while True:
    try:
        w.update()
        w.update_idletasks()
    except tkinter.TclError:
        quit()
