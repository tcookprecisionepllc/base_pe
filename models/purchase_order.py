# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    origin_custom = fields.Char("Custom Origin")
    date_sent = fields.Datetime(string="Date Sent")
    sent_by = fields.Many2one('res.partner','Sent By')
    #date_confirmed = field.Datetime(string="Date Confirmed")
