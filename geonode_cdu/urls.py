from django.conf.urls import patterns, url

from geonode.urls import *

from wkhtmltopdf.views import PDFTemplateView

import cdu.views
import cdu.document

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'geonode.views.index', {'template': 'site_index.html'}, name='home'),
    url(r'^cdu/', cdu.views.MyView.as_view(), name='index'),
    url(r'^pdf/', PDFTemplateView.as_view(template_name='cdu/cdu.html', filename='cdu.pdf'), name='pdf')
 ) + urlpatterns
