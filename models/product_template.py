# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class ProductTemplate(models.Model):
    _inherit = "product.template"

    cost_custom = fields.Float('Custom Cost')
    cost_entered_by = fields.Many2One('res.partner','Entered By')
    cost_entered_date = fields.Date('Date Entered')
