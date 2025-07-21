{
    "name": "POS Credit Limit Alert",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Show credit limit warning in POS when customer exceeds limit",
    "depends": ["point_of_sale", "account"],
    "data": ["views/assets.xml"],
    "assets": {
        "point_of_sale.assets": [
            "pos_credit_limit_alert/static/src/js/credit_limit_alert.js"
        ]
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3"
}