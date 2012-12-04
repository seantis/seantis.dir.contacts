from seantis.dir.contacts.tests import IntegrationTestCase
from seantis.dir.contacts.contact import IContactPerson


class TestContactPerson(IntegrationTestCase):

    def test_add(self):
        person = self.add_contact('BDFL')
        self.assertTrue(IContactPerson.providedBy(person))
        self.assertEqual(person.id, 'BDFL')

    def test_name(self):
        person = self.add_contact()
        person.first_name = 'Guido'
        person.last_name = 'van Rossum'
        self.assertEqual(person.title, 'Guido van Rossum')
