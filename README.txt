PloneSkel

 This is a skeleton Plone product which shouldn't do anything exciting,
 but it does demonstrate how to create a new Plone product and it should
 provide an easily reusable basis for all my future products.

 In order to customise for a new project, add some content types (if
 using Archetypes) or whatever else, and edit __init__.py:initialize()
 to import them.  Edit __pkginfo__.py to specify metadata for the
 package.  Edit readme.txt (this file) for a product description.
 version.txt should contain the version number of the product.  Remove
 refresh.txt once the product moves into a production environment.  And
 finally, you'll need to modify Extensions/Install.py to import the
 correct config file.

 TODO

   * I've a variable in config.py to set the 'DEFAULT_STORAGE' of
     Archetypes types.  But I haven't actually implemented something to
     set the default storage.  I should do that...
