# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.constrains('name')
    def _check_unique_name(self):
        """Category should have unique name"""
        for record in self:
            existing_category = self.search([('name', '=', record.name), ('id', '!=', record.id)], limit=1)
            if existing_category:
                raise ValidationError("Category name must be unique!")