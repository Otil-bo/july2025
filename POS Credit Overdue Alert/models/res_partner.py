from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    overdue_credit = fields.Monetary(
        string='Overdue Credit',
        compute='_compute_overdue_credit',
        currency_field='company_currency_id',
        store=True,
        readonly=True,
        help='Sum of all unpaid receivables that are past their due date.'
    )

    @api.depends_context('company')
    def _compute_overdue_credit(self):
        today = fields.Date.context_today(self)
        aml = self.env['account.move.line'].sudo()
        for partner in self:
            lines = aml.search([
                ('partner_id', '=', partner.id),
                ('account_id.internal_type', '=', 'receivable'),
                ('parent_state', '=', 'posted'),
                ('payment_state', 'in', ['not_paid', 'partial']),
                ('date_maturity', '<', today),
            ])
            partner.overdue_credit = sum(lines.mapped('amount_residual'))