from model import task
from collections import OrderedDict
import datetime

task_item = task.Task
task_list = []


def menuloop():
    '''Function for the menu loop'''

    toggle = None
    while toggle != 'q':
        print('')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        toggle = input('\nMake a selection (q to quit): ').lower().strip()
        if toggle == 'a':
            add_entry()
        if toggle == 'v':
            view_entries()


def add_entry():
    '''Add an Entry'''
    name = input('\nName\n>>> ')
    time = input('Time Taken\n>>> ')
    notes = input('Notes\n>>> ')
    try:
        task_list.append(
            task.Task(name=name, time=time, notes=notes,
                      date=datetime.datetime.now().strftime('%m/%d/%Y')))
    except ValueError:
        print('Invalid input')


def view_entries():
    '''View Entries'''
    for item in task_list:
        item.print()


def by_date(search_string):
    input('Please enter a date - MM/DD/YYYY')
    for item in task_list:
        print(item.find_by_date(search_string))
    pass


def by_time(search_string):
    input('Please enter number of minutes')
    for item in task_list:
        print(item.find_by_time(search_string))
    pass


def by_exact(search_string):
    input('Please enter exact phrase to search by')
    for item in task_list:
        print(item.find_by_exact(search_string))
    pass


def by_pattern(search_string):
    input('Please enter a regex pattern')
    for item in task_list:
        print(item.find_by_pattern(search_string))
    pass


def search_loop():
    '''Function for the search loop'''
    toggle = None
    while toggle != 'b':
        print('')
        for key, value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        toggle = input('\nMake a selection '
                       '(b to return to the main menu): ').lower().strip()
        if toggle == 'd':
            by_date()
        if toggle == 't':
            by_time()
        if toggle == 'e':
            by_exact()
        if toggle == 'p':
            by_pattern()



menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries)
])

if __name__ == '__main__':
    menuloop()

# find by date
# find by time spent
# find by exact search
# find by pattern