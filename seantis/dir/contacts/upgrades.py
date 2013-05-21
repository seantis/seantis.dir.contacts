from Products.CMFCore.utils import getToolByName
from seantis.dir.base.upgrades import reset_images, add_behavior_to_item
from seantis.dir.contacts.directory import IContactsDirectory
from seantis.dir.contacts.item import IContactsDirectoryItem


def upgrade_2_to_3(context):

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-seantis.dir.contacts:default', 'cssregistry'
    )


def upgrade_3_to_1000(context):

    add_behavior_to_item(
        context, 'seantis.dir.contacts', IContactsDirectoryItem
    )
    reset_images(context, (IContactsDirectory, IContactsDirectoryItem))
