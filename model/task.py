class Task():
    name = ''
    date = ''
    description = 'Eat food'
    notes = ''
    time_spent = 0

    def __init__(self, name, date, description, notes, **kwargs):
        self.name = name
        self.description = description
        self.notes = notes

        for key, value in kwargs.items():
            setattr(self, key, value)

    def print(self):
        print(self.name)
        print(self.description)
        print(self.notes)

    def find_by_date(self, date):
        if self.date == date:
            return self

    def find_by_time(self, time):
        if self.time_spent == time:
            return self

    def find_by_exact(self, string):
        if self.name == string or self.notes == string:
            return self

    def find_by_pattern(self, pattern):
        return self