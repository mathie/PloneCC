
# __pkginfo__.py is modeled after the data found in Archetypes' similar
# file, except that I don't duplicate so much information. :-)  Dunno
# what it really does either.

from re import split
import os, sys

# Things you want to specify
_copyrightYear = '2004'
author = 'Graeme Mathieson'
author_email = 'mathie@woss.name'
license = 'GPL'
short_desc = 'Creative Commons support for Plone'
web = 'http://woss.name/software/PloneCC/'
ftp = ''
mailing_list = ''
debian_maintainer = ''
debian_maintainer_email = ''

# Workings
_productPath = os.path.dirname(os.path.abspath(__file__))

# Stuff that's calculated automatically
modname = _productPath.split('/')[-1]
version = file('%s/version.txt' % _productPath).readlines()[0].rstrip()
numversion = tuple(split('[-.]', version))
copyright = 'Copyright (c) %s %s <%s>' % (_copyrightYear, author,
                                          author_email)
long_desc = '\n'.join([line.rstrip() or '.'
                       for line in
                       file('%s/README.txt' % _productPath).readlines()])

debian_name = 'zope-cmf%s' % modname.lower()
debian_handler = 'zope'
