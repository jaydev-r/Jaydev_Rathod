# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        """Partner should be search on the Ref field from all Many2one"""
        if not args:
            args = []

        if name:
            args += ['|', ('ref', operator, name), ('name', operator, name)]

        return super()._name_search(name, args, operator, limit, name_get_uid)

    def _compute_display_name(self):
        """Custom display name format: PARTNER NAME [REF]"""
        for partner in self:
            ref_part = f" [{partner.ref}]" if partner.ref else ""
            partner.display_name = f"{partner.name}{ref_part}"




