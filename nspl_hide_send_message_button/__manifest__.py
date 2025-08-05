# -*- coding: utf-8 -*-
{
    'name': 'Hide Send Message Button',
    'version': '18.0',
    'summary': "Hide the chatter Send Message button for selected users",
    'description': """
This module adds a user-specific setting to hide the 'Send Message' button in the Odoo chatter for better control and cleaner UI.

✔ Hide 'Send Message' button for selected users  
✔ Controlled via a dedicated security group  
✔ Ideal for roles that should not use chatter communication  
✔ Works across all models using the chatter  
✔ Lightweight and fully JavaScript-based behavior patch  
✔ No impact on messaging or notifications system  

Useful in regulated environments or teams with limited communication permissions.
    """,
    'category': 'Tools',
    'sequence': 5,
    'author': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech',
    'contributors': ['Khanak Hathi'],
    'website': 'https://www.namahsoftech.in',
    'license': 'LGPL-3',
    'support': 'support@namahsoftech.in',
    'price': 29.99,
    'currency': 'USD',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/hide_send_message_group.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'nspl_hide_send_message_button/static/src/js/chatter_patch.js',
            'nspl_hide_send_message_button/static/src/xml/mail_thread_inherit.xml',
        ],
    },
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
