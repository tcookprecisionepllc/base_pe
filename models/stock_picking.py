# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.picking"

    replacement_move_no = fields.Char("Replacement Move")
    corrective_move_no = fields.Char("Corrective Move")
