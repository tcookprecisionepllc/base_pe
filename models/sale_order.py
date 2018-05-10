# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    #invoice_address_email = fields.Many2one("Email Address", related="partner_invoice_id.email_temp")
