import re
import cdu
from cdu.models import Uiu

from django.conf import settings
import os

import random

class Document(object):
    uiu = []
    urbanistic_plans = []
    personal_data = []
    template_file_path = ''

    def __init__(self, u, p, d):
        super(Document, self).__init__()
        self.uiu = u
        self.urbanistic_plans = p
        self.personal_data = d
        self.template_file_path = settings.CDU_TEMPLATE_PATH
        self.intersections = []
        self.out_file_path = os.getcwd()+'/cdu/templates/cdu/'


    def create_intersections(self):
        """
        creates intersections between uiu and urbanistic plans polygons
        """
        models = cdu.models.__dict__
        urbanistic_models = [models[p.capitalize()] for p in self.urbanistic_plans]
        for uiu in self.uiu.values():
            index = uiu.find('-')
            if index != -1:
                u = {'fg': uiu[0:index], 'num': uiu[index+1:len(uiu)]}
                try:
                    uiu = Uiu.objects.get(foglio=u['fg'], numero=u['num'],
                                          tipologia='PARTICELLA')
                except:
                    uiu = None
                if uiu:
                    intersect_object = {}
                    intersect_object['fg'] = u['fg']
                    intersect_object['num'] = u['num']
                    intersect_object['area'] = uiu.the_geom.area
                    intersect_object['intersections'] = []
                    for model in urbanistic_models:
                        intersecting_polygons = model.objects.filter(
                            the_geom__intersects=uiu.the_geom)
                        for i in intersecting_polygons:
                            intersection = {}
                            intersection['intersection_area'] = i.the_geom. \
                            intersection(uiu.the_geom).area
                            intersection['intersection_percentage'] = \
                            (intersection['intersection_area'] * 100) \
                            / intersect_object['area']
                            intersection['urbanistic_plan'] = \
                            re.sub('urbutm$', '', model.__name__)
                            intersection['urbanistic_zone'] = str(i.string)
                            intersect_object['intersections'].append(intersection)
                    self.intersections.append(intersect_object)

    def create_html_document(self):
        """
        creates a pdf document from html template replacing tokens
        """
        self.create_intersections()
        if len(self.intersections) > 0:
            template_file = open(self.template_file_path)
            text = template_file.read()

            #personal_data
            text = text.replace('{protocollo}',
                                self.personal_data['num_protocollo'])
            text = text.replace('{dataprotocollo}',
                                self.personal_data['data_protocollo'])
            text = text.replace('{protocollorichiesta}',
                                self.personal_data['num_richiesta'])
            text = text.replace('{datarichiesta}',
                                self.personal_data['data_richiesta'])
            text = text.replace('{cognome}', self.personal_data['cognome'])
            text = text.replace('{nome}', self.personal_data['nome'])
            text = text.replace('{luogo_nascita}',
                                self.personal_data['luogo_nascita'])
            text = text.replace('{prov_nascita}',
                                self.personal_data['prov_nascita'])
            text = text.replace('{data_nascita}',
                                self.personal_data['data_nascita'])
            text = text.replace('{citta}', self.personal_data['citta'])
            text = text.replace('{pv}', self.personal_data['pv'])
            text = text.replace('{indirizzo}', self.personal_data['indirizzo'])


            #html lists of uiu and intersections
            list_uiu = '<ul>'
            list_intersections = ''
            for i in self.intersections:
                list_uiu += '<li>foglio: '+i['fg']+' numero: '+i['num']+'</li>'

            if len(i['intersections']) > 0:
                list_intersections += '<p>che il foglio '+i['fg']+', numero '+ \
                i['num']+' <b>('+str(round(i['area'], 2))+ \
                'mq)</b> &egrave; incluso nel piano urbanistico:<br><ol>'
                plans = []
                for plan in i['intersections']:
                    if plan['urbanistic_plan'] not in plans:
                        plans.append(plan['urbanistic_plan'])

                for plan in plans:
                    list_intersections += '<li><b>'+plan+'</b></li><ul>'
                    for z in i['intersections']:
                        if z['urbanistic_plan'] == plan:
                            list_intersections += '<li>per <b>' + \
                            str(round(z['intersection_area'], 2)) + \
                            ' mq</b> nella zona ' + z['urbanistic_zone']+'</li>'

                list_intersections += '</ol>'

            list_uiu += '</ul>'

            text = text.replace('{elencoplle}', list_uiu)
            text = text.replace('{certifica}', list_intersections)


            #TODO:: add norme texts
            text = text.replace('{norme}', '')

            out_file_name = 'cdu_'+str(random.randrange(1, 999999))+'.html'
            self.out_file_path += out_file_name
            out_file = open(self.out_file_path, 'w')
            out_file.write(text)
            out_file.close()

            return out_file_name
        else:
            return False



    def remove_html_document(self):
        """
        removes html document template
        """
        os.remove(self.out_file_path)
