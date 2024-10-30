print('Welcome To your Personalised Task Tracker')

print('Here You can add, delete tasks, mark their progress as well as make a todo list')


def addtsk():
    tsk = input('enter the task: ')
    f = open("/home/s/code/trackr/trackr/tasks.txt", "w" )
    f.write(tsk)
    if (tsk==""):
        return (addtsk())
    else:
        print("task saved")

def progress():
    print('If you have completed the task type done')
    don = input()
    if (don=='done'):
        return (deltsk())
    else:
        print("What is the Status of your Task?")



def deltsk():
    f = open("/home/s/code/trackr/trackr/tasks.txt", "w")
    f.write("Nothing to see Here")
    f.close()

print('To Add a task type "add" and press enter')

action = input()
if (action=='add'):
    addtsk()
elif (action=='del'):
    deltsk()
elif (action=='prog'):
    progress()

