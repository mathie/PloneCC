from AccessControl import ClassSecurityInfo
from Products.CMFCore.utils import getToolByName, UniqueObject, \
     SimpleItemWithProperties
from Products.CMFCore.CMFCorePermissions import ManagePortal
from Products.PageTemplates.PageTemplateFile import PageTemplateFile

import os

class CreativeCommonsTool(UniqueObject, SimpleItemWithProperties):

    security = ClassSecurityInfo()

    id = 'creativecommons_tool'
    title = 'Manage the Creative Commons license used on this site'
    meta_type = 'Creative Commons Tool'

    manage_options = (({'label': 'Overview',
                        'action': 'manage_overview'},) +
                      SimpleItemWithProperties.manage_options)
    security.declareProtected(ManagePortal, 'manage_overview')
    manage_overview = PageTemplateFile(os.path.join('www', 'manage_overview'),
                                       globals())
    manage_overview.__name__ = 'manage_overview'
    manage_overview.__need__name__ = 0

    _properties = (
        {'id':'license_url', 'type':'string', 'mode':'r',
         'label':'License URL'},
        {'id':'license_name', 'type':'string', 'mode':'r',
         'label':'Name of the Creative Commons License'},
        {'id':'license_button', 'type':'string', 'mode':'r',
         'label':'The button to signify the license'},
        {'id':'deed_url', 'type':'string', 'mode':'r',
         'label':'Deed URL'},
        {'id':'copyright_text', 'type':'string', 'mode':'w',
         'label':'Copyright text displayed on pages'},
        )

    license_url = ''
    license_name = ''
    license_button = ''
    deed_url = ''
    
    _license_engine_url = 'http://creativecommons.org/license/'
    _license_permits = ''
    _license_requires = ''
    _license_prohibits = ''
    
    def getPartner(self):
        return 'PloneCC'

    def getExitUrl(self):
        return self.absolute_url() + '/manage_licenseOptions?license_url=[license_url]&license_name=[license_name]&license_button=[license_button]&deed_url=[deed_url]'

    def getPartnerIconUrl(self):
        return self.absolute_url() + '/logo.jpg'

    def getLicenseEngineUrl(self):
        return self._license_engine_url

    def getLicenseUrl(self):
        return self.license_url

    def getLicenseName(self):
        return self.license_name

    def getButtonUrl(self):
        return self.license_button

    def getLicensePermits(self):
        return self._license_permits

    def getLicenseRequires(self):
        return self._license_requires

    def getLicenseProhibits(self):
        return self._license_prohibits

    # Strictly speaking, this ought to be done in a page template, I
    # suppose, but it's supposed to be inside a comment, and I'm not
    # sure how to achieve that...
    def getRDFInformation(self, obj):
        rdf = '<!--\n<rdf:RDF xmlns:cc="http://web.resource.org/cc/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">\n'
        rdf += '<cc:Work rdf:about="">\n'
        
        if obj:
            for i in ['title', 'description', 'subject', 'publisher',
                      'creator', 'contributor', 'rights', 'date',
                      'format', 'source']:
                attrfn = getattr(obj, i.capitalize(), None)
                if attrfn:
                    attr = attrfn()
                else:
                    attr = None
                if attr:
                    rdf += '<dc:%s>%s</dc:%s>\n' % (i, attr, i)
        rdf += '<cc:license rdf:resource="%s" />\n' % self.getLicenseUrl()
        rdf += '</cc:Work>\n'
        rdf += '<cc:License rdf:about="%s">' % self.getLicenseUrl()
        for require in self.getLicenseRequires():
            rdf += '<cc:requires rdf:resource="%s" />\n' % require
        for permit in self.getLicensePermits():
            rdf += '<cc:permits rdf:resource="%s" />\n' % permit
        for prohibit in self.getLicenseProhibits():
            rdf += '<cc:prohibits rdf:resource="%s" />\n' % prohibit
        rdf += '</cc:License></rdf:RDF> -->\n'
        return rdf

    def _parseLicenseName(self, ln):
        Reproduction    = 'http://web.resource.org/cc/Reproduction'
        Distribution    = 'http://web.resource.org/cc/Distribution'
        DerivativeWorks = 'http://web.resource.org/cc/DerivativeWorks'
        Notice          = 'http://web.resource.org/cc/Notice'
        Attribution     = 'http://web.resource.org/cc/Attribution'
        ShareAlike      = 'http://web.resource.org/cc/ShareAlike'
        CommercialUse   = 'http://web.resource.org/cc/CommercialUse'
        
        if ln == 'Attribution':
            self._license_permits =   [Reproduction, Distribution, DerivativeWorks]
            self._license_requires =  [Attribution, Notice]
            self._license_prohibits = [ ]
        elif ln == 'Attribution-NoDerivs':
            self._license_permits =   [Reproduction, Distribution]
            self._license_requires =  [Attribution, Notice]
            self._license_prohibits = [ ]
        elif ln == 'Attribution-NoDerivs-NonCommercial':
            self._license_permits =   [Reproduction, Distribution]
            self._license_requires =  [Attribution, Notice]
            self._license_prohibits = [CommercialUse]
        elif ln == 'Attribution-NonCommercial':
            self._license_permits =   [Reproduction, Distribution, DerivativeWorks]
            self._license_requires =  [Attribution, Notice]
            self._license_prohibits = [CommercialUse]
        elif ln == 'Attribution-NonCommercial-ShareAlike':
            self._license_permits =   [Reproduction, Distribution, DerivativeWorks]
            self._license_requires =  [Attribution, Notice, ShareAlike]
            self._license_prohibits = [CommercialUse]
        elif ln == 'Attribution-ShareAlike':
            self._license_permits =   [Reproduction, Distribution, DerivativeWorks]
            self._license_requires =  [Attribution, Notice, ShareAlike]
            self._license_prohibits = [ ]
        elif ln == 'Public Domain':
            self._license_permits =   [Reproduction, Distribution, DerivativeWorks]
            self._license_requires =  [ ]
            self._license_prohibits = [ ]
        else:
            self._license_permits =   [ ]
            self._license_requires =  [ ]
            self._license_prohibits = [ ]
        return

    def isPublicDomain(self):
        return self.license_name == 'Public Domain'
    
    security.declareProtected(ManagePortal, 'manage_license_options')
    def manage_licenseOptions(self, license_url = None, REQUEST = None,
                              license_name = None, license_button = None,
                              deed_url = None):
        """ Set the license options passed in from CC's form. """
        if license_url:
            self.license_url = license_url
        if license_name:
            self.license_name = license_name
            self._parseLicenseName(license_name)
        if license_button:
            self.license_button = license_button
        if deed_url:
            self.deed_url = deed_url
        REQUEST.RESPONSE.redirect(self.absolute_url() + '/manage_overview?manage_tabs_message=Tool+Updated')
        return
