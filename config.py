from Products.CMFCore.CMFCorePermissions import AddPortalContent
import os

from __pkginfo__ import modname as PKG_NAME

SKIN_NAME = PKG_NAME.lower()
ADD_CONTENT_PERMISSION = AddPortalContent
GLOBALS = globals()

# Setup your preferred Archetypes storage method here...
from Products.Archetypes.Storage import AttributeStorage
DEFAULT_STORAGE = AttributeStorage()
