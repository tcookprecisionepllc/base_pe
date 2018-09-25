# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    invoice_address_email = fields.Char("Email Address", related="partner_id.email_temp")
    shipping_address_email = fields.Char("Email Address", related="partner_shipping_id.email_temp")
    legacy_number = fields.Char("Legacy Number")
    billing_method = fields.Selection([('email', _('Email')),('mail', _('Mail')),('fax', _('Fax')),('hand', _('Hand-delivered'))], string='Billing Method')
    date_delivered = fields.Date('Date Delivered')
    replaced_by = fields.Char("Replaced By")
    date_audited = fields.Date('Date Audited')
