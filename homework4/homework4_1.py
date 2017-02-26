# Task1
# Реализовать класс Person, у которого должно быть два публичных поля: age и name.
# Также у него должен быть следующий набор методов:
# know(person), который позволяет добавить другого человека в список знакомых.
# И метод is_known(person), который возвращает знакомы ли два человека


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name
        self.friends = []

    def know(self, other_person):
        self.friends.append(other_person)

    def is_known(self, other_person):
        return other_person in self.friends
jack = Person('Jack', 25)
alice = Person('Alice', 24)

print("Does {} ever met {}?".format(jack.name, alice.name), jack.is_known(alice))  # Не понимаю
#                                                                              как работает jack.is_known(alice)
jack.know(alice)           # Не понимаю как работает jack.know(alice)! Мы говорим что Джек встречал Алису!
print("Does {} ever met {}?".format(jack.name, alice.name), jack.is_known(alice))




