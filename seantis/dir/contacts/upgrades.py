from Products.CMFCore.utils import getToolByName


def upgrade_2_to_3(context):

    setup = getToolByName(context, 'portal_setup')
    setup.runImportStepFromProfile(
        'profile-seantis.dir.contacts:default', 'cssregistry'
    )
