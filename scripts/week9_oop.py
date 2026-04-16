class Facility:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def display(self):
        print(f'{self.name} - {self.status}')
