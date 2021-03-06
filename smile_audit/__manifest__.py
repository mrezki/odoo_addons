# -*- coding: utf-8 -*-
# (C) 2010 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Audit Trail",
    "version": "0.1",
    "sequence": 100,
    "category": "Tools",
    "author": "Smile",
    "license": 'AGPL-3',
    "website": 'http://www.smile.fr',
    "description": """
This module lets administrator track every user operation on
all the objects of the system
(for the moment, only create, write and unlink methods).

Suggestions & Feedback to: corentin.pouhet-brunerie@smile.fr
    """,
    "depends": [
        'base',
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/audit_rule_view.xml',
        'views/audit_log_view.xml',
    ],
    "test": [
        'test/audit_test.yml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
