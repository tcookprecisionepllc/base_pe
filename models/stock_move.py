# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    date_done = fields.Datetime('Closed Date',related='picking_id.date_done', store=True, readonly=True)
    qty_available = fields.Float('QoH', related="product_id.qty_available",store=False,readonly=True)

    product_desc = fields.Text(string="Description",related="product_id.description_picking")
    bin_locations = fields.One2many(string="Bin Locations",related="product_id.x_shelf_location_tags")
