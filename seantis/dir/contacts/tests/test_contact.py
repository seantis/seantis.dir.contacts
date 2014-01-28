from plone import api

from seantis.dir.contacts.tests import IntegrationTestCase
from seantis.dir.contacts.contact import IContactPerson


class TestContactPerson(IntegrationTestCase):

    def test_add(self):
        with self.user('admin'):
            person = api.content.create(
                container=self.new_temporary_folder(),
                type='seantis.dir.contacts.contact',
                title='BDFL'
            )

            self.assertTrue(IContactPerson.providedBy(person))
            self.assertEqual(person.id, 'bdfl')

    def test_name(self):
        with self.user('admin'):
            person = api.content.create(
                container=self.new_temporary_folder(),
                type='seantis.dir.contacts.contact',
                title='BDFL'
            )
            person.first_name = 'Guido'
            person.last_name = 'van Rossum'
            self.assertEqual(person.title, 'Guido van Rossum')
