from seantis.dir.contacts.tests.layer import Layer
from Products.PloneTestCase.ptc import PloneTestCase


class IntegrationTestCase(PloneTestCase):
    layer = Layer

    def add_contact(self, name='Contact'):
        self.folder.invokeFactory('seantis.dir.contacts.contact', name)
        return self.folder[name]
