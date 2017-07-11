from model import task

task_item = task.Task
task_list = []
toggle = 0
while toggle != 'q':
    toggle = input('Make a selection - q to quit')
    if toggle == '1':
        name = input('Name\n>>> ')
        description = input('Description\n>>> ')
        notes = input('Notes\n>>> ')
        task_list.append(task.Task(name=name, description=description, notes=notes))
    if toggle == '2':
        for item in task_list:
            item.print()

# find by date
# find by time spent
# find by exact search
# find by pattern