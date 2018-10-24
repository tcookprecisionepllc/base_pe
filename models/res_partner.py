# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    email_temp = fields.Char('Email Address')
    salesperson_custom = fields.Many2one('res.partner','Custom Salesperson')
