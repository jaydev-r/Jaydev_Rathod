# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _get_new_picking_values(self):
        """Copy all the tags from sale order to Delivery orders created from sale order"""
        vals = super(StockMove, self)._get_new_picking_values()
        tag_ids = self.group_id.sale_id.tag_ids.ids
        vals['tag_ids'] = tag_ids
        return vals