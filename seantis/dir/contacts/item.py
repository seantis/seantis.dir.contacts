from five import grok

from zope.schema import TextLine, Text
from plone.memoize import view
from plone.namedfile.field import NamedImage
from plone.directives import form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget
from collective.dexteritytextindexer import searchable
from zope.security import checkPermission

from seantis.dir.base import core
from seantis.dir.base.item import DirectoryItem
from seantis.dir.base.interfaces import (
    IFieldMapExtender,
    IDirectoryItem
)
from seantis.dir.base.fieldmap import FieldMap
from seantis.dir.base.schemafields import Email, AutoProtocolURI

from seantis.dir.contacts import _
from seantis.dir.contacts.directory import IContactsDirectory
from seantis.dir.contacts.contact import IContactPerson


class IContactsDirectoryItem(IDirectoryItem):
    """Extends the seantis.dir.base IDirectoryItem."""

    image = NamedImage(
        title=_(u'Image'),
        required=False,
        default=None
    )

    searchable('street')
    street = TextLine(
        title=_(u'Street'),
        required=False,
        default=u''
    )

    searchable('zipcode')
    zipcode = TextLine(
        title=_(u'Zipcode'),
        required=False,
        default=u''
    )

    searchable('city')
    city = TextLine(
        title=_(u'Town'),
        required=False,
        default=u''
    )

    searchable('phone')
    phone = TextLine(
        title=_(u'Phone'),
        required=False,
        default=u''
    )

    searchable('fax')
    fax = TextLine(
        title=_(u'Fax'),
        required=False,
        default=u''
    )

    searchable('url')
    url = AutoProtocolURI(
        title=_(u'Internet Address'),
        required=False,
        default=None
    )

    searchable('email')
    email = Email(
        title=_(u'Email'),
        required=False,
        default=u''
    )

    searchable('opening_hours')
    opening_hours = Text(
        title=_(u'Opening Hours'),
        required=False,
        default=u''
    )

    searchable('information')
    form.widget(information=WysiwygFieldWidget)
    information = Text(
        title=_(u'Information'),
        required=False,
        default=u''
    )


class ContactsDirectoryItem(DirectoryItem):
    pass


class View(core.View):
    """Default view of a seantis.dir.contacts item."""
    grok.context(IContactsDirectoryItem)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/item.pt')

    @view.memoize
    def contacts(self):
        children = (obj[1] for obj in self.context.contentItems())
        is_contact = lambda child: IContactPerson.providedBy(child)
        is_visible = lambda child: checkPermission('zope2.View', child)

        return [c for c in children if is_contact(c) and is_visible(c)]

    def may_manage(self, contact):
        return checkPermission('cmf.ModifyPortalContent', contact)

    def description(self):
        if self.context.description:
            return self.context.description.split('\n')
        else:
            return None

    def html_opening_hours(self):
        """Returns the opening_hours with newlines replaced by <br/> tags"""
        return self.context.opening_hours and \
            self.context.opening_hours.replace('\n', '<br />') or ''


class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of seantis.dir.base.item.

    """
    grok.context(IContactsDirectory)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self, itemmap):
        itemmap.typename = 'seantis.dir.contacts.item'
        itemmap.interface = IContactsDirectoryItem

        extended = ['street', 'zipcode', 'city', 'phone', 'fax',
                    'url', 'email', 'opening_hours', 'information']

        itemmap.add_fields(extended, len(itemmap))

        contactfields = ['first_name', 'last_name',
                         'street', 'zipcode', 'town', 'phone',
                         'fax', 'email', 'function']

        contactmap = FieldMap()
        contactmap.interface = IContactPerson
        contactmap.typename = 'seantis.dir.contacts.contact'
        contactmap.keyfields = ('first_name', 'last_name')
        contactmap.add_fields(contactfields, len(itemmap))

        itemmap.children.append(contactmap)
