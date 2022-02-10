# -*- coding: utf-8 -*-

from odoo import models, fields


# class pgl-custom(models.Model):
#     _name = 'pgl-custom.pgl-custom'
#     _description = 'pgl-custom.pgl-custom'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class CrmLead(models.Model):
    
    _inherit = 'crm.lead'
    
    project_category = fields.Selection([
        ('public_sector', 'Public Sector'),
        ('private_sector', 'Private Sector'),
    ], required=True)
    
    
    
    