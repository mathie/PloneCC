from Products.CMFCore.DirectoryView import registerDirectory
from Products.Archetypes.ArchetypeTool import process_types, listTypes
from Products.CMFCore.utils import ToolInit
from CreativeCommonsTool import CreativeCommonsTool
from config import *
 
tools = (CreativeCommonsTool,)

# Register the skins directory.
registerDirectory('skins', GLOBALS)
 
def initialize(context):
    init = ToolInit(PKG_NAME, tools = tools, product_name = PKG_NAME,
                    icon='tool.gif')
    init.initialize(context)
