class Employee:
    pass


e1 = Employee()
e2 = Employee()
print(e1)
print(e2)

e1.first = "Corey"
e1.last = "Max"

print(e1.last + ", " + e1.first)

print('-' * 80)


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


e1 = Employee('Corey', 'Schafer', 50000)
e2 = Employee('Test', 'User', 60000)
print(e1)
print(e2)

print(e1.fullname())
