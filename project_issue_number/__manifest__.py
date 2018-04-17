# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project Issue Sequence',
    'version': '10.0.0.1',
    'author': 'UASB-E',
    'category':'Project',
    'website': 'www.uasb.edu.ec',
    'summary': 'Este módulo crea un secuencial de los tickets',
    'description':""" Este módulo crea un secuencial de los tickets.""",
    'depends':['project','rating_project_issue'],
    'data':[
        'data/ir_sequence_data.xml',
        'views/project_issue.xml',
        ],
    'installable': True,
    'auto_install': False
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
