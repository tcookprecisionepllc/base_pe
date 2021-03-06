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
    carton_description = fields.Text(string="Carton Description")
    tracking_number_text = fields.Text(string="Tracking Number(s)")
    date_shipped = fields.Datetime(string="Date Shipped")
    shipped_by = fields.Many2one('res.partner', "Shipped By")
    product_description = fields.Text(string="Description", related="product_id.description_picking")
    delivered_to = fields.Many2one('res.partner', "Delivered To")
    asset_number = fields.Char(string='Asset Number', related="sale_id.asset_number")
    rig_number = fields.Char(string='Rig Number', related="sale_id.rig_number")
    audit_transaction = fields.Boolean("Audit Transaction (no record)")
    is_invalid = fields.Boolean(string="Invalid")
    repair_description = fields.Char(string='Repair Description', related="sale_id.repair_description")
