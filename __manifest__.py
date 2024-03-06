# -*- coding: utf-8 -*-
{
    'name': "Dental Care",
    'summary': "Dental Care Service",
    'description': """
    Custom module for dental care management in Odoo
    """,

    'author': "Yusuf Willman",
    'website': "https://www.odoo.yusufwllmn.my.id",
    'category': 'Healthcare',
    'version': '0.1',

    'images': ['static/description/icon.png'],
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        
        'views/view_service.xml',
        'views/view_doctor.xml',
        'views/view_patient.xml',
        'views/view_appointment.xml',
        'views/menu.xml',
        
        'report/report_appointment.xml',
        'report/report.xml',
    ],
    
    'installable': True,
    'application': True,
    
    'demo': [
        'demo/demo.xml',
    ],
}

