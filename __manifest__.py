# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '1.2',
    'sequence': -100,
    'category': 'Sales/Sales',
    'summary': 'Sales internal machinery',
    'description': """
This module contains all the common features of Sales Management and eCommerce.
    """,
    'depends': ['sales_team', 'payment', 'portal', 'utm'],
    'data': [ ],

    'installable': True,
    'auto_install': False,
     'application': True,

}
