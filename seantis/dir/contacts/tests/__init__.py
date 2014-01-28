from zope.security.management import newInteraction, endInteraction

from seantis.plonetools.testing import TestCase
from seantis.dir.contacts.testing import (
    INTEGRATION_TESTING,
    FUNCTIONAL_TESTING
)


class IntegrationTestCase(TestCase):
    layer = INTEGRATION_TESTING

    def setUp(self):
        super(IntegrationTestCase, self).setUp()
        # setup security
        newInteraction()

    def tearDown(self):
        endInteraction()
        super(IntegrationTestCase, self).tearDown()


# to use with the browser which does its own security interactions
class FunctionalTestCase(TestCase):
    layer = FUNCTIONAL_TESTING
