PloneCC

 PloneCC provides complete Creative Commons support for Plone, including
 choosing a license for your site, displaying the appropriate licensing
 information and including the necessary RDF.

 Installation

  Download the tarball and unpack it inside your 'Products' directory
  (either the global Zope Products directory or your own instance, as
  you prefer). Restart your Zope instance. Login as an administrative
  user, go to 'Plone Setup' and choose 'Add/Remove Products'. Select the
  checkbox next to 'PloneCC' and click install.

  Once it successfully installs, there is currently another manual step
  (though I'll try to automate it in the next release).  Go to 'Plone
  Setup', then 'Zope Management Interface'.  From the drop-down box for
  adding new content, select 'PloneCC' and click 'add' (if it doesn't
  happen automagically).  Select the radio button next to 'Creative
  Commons Tool' and click 'Add' again.

 Choosing a License

  In order to choose a license, follow these steps:

  * Login as an admin user.

  * Go to 'Plone Setup' and choose 'Zope Management Interface'

  * Select the 'creativecommons_tool' in your Plone root.

  * Click 'Choose a License' and follow the instructions in the wizard.
    Read the information carefully so that you know exactly what rights
    you are giving away!

  * Once that's finished, you'll be returned to the ZMI with the chosen
    license.

  To display the chosen license on your pages, you'll need to add the
  appropriate portlet.  From the root of your Plone instance in the ZMI
  (ie where you reached after the second step above), select the
  properties tab.  Add to either 'left_slots' or 'right_slots'
  (depending upon your preference) the line
  'here/portlet_plonecc/macros/portlet' and click 'Save Changes'.

  Your site should now display the license portlet with the correct
  license button, linked to the correct place and with the correct meta
  data.  In order to verify it is functioning correctly, you might want
  to try out the "CC RDF License
  Validator":http://validator.creativecommons.org/.
