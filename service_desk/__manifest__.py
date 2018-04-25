# -*- coding: utf-8 -*-
{
    'name': "service_desk",

    'summary': """
        Mesa de servicios adaptado para la Universidad Andina Simón Bolívar""",

    'description': """
        Mesa de servicios adaptado para la Universidad Andina Simón Bolívar
    """,

    'author': "UASB-EC",
    'website': "http://www.uasb.edu.ec",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_issue.xml',
    ],
}