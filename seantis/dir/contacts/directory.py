from five import grok
from zope.interface import alsoProvides
from plone.namedfile.field import NamedImage
from plone.autoform.interfaces import IFormFieldProvider
from plone.directives import form

from seantis.dir.base import core
from seantis.dir.base import directory

from seantis.dir.contacts import _

class IContactsDirectory(form.Schema):
    """Extends the seantis.dir.base.directory.IDirectory"""

    image = NamedImage(
            title=_(u'Image'),
            required=False,
            default=None
        )

alsoProvides(IContactsDirectory, IFormFieldProvider)

@core.ExtendedDirectory
class ContactsDirectoryFactory(core.DirectoryMetadataBase):
    interface = IContactsDirectory

class ContactsDirectory(directory.Directory):
    pass

class ExtendedDirectoryViewlet(grok.Viewlet):
    grok.context(directory.IDirectory)
    grok.name('seantis.dir.base.directory.detail')
    grok.require('zope2.View')
    grok.viewletmanager(directory.DirectoryViewletManager)

    template = grok.PageTemplateFile('templates/directorydetail.pt')
