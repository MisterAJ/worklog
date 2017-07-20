import re


class Task:
    '''Class for the '''
    name = None
    date = None
    notes = None
    time = None

    def __init__(self, name, date, time, notes, **kwargs):
        self.name = name
        self.time = time
        self.notes = notes
        self.date = date

        for key, value in kwargs.items():
            setattr(self, key, value)

    def print(self):
        print('\nName            - {}'
              '\nTime Taken(min) - {}'
              '\nDate            - {}'
              '\nNotes           - {}\n'
              '\n----------------------------\n'
              .format(self.name, self.time, self.date, self.notes))

    def find_by_date(self, date):
        return self.date == date

    def find_by_time(self, time):
        return self.time == time

    def find_by_exact(self, string):
        return self.name == string or self.notes == string

    def find_by_pattern(self, pattern):
        return (bool(re.search(pattern, self.name)) or
                bool(re.search(pattern, self.notes)))

    def string(self):
        return (self.name + ',' + self.time +
                ',' + self.date + ',' + self.notes
                + '\n')
