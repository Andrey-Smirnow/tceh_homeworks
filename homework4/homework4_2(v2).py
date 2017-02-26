#Task 2 (var. 2)
# Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод:
# log(*values). Написать класс FormattedPrinter, который выводит в консоль информацию,
# окружая ее строками из *

# Task 2 (var. 2)
class Printer:

    @staticmethod
    def print_info(info):
        print(info)

    def log(self, *values):
        self.logs = values


class FormatedPrinter:
    
    @staticmethod
    def form_printer(info):
print('*** {} ***'.format(info))

print('Task 3'.center(70))
    a = Printer()
    b = FormatedPrinter
    a.log('Some_text', 1, [])
    a.print_info(a.logs)
    b.form_printer(a.logs)
print('***'.center(70))







