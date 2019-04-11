# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order"

    invoice_address_email = fields.Char("Email Address", related="partner_invoice_id.email_temp")
    shipping_address_email = fields.Char("Email Address", related="partner_shipping_id.email_temp")
    sale_deadline = fields.Date('Sale Deadline')
    user_id = fields.Many2one('res.users', string='Created By', index=True, track_visibility='onchange', default=lambda self: self.env.user)
    salesperson_from_partner = fields.Char(string="Salesperson", related="partner_id.salesperson.display_name")
    job_ticket_number = fields.Char(string='Job Ticket Number')
