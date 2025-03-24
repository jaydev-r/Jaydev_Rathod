# -*- coding: utf-8 -*-
{
    "name": "Product Delivery",
    "version": "18.0.0.0",
    "website": "",
    "author": "",
    "maintainers": "",
    "license": "Other proprietary",
    "category": "product",
    "summary": "Jaydev Rathod",
    "depends": [
        "base", "stock", "sale", "mrp"
    ],
    "data": [
        "data/delivery_order_mail_template.xml",
        "views/stock_picking_views.xml",
        "views/mrp_production.xml",
        "views/sale_order_view.xml",
        "views/cron.xml"
    ],

    "application": False,
    "installable": True,
    "auto_install": False,
}
