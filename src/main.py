import time
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import sys
#test
running = True
counting = False

time_elapsed = 0
state = 1
start_time = 0

root = tk.Tk()
root.title('Handy timer')
root['bg'] = '#006600'

running_time_str = tk.StringVar()
project_name = tk.StringVar()

#Elements
#ROW 1
project_label = tk.Label(root,text = 'Project name')
project_label.grid(row=0,column=1,padx=(10,10))

project_entry = tk.Entry(root,font='helvetica 15', textvariable=project_name)
project_entry.grid(row=1,column=1,padx=(10,10))

#PROBLEM : Single-line only
#project_details = tk.Entry(root,text = 'yo',font='helvetica 15', textvariable=project_name)
#project_details.grid(row=2,column=1,padx=(10,10))

project_details = ScrolledText(root, width=50, height=5)
project_details.grid(row=2,column=1)
project_details.insert(0.0,"")

save_button = tk.Button(root, command= lambda : save(), text='Save', font='helvetica 20', width=35,
                         height=2, bg = '#446600')
save_button.grid(row=3,column = 1 ,pady=(10,3),padx=(3,10))


#ROW 2
sesh_label = tk.Label(root,text = 'Current session length')
sesh_label.grid(row=0,column=0)

time_label = tk.Label(root,font='helvetica 20',textvariable = running_time_str,relief='sunken',width=10)
time_label.grid(row=1,column=0)

start_button = tk.Button(root, command= lambda : handle_button(), text='Start', font='helvetica 15', width=15,
                         height=3, bg= '#446600')
start_button.grid(row=2,column=0,pady=(10,3),padx=(3,10))

reset_button = tk.Button(root, command= lambda : reset(), text='Reset', font='helvetica 15', width=15,
                         height=3, bg = '#446600')
reset_button.grid(row=3,column=0,pady=(10,3),padx=(3,10))


#Bindings
root.protocol("WM_DELETE_WINDOW", root.iconify)
root.bind('<Delete>', lambda e: on_exit())

def reset():
    global time_elapsed, running_time_str,counting,state
    if counting:
        counting = False
        state = 1
        start_button.configure(text='Start')
    time_elapsed = 0
    running_time_str.set('00:00:00')


def save():
    f = open('G:\\PythonProjects\\timer\\src\\python_timer.txt', 'a+')
    print(sys.path[0])
    f.write('>>>>Date: ' + time.strftime('%e:%b:%G',time.gmtime(time.time())) + '\n' +
            '>>>Elapsed time: ' + running_time_str.get() + '\n' +
            '>>Subject: ' + project_name.get() + '\n' +
            '>Details:\n' + project_details.get(0.0,'end') + '\n\n')
    f.close()

def on_exit(): # Set running to false before destroying
    global running
    running=False
    root.destroy()

def handle_button():
    global state, counting, time_elapsed,start_time
    if state ==0:
        start_button.configure(text='Start')
        counting = False
        time_elapsed = get_sec(running_time_str.get())
        state=1
    else:
        start_button.configure(text='Stop')
        start_time = time.time()
        counting = True
        state=0

def start():
    print("started")
    print(project_name.get())
    print(project_details.get(0.0, 'end'))

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

while running:
    if counting:
        running_time_str.set(time.strftime('%H:%M:%S', time.gmtime(time_elapsed + round(time.time() - start_time))))
        time.sleep(0.1)
    root.update_idletasks()
    root.update()

