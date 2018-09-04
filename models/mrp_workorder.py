# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError

class MrpWorkorder(models.Model):
    _inherit = "mrp.workorder"

    workcenter_note = fields.Text(string="Work Center Description", related="workcenter_id.note")
