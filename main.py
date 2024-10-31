import datetime
import json
import colorama


def addtsk():
    tsk=[]
    while True:
        utsk=input(colorama.Fore.GREEN + colorama.Style.BRIGHT+'Enter the task')
        print('task saved')
        tsk.append(utsk)
        if (utsk=='exit'):
            break
        with open('tasks.json', 'w') as tsks:
            json.dump(tsk, tsks)

def  showtsk():
    dt=str(datetime.datetime.now())
    with open('tasks.json', 'r')as fp:
        for x in fp:
            print(x+dt)






def action():
    action=input('Enter "add" to add a task \n Enter "show" to show tasks')
    if (action=='add'):
        addtsk()
    elif (action=='show'):
        showtsk()


action()
