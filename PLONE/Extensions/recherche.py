
import logging
import pdb
from plone import api

logger = logging.getLogger('external: ')

stdTypes = []
stdTypes.append('Folder')
stdTypes.append('Document')
stdTypes.append('Image')
stdTypes.append('Event')
stdTypes.append('File')
stdTypes.append('News Item')
stdTypes.append('Collection')

def countTypes(self):
    # logger.info(self)
    folder_path = '/'.join(self.getPhysicalPath())
    portal = api.portal.get()
    catalog = portal.portal_catalog
    results = catalog.searchResults(
        path={'query': folder_path, 'depth': 9},)
    p_types = {}
    for brain in results:
        obj = brain.getObject()
        p_type = obj.portal_type
        if p_types.get(p_type):
            p_types[p_type]['nb'] += 1
            p_types[p_type]['objs'].append(obj.absolute_url())
        else:
            p_types[p_type] = {}
            p_types[p_type]['nb'] = 1
            p_types[p_type]['objs'] = []
            p_types[p_type]['objs'].append(obj.absolute_url())
    html = u"<html>"
    html += u"<head>"
    html += u"</head>"
    html += u"<body>"
    html += u"<table><tbody>"
    for k in p_types.keys():
        if k not in stdTypes:
            html += u'<tr style="color: red">'
        else:
            html += u"<tr>"
        html += u"<td>" + k + u"</td>"
        html += u"<td>" + str(p_types[k]['nb']) + u"</td>"
        html += u"</tr>"
    html += u"</tbody></table><br /><br />"
    # pdb.set_trace()
    html += u"<table><tbody>"
    for k in p_types.keys():
        if k not in stdTypes:
            for url in p_types[k]['objs']:
                html += u"<tr>"
                html += u"<td>" + k + u"<td>"
                html += u'<td>'
                html += u'<a href="' + url + u'"target="_blank">' + url
                html += u'<td>'
                html += u"</tr>"

    html += u"</tbody></table>"
    html += u"</tbody></table></body></html>"
    return html


