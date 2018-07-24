# -*- coding: utf-8 -*-
{
    'name': "mi modulo",

    'summary': """
        Este el resumen del módulo""",

    'description': """
        La descripción del módulo
    """,

    'author': "Cristhian Carreño",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'data/data.xml'
    ]
}