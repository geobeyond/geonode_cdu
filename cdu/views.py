from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.db import connections

import cdu.document


from wkhtmltopdf.views import PDFTemplateResponse

class MyView(View):


    def get(self, request, *args, **kwargs):
        cursor = connections['gisdata'].cursor()
        cursor.execute("SELECT tablename FROM pg_tables where tablename like '%%urbutm'")
        tables = cursor.fetchall()
        tables = dict((item[0], None) for item in tables)
        context = {'urbanistic_names': tables}
        return render(request, 'cdu/index.html', context)


    def post(self, request, *args, **kwargs):

        uiu = {k:v for k, v in request.POST.iteritems() if 'uiu' in k}
        personal_data = {k:v for k, v in request.POST.iteritems() if 'urbutm' not in k and 'uiu' not in k}
        urbanistic_plans = [k for k, v in request.POST.iteritems() if 'urbutm' in k and v == 'on']

        cdu_doc = cdu.document.Document(uiu, urbanistic_plans, personal_data)
        html_template = cdu_doc.create_html_document()
        if html_template:
            context = {'urbanistic_names': urbanistic_plans}
            pdf = PDFTemplateResponse(request=request,
                                      template='cdu/'+html_template,
                                      filename="cdu.pdf",
                                      context=context,
                                      show_content_in_browser=False)
            pdf.render()
            cdu_doc.remove_html_document()
            response = HttpResponse(content=pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="cdu.pdf"'
            return response

        else:
            #TODO:: adjust not intersections response
            return HttpResponse('Non ci sono intersezioni')
