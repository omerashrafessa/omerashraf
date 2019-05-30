# Copyright 2014 Carlos Sánchez Cifuentes <csanchez@grupovermon.com>
# Copyright 2015 Pedro M. Baeza <pedro.baeza@serviciosbaeza.com>
# Copyright 2015 Oihane Crucelaegui <oihanecrucelaegi@avanzosc.es>
# Copyright 2016 Vicent Cubells <vicent.cubells@tecnativa.com>
# Copyright 2017 David Vidal <david.vidal@tecnativa.com>
# Copyright 2018 Duc Dao Dong <duc.dd@komit-consulting.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Sale sec task ",
    "version": "11.0.1.0.0",
    "category": "Sales Management",
    "website": "http://github.com/OCA/sale-workflow",
    "author": "AvanzOSC,"
              "Grupo Vermon,"
              "Tecnativa,"
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
    'base','portal'
    ],
    "data": [
        "security/task_security.xml",
        "views/sale_order_view.xml",
        #"views/saleorder.xml",
    ],
}
