from unittest import TestCase
from person.person import Person

class PersonTest(TestCase):
    def person_test():
        person = Person('Lewis')
        assert person.name == 'Lewis'
