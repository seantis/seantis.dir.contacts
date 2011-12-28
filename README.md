# Introduction

seantis.dir.base allows to put dexterity objects into 1-4 categories, showing those categories in a browsable and searchable catalog.
To learn more about seantis.dir.base visit [https://github.com/seantis/seantis.dir.base](https://github.com/seantis/seantis.dir.base)

seantis.dir.contacts builds on seantis.dir.base, adding contact person types and fields to build a catalog of personell.

# Dependencies

seantis.dir.contacts relies on Plone 4.0+ with dexterity and seantis.dir.base:

# Installation

1. Add dexterity to Plone by adding the following Known Good Set to your buildout.cfg:

        extends =
            ...
            http://good-py.appspot.com/release/dexterity/1.1?plone=4.1.2

2. Add the module to your instance eggs

        [instance]
        ...
        eggs =
            ...
            seantis.dir.contacts

3. Install dexterity and seantis.dir.contacts using portal_quickinstaller

# License

seantis.dir.contacts is released under GPL v2

# Maintainer

seantis.dir.contacts is maintained by Seantis GmbH (www.seantis.ch)