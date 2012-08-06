from seantis.dir.base.setuphandlers import get_fti, add_behavior, remove_behavior

def uninstallOldBehaviors(context, logger=None):
    
    fti = get_fti('seantis.dir.base.item')
    remove_behavior(fti, 'seantis.dir.contacts.item.IExtendedDirectoryItem')

    fti = get_fti('seantis.dir.base.directory')
    remove_behavior(fti, 'seantis.dir.contacts.item.IExtendedDirectory')

def installBehavior(context, logger=None):
    """Registers behaviors for seantis.dir.base.item."""

    uninstallOldBehaviors(context, logger)

    fti = get_fti('seantis.dir.base.item')
    add_behavior(fti, 'seantis.dir.contacts.item.IContactsDirectoryItem')

    fti = get_fti('seantis.dir.base.directory')
    add_behavior(fti, 'seantis.dir.contacts.directory.IContactsDirectory')