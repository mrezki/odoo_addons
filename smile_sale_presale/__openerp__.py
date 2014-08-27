# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2014 Smile (<http://www.smile.fr>). All Rights Reserved
#                       author cyril.defaria@smile.fr
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{'name': 'Smile Sale Presale',
 'version': '1.0.0',
 'category': 'Sales',
 'depends': ['sale', 'smile_sale_delivery_date'],
 'author': 'Smile',
 'license': 'AGPL-3',
 'description': """
Sur la fiche produit, le module propose les fonctionnalités suivantes:
- Date de sortie d'un produit (release_date).
- Un filtre permet de récupérer les produits dont la date de sortie est dans le futur.
""",
 'data': [
	'views/product_view.xml'
 ],
 'installable': True,
 'application': False,
 'auto_install': False,
 }