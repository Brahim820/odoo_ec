# -*- coding: utf-8 -*-
{
    'name': "ip_ec_solicitud_material",

    'summary': """
        La generación de un RFP (Solicitud de material) es la creación de un listado de productos requeridos, para que el departamento de compras inicie un proceso de adquisición.""",

    'description': """
        La generación de un RFP (Solicitud de material) es la creación de un listado de productos requeridos, para que el departamento de compras inicie un proceso de adquisición.
    """,

    'author': "Infinit-Plus",
    'website': "http://www.infinit-plus.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Compras',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/request_proposal.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}