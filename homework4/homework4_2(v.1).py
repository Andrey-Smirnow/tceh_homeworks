#Task 3 (var. 1)
# Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод:
# log(*values). Написать класс FormattedPrinter, который выводит в консоль информацию,
# окружая ее строками из *

class Printer(object):

    def log(self, *values):
        return str(values)


class FormattedPrinter(Printer):

    def log_with_stars(self, *values):
        # Если Printer.log(*values) возвращает строковое значение:
        print('***\n' + self.log(*values) + '\n***')


a = Printer()
b = FormattedPrinter()

print()
print(a.log(25, 'a', 34.2, [25, 34], True))
print()
print(b.log_with_stars(25, 'a', 34.2, [25, 34], True))








