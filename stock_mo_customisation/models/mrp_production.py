# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    is_readonly = fields.Boolean()

    def action_confirm(self):
        """Manufacturing orders created from sale order should not allowed to change the qty after the confirmation"""
        res = super(MrpProduction, self).action_confirm()
        if self.origin and self.state in ('confirmed', 'cancel'):
            self.is_readonly = True
        return res