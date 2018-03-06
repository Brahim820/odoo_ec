# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class ip_ec_solicitud_material(models.Model):
#     _name = 'ip_ec_solicitud_material.ip_ec_solicitud_material'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100