from setuptools import setup, find_packages
import os

version = '1.7'

tests_require = [
    'collective.testcaselayer',
]

setup(name='seantis.dir.contacts',
      version=version,
      description="Directory of Contacts",
      long_description='\n'.join((
          open("README.rst").read(),
          open(os.path.join("docs", "HISTORY.txt")).read()
      )),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          'Framework :: Plone',
          'Framework :: Plone :: 4.3',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Libraries :: Python Modules',
          "Programming Language :: Python",
      ],
      keywords='',
      author='Seantis GmbH',
      author_email='info@seantis.ch',
      url='https://github.com/seantis/seantis.dir.contacts',
      license='GPL v2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['seantis', 'seantis.dir'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'collective.autopermission',
          'plone.behavior',
          'plone.directives.form',
          'collective.dexteritytextindexer',
          'seantis.dir.base>=1.7',
      ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
