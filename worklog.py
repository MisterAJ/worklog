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
        if toggle == 's':
            search_loop()


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
    '''Search by Date'''
    for item in task_list:
        print(item.find_by_date(search_string))
    pass


def by_time(search_string):
    '''Search by Time'''
    for item in task_list:
        print(item.find_by_time(search_string))
    pass


def by_exact(search_string):
    '''Search by Exact phrase'''
    for item in task_list:
        print(item.find_by_exact(search_string))
    pass


def by_pattern(search_string):
    '''Search by Regex pattern'''
    for item in task_list:
        print(item.find_by_pattern(search_string))
    pass


def search_loop():
    '''Search for tasks'''
    toggle = None
    while toggle != 'b':
        print('')
        for key, value in search_menu.items():
            print('{}) {}'.format(key, value.__doc__))
        toggle = input('\nMake a selection '
                       '(b to return to the main menu): ').lower().strip()
        if toggle == 'd':
            by_date(input('Please enter a date - MM/DD/YYYY'))
        if toggle == 't':
            by_time(input('Please enter number of minutes'))
        if toggle == 'e':
            by_exact(input('Please enter exact phrase to search by'))
        if toggle == 'p':
            by_pattern(input('Please enter a regex pattern'))

search_menu = OrderedDict([
    ('d', by_date),
    ('t', by_time),
    ('e', by_exact),
    ('p', by_pattern)
])

menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_loop)
])

if __name__ == '__main__':
    menuloop()