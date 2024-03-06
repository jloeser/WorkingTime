class Database:

    def __init__(self):
        pass

    def load(self):
        days = Days()
        for line in textfile:
            day_from_line = Day()
            days.append(day_from_line)
        return days

    def save(self):
        pass


class Days(list):

    def __init__(self):
        pass

    def list(self):
        pass

    def add(self):
        newday = Day()
        self.append(newday)

    def edit(self):
        pass

    def delete(self):
        pass

    def __del__(self):
        print("I am going to be removed...")


class Day:

    def __init__(self, date):
        self.date = date
        print("Hello, I am alive")

    def __del__(self):
        print("I am going to be removed...")
