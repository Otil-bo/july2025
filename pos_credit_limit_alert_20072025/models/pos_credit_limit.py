from odoo import api, models

class PosCreditLimit(models.Model):
    _inherit = "res.partner"

    @api.model
    def check_partner_credit(self, partner_id):
        partner = self.browse(partner_id)
        if not partner:
            return {'allowed': True, 'message': ''}

        credit_limit = partner.credit_limit
        debt = partner.credit or 0.0

        if debt > credit_limit:
            message = (
                f"El cliente {partner.name} tiene un límite de crédito de "
                f"{credit_limit} y una deuda actual de {debt}. No puede continuar."
            )
            return {'allowed': False, 'message': message}

        return {'allowed': True, 'message': ''}
