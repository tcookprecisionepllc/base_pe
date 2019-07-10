# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    product_desc = fields.Text(string="Description",related="product_id.description_picking")
