from five import grok
from plone.namedfile.field import NamedImage

from seantis.dir.base import directory
from seantis.dir.contacts import _

class IContactsDirectory(directory.IDirectory):
    """Extends the seantis.dir.base.directory.IDirectory"""

    image = NamedImage(
            title=_(u'Image'),
            required=False,
            default=None
        )

class ContactsDirectory(directory.Directory):
    pass

class ContactsDirectoryViewlet(grok.Viewlet):
    grok.context(IContactsDirectory)
    grok.name('seantis.dir.contacts.directory.detail')
    grok.require('zope2.View')
    grok.viewletmanager(directory.DirectoryViewletManager)

    template = grok.PageTemplateFile('templates/directorydetail.pt')