# -*- coding: utf-8 -*-
{
    'name': "uasb_talento_humano",

    'summary': """
        Módulo para Talento Humano UASB""",

    'description': """
        Talento Humano
    """,

    'author': "Carlos Diaz",
    'website': "http://www.uasb.edu.ec",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'hr',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/hr_view.xml',
        'security/groups.xml',
    ],
}