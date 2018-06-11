# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpBom(models.Model):
    _inherit = "mrp.bom"

    labor_hours = fields.Float("Labor Hours")
