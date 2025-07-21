{
    "name": "POS Credit Limit Alert",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Show credit limit warning in POS when placing an order",
    "depends": ["point_of_sale", "sale"],
    "data": [
        "views/assets.xml"
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_credit_limit_alert/static/src/js/pos_credit_limit.js",
            "pos_credit_limit_alert/static/src/xml/pos_credit_limit_templates.xml"
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False
}
