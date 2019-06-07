# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    date_done = fields.Datetime('Closed Date',related='picking_id.date_done', store=True, readonly=True)
    qty_available = fields.Float('QoH', related="product_id.qty_available",store=False,readonly=True)

    product_desc = fields.Text(string="Description",related="product_id.description_picking")
    bin_locations = fields.Many2many(string="Bin Locations",related="product_id.x_shelf_location_tags")
    counted_by = fields.Many2many('res.partner', string="Counted By")
    reversing_move = fields.Many2one('stock.move', string="Reversing Move")
    is_reversing_move = fields.Boolean(string="Is Reversing Move")
    qty_counted = fields.Float('Quantity Counted')
    zero_counted = fields.Boolean(string="Zero Counted")
    date_actual = fields.Datetime(string="Actual Date")
    date_received = fields.Datetime(string="Date Received")
    pulled_by = fields.Many2one('res.partner','Pulled/Stocked By')
    custom_origin = fields.Char(string="Custom Origin")
    serial_number = fields.Char(string="Serial Number")
    is_equipment = fields.Boolean(string="Is Equipment", related="product_id.x_is_equipment")
    partner =

    #@api.model
    #def my_example(self):
    #    res = super(StockMove, self).my_example()
    #    for record in self:
    #        print 'hello'
    #    return res

    def name_get(self):
        res = []
        for move in self:
            res.append((move.id, '%s - %s%s%s>%s' % (move.id,
                move.picking_id.origin and '%s/' % move.picking_id.origin or '',
                move.product_id.code and '%s: ' % move.product_id.code or '',
                move.location_id.name, move.location_dest_id.name)))
        return res
