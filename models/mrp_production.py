# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = "mrp.production"

    moves_corrected_by = fields.Many2one('res.users', 'Moves Corrected By')
    moves_corrected_date = fields.Date('Date Corrected')
    no_correction = fields.Boolean("No Correction Necessary")
    date_reversed = fields.Date('Date Reversed')
    corrections_submitted_by = fields.Many2one('res.users', 'Corrections Submitted By')
    corrections_submitted_to = fields.Many2one('res.users', 'Corrections Submitted To')
    corrections_submitted_date = fields.Date('Date Submitted')
    #bom_labor_hours = fields.Float(string="BOM Labor Hours", related="bom_id.labor_hours")
    #actual_labor_hours = fields.Float("Actual Labor Hours")
