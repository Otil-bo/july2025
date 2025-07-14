{
    "name": "POS Credit Overdue Alert",
    "version": "16.0.1.0.0",
    "summary": "Shows an alert in POS when the selected customer has overdue credit and displays the outstanding amount.",
    "author": "ChatGPT Demo",
    "website": "",
    "license": "LGPL-3",
    "category": "Point of Sale",
    "depends": ["point_of_sale", "account"],
    "data": [
        "views/res_partner_view.xml"
    ],
    "assets": {
        "point_of_sale.assets": [
            "pos_credit_overdue_alert/static/src/js/overdue_credit_alert.js",
            "pos_credit_overdue_alert/static/src/xml/overdue_credit_popup.xml"
        ]
    },
    "installable": true,
    "application": false
}