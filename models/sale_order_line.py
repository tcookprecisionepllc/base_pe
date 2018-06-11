# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    product_internal_category = fields.Char(string="Category", related="product_id.categ_id.name")
