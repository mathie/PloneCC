from Products.Archetypes.public import listTypes
from Products.Archetypes.Extensions.utils import installTypes, \
     install_subskin
from cStringIO import StringIO

from Products.PloneCC.config import *

def install(self):
    out = StringIO()
    installTypes(self, out, listTypes(PKG_NAME), PKG_NAME)
    install_subskin(self, out, GLOBALS)
    print >> out, "Successfully installed %s." % PKG_NAME
    return out.getvalue()
