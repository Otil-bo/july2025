from odoo import models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def check_credit_limit(self, partner_id):
        partner = self.browse(partner_id)
        if not partner or not partner.credit_limit:
            return {'warning': False, 'message': ''}
        if partner.credit > partner.credit_limit:
            return {
                'warning': True,
                'message': f"El cliente {partner.name} ha excedido su límite de crédito."
            }
        return {'warning': False, 'message': ''}