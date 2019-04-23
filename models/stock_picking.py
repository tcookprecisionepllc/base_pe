# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.picking"

    replacement_move_no = fields.Char("Replacement Move")
    corrective_move_no = fields.Char("Corrective Move")
    job_ticket_number = fields.Char(string='Job Ticket Number', related="sale_id.job_ticket_number")
    date_received = fields.Datetime(string="Date Received")
    date_checked = fields.Datetime(string="Date Checked")
    checked_by = fields.Many2one('res.partner','Checked By')
    stocked_by = fields.Many2one('res.partner','Pulled/Stocked By')
    freight_cost = fields.Float(string="Freight Charge")
    freight_po = fields.Char(string="Freight PO")
    weight_custom = fields.Float(string="Weight (lbs)")
    carton_count_custom = fields.Integer(string="Number of Cartons")
    carton_description = fields.Char(string="Carton Description")
