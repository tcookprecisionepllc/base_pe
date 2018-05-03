# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    date_done = fields.Datetime('Closed Date',related='picking_id.date_done', store=True, readonly=True)
    qty_available = fields.Float('QoH', related="product_id.qty_available",store=False,readonly=True)
<<<<<<< HEAD
    #product_desc = fields.Text(string="Description", related="product_id.description_picking")
=======
    product_desc = fields.Text(string="Description",related="product_id.description_picking")
>>>>>>> 9c3ffd37ca885ee380d3c00cb69a515c3da19323
