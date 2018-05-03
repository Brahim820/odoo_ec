# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class project_issue_uasb(models.Model):
    _inherit = 'project.issue'

    categoria = fields.Many2one(comodel_name="project.issue.category", string="Categoría", required=True, )
    subcategoria = fields.Many2one(comodel_name="project.issue.subcategory", string="SubCategoría", required=True, )
    area = fields.Many2one(comodel_name="project.issue.area", string="Área", required=True, )
    group = fields.Many2one(comodel_name="project.issue.group", string="Grupo", required=True, )
    type = fields.Many2one(comodel_name="project.issue.type", string="Tipo Contacto", required=True, )
    tipo = fields.Many2one(comodel_name="project.issue.tipo", string="Tipo", )

class Categoria(models.Model):
    _name = 'project.issue.category'
    name = fields.Char(string="Categoría")

class Area(models.Model):
    _name = 'project.issue.area'
    name = fields.Char(string="Área")

class Grupo(models.Model):
    _name = 'project.issue.group'
    name = fields.Char(string="Grupo")

class Type(models.Model):
    _name = 'project.issue.type'
    name = fields.Char(string="Tipo de Contacto")

class Subcategoria(models.Model):
     _name = 'project.issue.subcategory'
     name = fields.Char(string="SubCategoría")
     categoria_id = fields.Many2one('project.issue.category', string="Categoría")

class Gestion(models.Model):
     _name = 'project.issue.tipo'
     name = fields.Char(string="Tipo")
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: