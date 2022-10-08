# -*- coding: utf-8 -*-

from odoo import api, models, fields

class filter_category(models.Model):
    _inherit = 'pos.category'
    hora_inicio = fields.Float()
    hora_fin= fields.Float()
    #state = fields.Selection(selection_add=[('state', 'state')], ondelete={'state': 'set default'})

