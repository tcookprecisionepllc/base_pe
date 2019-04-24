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
    labor_hours_bom = fields.Float(string="BOM Labor Hours", related="bom_id.labor_hours")
    labor_hours_actual = fields.Float("Actual Labor Hours")
    assembled_by = fields.Many2one('res.partner', 'Assembled By')
    date_audited = fields.Datetime(string="Date Audited")
    audited_by = fields.Many2one('res.users', 'Audited By')
    date_pulled = fields.Datetime(string="Date Pulled")
    pulled_by = fields.Many2one('res.partner','Pulled By')
    description = fields.Text("Description", related="product_id.description_picking")
    replacement_mo = fields.Char("Replacement MO")
