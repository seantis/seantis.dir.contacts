Introduction
============

seantis.dir.contacts allows to keep a directory of contacts for display on
a Plone site.

seantis.dir.contacts builds on seantis.dir.base, adding contact person
types and fields to build a catalog of personell.


Build Status
============

.. image:: https://secure.travis-ci.org/seantis/seantis.dir.contacts.png
   :target: https://travis-ci.org/seantis/seantis.dir.contacts


Installation
============

1. Add dexterity to Plone by adding the following Known Good Set to your buildout.cfg::

    extends =
        ...
        http://good-py.appspot.com/release/dexterity/1.1?plone=4.1.2


2. Add the module to your instance eggs::

    [instance]
    ...
    eggs =
        ...
        seantis.dir.contacts


3. Ensure that the i18n files are compiled by adding::

    [instance]
      ...
      environment-vars =
        ...
        zope_i18n_compile_mo_files true


4. Install dexterity and seantis.dir.contacts using portal_quickinstaller


Links
=====

- Main github project repository: https://github.com/seantis/seantis.dir.contacts
- Issue tracker: https://github.com/seantis/seantis.dir.contacts/issues
- Package on pypi: http://pypi.python.org/pypi/seantis.dir.contacts
- Continuous integration: https://travis-ci.org/seantis/seantis.dir.contacts


License
=======

seantis.dir.contacts is released under GPL v2


Maintainer
==========

seantis.dir.contacts is maintained by Seantis GmbH (www.seantis.ch)
