# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    invoice_address_email = fields.Char("Email Address", related="partner_id.email_temp")
    shipping_address_email = fields.Char("Email Address", related="partner_shipping_id.email_temp")
    legacy_number = fields.Char("Legacy Number")
