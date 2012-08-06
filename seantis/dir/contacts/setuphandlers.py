from zope.component.hooks import getSite

def get_fti(typename):
    types = getSite().portal_types

    if typename in types:
        return types[typename]
    else:
        return None

def add_behavior(fti, behavior):
    if fti:
        behaviors = list(fti.behaviors)
        if not behavior in behaviors:
            behaviors.append(behavior)
            fti.behaviors = tuple(behaviors)

def remove_behavior(fti, behavior):
    if fti:
        behaviors = list(fti.behaviors)
        if behavior in behaviors:
            behaviors.remove(behavior)
            fti.behaviors = tuple(behaviors)

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