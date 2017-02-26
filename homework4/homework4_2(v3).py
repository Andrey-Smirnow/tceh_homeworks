#Task 2 (var. 3)
# Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод:
# log(*values). Написать класс FormattedPrinter, который выводит в консоль информацию,
# окружая ее строками из *

# Task 2 (var. 3)


class Printer_1:

    def __init__(self):
        self.logs = None

    @staticmethod
    def print_info(info):
        print(info)

    def log(self, *values):
        self.logs = values


class FormatedPrinter_1:

    @staticmethod
    def form_printer(info, val):
        if val.logs is None:
            raise RuntimeError('Printer class method "log" not initiated')
        print('{0} {1} {0}'.format(''.join([str(text) for text in val.logs]), info))

print('Task 3 (var.2)'.center(70))
    a_1 = Printer_1()
    a_1.log('Some_text', 1, [])
    b_1 = FormatedPrinter_1()
b_1.form_printer('aaa', a_1)



