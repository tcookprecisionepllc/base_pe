# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpBomLine(models.Model):
    _inherit = "mrp.bom.line"

    description = fields.Text(string="Description", related="product_id.description_picking")
    test = fields.Char(string="test")
    #1809011048 This field is not showing up in model. See ir_ui_views.xml for the BOM view to be changed
