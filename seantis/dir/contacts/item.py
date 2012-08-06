from five import grok

from zope.schema import TextLine, Text
from zope.schema import URI
from zope.interface import alsoProvides
from plone.memoize import view
from plone.namedfile.field import NamedImage
from plone.autoform.interfaces import IFormFieldProvider
from collective.dexteritytextindexer import IDynamicTextIndexExtender
from plone.directives import form
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from seantis.dir.base import core
from seantis.dir.base import item
from seantis.dir.base.interfaces import IFieldMapExtender
from seantis.dir.base.fieldmap import FieldMap
from seantis.dir.base.schemafields import Email

from seantis.dir.contacts import _
from seantis.dir.contacts.contact import IContactPerson
  
class IContactsDirectoryItem(form.Schema):
    """Extends the seantis.dir.IDirectoryItem."""

    image = NamedImage(
            title=_(u'Image'),
            required=False,
            default=None
        )

    street = TextLine(
            title=_(u'Street'),
            required=False,
            default=u''
        )

    zipcode = TextLine(
            title=_(u'Zipcode'),
            required=False,
            default=u''
        )

    city = TextLine(
            title=_(u'Town'),
            required=False,
            default=u''
        )

    phone = TextLine(
            title=_(u'Phone'),
            required = False,
            default=u''
        )

    fax = TextLine(
            title=_(u'Fax'),
            required = False,
            default=u''
        )

    url = URI(
            title=_(u'Internet Address'),
            required = False,
            default=None
        )

    email = Email(
            title=_(u'Email'),
            required = False,
            default=u''
        )

    opening_hours = Text(
            title=_(u'Opening Hours'),
            required=False,
            default=u''
        )

    form.widget(information=WysiwygFieldWidget)
    information = Text(
            title=_(u'Information'),
            required=False,
            default=u''
        )

alsoProvides(IContactsDirectoryItem, IFormFieldProvider)

@core.ExtendedDirectory
class ContactsDirectoryItemFactory(core.DirectoryMetadataBase):
    interface = IContactsDirectoryItem

class ContactsDirectoryItem(item.DirectoryItem):
    pass

class DirectoryItemSearchableTextExtender(grok.Adapter):
    grok.context(item.IDirectoryItem)
    grok.name('IExtendedDirectoryItem')
    grok.provides(IDynamicTextIndexExtender)

    def __init__(self, context):
        self.context = context

    def __call__(self):
        """Extend the searchable text with a custom string"""
        context = self.context
        get = lambda ctx, attr: hasattr(ctx, attr) and unicode(getattr(ctx, attr)) or u''

        result = ' '.join((
                         get(context, 'street'), 
                         get(context, 'zipcode'),
                         get(context, 'city'),
                         get(context, 'phone'),
                         get(context, 'fax'),
                         get(context, 'url'),
                         get(context, 'email'),
                         get(context, 'opening_hours'),
                         get(context, 'information'),
                    ))

        return result


class ExtendedDirectoryItemViewlet(grok.Viewlet):
    grok.context(item.IDirectoryItem)
    grok.name('seantis.dir.base.item.detail')
    grok.require('zope2.View')
    grok.viewletmanager(item.DirectoryItemViewletManager)

    template = grok.PageTemplateFile('templates/listitem.pt')


class View(core.View):
    """Default view of a seantis.dir.contacts item."""
    grok.context(item.IDirectoryItem)
    grok.require('zope2.View')

    template = grok.PageTemplateFile('templates/item.pt')

    @view.memoize
    def contacts(self):
        children = (obj[1] for obj in self.context.contentItems())
        is_contact = lambda child: IContactPerson.providedBy(child)
        return [c for c in children if is_contact(c)]

    def description(self):
        if self.context.description:
            return self.context.description.split('\n')
        else:
            return None

    def html_opening_hours(self):
        """Returns the opening_hours with newlines replaced by <br/> tags"""
        return self.context.opening_hours and self.context.opening_hours.replace('\n', '<br />') or ''

class ExtendedDirectoryItemFieldMap(grok.Adapter):
    """Adapter extending the import/export fieldmap of seantis.dir.base.item."""
    grok.context(FieldMap)
    grok.provides(IFieldMapExtender)

    def __init__(self, context):
        self.context = context

    def extend_import(self):
        itemmap = self.context
        itemmap.interface = IContactsDirectoryItem

        extended = ['street', 'zipcode', 'city', 'phone', 'fax', 
                    'url', 'email', 'opening_hours']
        
        itemmap.add_fields(extended, len(itemmap))

        contactfields = ['first_name', 'last_name', 
                         'street', 'zipcode', 'phone',
                         'fax', 'email', 'function']

        contactmap = FieldMap()
        contactmap.interface = IContactPerson
        contactmap.typename = 'seantis.dir.contacts.contact'
        contactmap.keyfields = ('first_name', 'last_name')
        contactmap.add_fields(contactfields, len(itemmap))

        itemmap.children.append(contactmap)