from setuptools import setup, find_packages
import os

version = '0.3'

setup(name='seantis.dir.contacts',
      version=version,
      description="Directories for the canton of Zug",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Seantis GmbH',
      author_email='info@seantis.ch',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['seantis', 'seantis.dir'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'plone.app.dexterity',
          'collective.autopermission',
          'collective.testcaselayer',
          'collective.dexteritytextindexer'
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
