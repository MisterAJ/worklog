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
        if self.date == date:
            return self

    def find_by_time(self, time):
        if self.time == time:
            return self

    def find_by_exact(self, string):
        if self.name == string or self.notes == string:
            return self

    def find_by_pattern(self, pattern):
        if (bool(re.search(pattern, self.name)) or
                bool(re.search(pattern, self.notes))):
            return self
