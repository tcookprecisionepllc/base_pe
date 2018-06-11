# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    invoice_address_email = fields.Char("Email Address", related="partner_invoice_id.email_temp")
    shipping_address_email = fields.Char("Email Address", related="partner_shipping_id.email_temp")
    product_internal_category = fields.Char(string="Category", related="product_id.categ_id")
