from five import grok
from plone.namedfile.field import NamedImage

from seantis.dir.base import directory
from seantis.dir.base.directory import Directory, DirectoryViewletManager
from seantis.dir.base.interfaces import IDirectory
from seantis.dir.contacts import _


class IContactsDirectory(IDirectory):
    """Extends the seantis.dir.base.directory.IDirectory"""

    image = NamedImage(
        title=_(u'Image'),
        required=False,
        default=None
    )


class ContactsDirectory(Directory):
    pass


class ContactsDirectoryViewlet(grok.Viewlet):
    grok.context(IContactsDirectory)
    grok.name('seantis.dir.contacts.directory.detail')
    grok.require('zope2.View')
    grok.viewletmanager(DirectoryViewletManager)

    template = grok.PageTemplateFile('templates/directorydetail.pt')


class View(directory.View):
    grok.context(IContactsDirectory)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/directory.pt')
