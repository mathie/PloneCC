from Products.CMFCore.DirectoryView import registerDirectory
from Products.Archetypes.ArchetypeTool import process_types, listTypes

from config import *

# Register the skins directory.
registerDirectory('skins', GLOBALS)

def initialize(context):
    # Import content types here to register them:

    content_types, constructors, ftis = \
                   process_types(listTypes(PKG_NAME), PKG_NAME)
    
    from Products.CMFCore import utils
    utils.ContentInit(PKG_NAME + ' Content',
                      content_types = content_types,
                      permission = ADD_CONTENT_PERMISSION,
                      extra_constructors = constructors,
                      fti = ftis).initialize(context)
