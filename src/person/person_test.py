from unittest import TestCase
from person.person import Person

class PersonTest(TestCase):

    person = Person('Lewis')

    def test_person(self):
        assert self.person.name == 'Lewis'

    def test_personHasCashAttribute0asDefault(self):
        assert self.person.cash == 0
