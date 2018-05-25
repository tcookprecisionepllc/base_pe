# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    date_done = fields.Datetime('Closed Date',related='picking_id.date_done', store=True, readonly=True)
    qty_available = fields.Float('QoH', related="product_id.qty_available",store=False,readonly=True)

    product_desc = fields.Text(string="Description",related="product_id.description_picking")
    bin_locations = fields.Many2many(string="Bin Locations",related="product_id.x_shelf_location_tags")
    #bin_locations = fields.Many2many('x_shelf_locations',string="Bin Locations")
    counted_by = fields.Many2many('res.users', string="Counted By")
    #reversing_move_id = fields.Integer('Reversing Move id')
    reversing_move = fields.Many2one('stock.move', string="Reversing Move")
    is_reversing_move = fields.Boolean(string="Is Reversing Move")

    def name_get(self):
        res = []
        for move in self:
            res.append((move.id, '%s - %s%s%s>%s' % (move.id,
                move.picking_id.origin and '%s/' % move.picking_id.origin or '',
                move.product_id.code and '%s: ' % move.product_id.code or '',
                move.location_id.name, move.location_dest_id.name)))
        return res
