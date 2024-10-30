print('Welcome To your Personalised Task Tracker')

print('Here You can add, delete tasks, mark their progress as well as make a todo list')

global tsk
global action

def addtsk():
    tsk = input('enter the task: ')
    f = open("/home/s/code/tasktracker/tasks.txt", "w" )
    f.write(tsk)
    if (tsk==""):
        return (addtsk())
    else:
        print("task saved")




print('To Add a task type "add" and press enter')

action = input()
if (action=='add'):
    addtsk()
