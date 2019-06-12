# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = "res.partner"

    email_temp = fields.Char('Email Address')
    salesperson = fields.Many2one('res.partner', string="Salesperson")
    vendor_application_submitted_date = fields.Datetime(string="Credit App Submitted")
    vendor_application_submitted_by = fields.Many2one('res.partner', string="Submitted By")
    vendor_application_approved_date = fields.Datetime(string="Credit App Approved")
    customer_application_submitted_date = fields.Datetime(string="Credit App Submitted")
    customer_application_approved_date = fields.Datetime(string="Credit App Approved")
    customer_application_approved_by = fields.Many2one('res.partner', string="Approved By")
    tax_id_number = fields.Char('Tax ID Number')
