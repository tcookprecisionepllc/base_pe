# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    moves_corrected_by = fields.Many2one('res.users', 'Moves Corrected By')
    moves_corrected_date = fields.Date('Date Corrected')
    no_correction = fields.Boolean("No Correction Necessary")
