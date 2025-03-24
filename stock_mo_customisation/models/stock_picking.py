# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import datetime, timedelta


class StockPicking(models.Model):
    _inherit = "stock.picking"

    tag_ids = fields.Many2many("crm.tag", string="Tags")

    @api.model
    def _cron_delivered_order(self):
        """sending mail to responsible(salesperson) of sale order when the delivery order is delivered."""
        delivered_pickings = self.env['stock.picking'].search([
            ('state', '=', 'done'),
            ('picking_type_id.code', '=', 'outgoing'),
            ('date_done', '>=', (datetime.now() - timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S'))
        ])
        email_template = self.env.ref(
            'stock_mo_customisation.email_template_for_send_mail_delivery_order')
        for picking in delivered_pickings:
            if picking.sale_id:
                email_values = {
                    'email_from': self.env.user.email,
                    'email_to': picking.partner_id.email,
                    'email_cc': False,
                    'scheduled_date': False,
                    'recipient_ids': [],
                    'partner_ids': [],
                    'auto_delete': True,
                }
                email_template.with_context(partner=picking.partner_id, inv=picking).send_mail(picking.id,
                                                                                         email_values=email_values,
                                                                                         force_send=True)
