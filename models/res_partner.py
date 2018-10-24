# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    email_temp = fields.Char('Email Address')
    test2 = fields.Many2one('sale.order', string="Test")
