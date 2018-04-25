# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from openerp import api, fields, models, _

class project_issue_uasb(models.Model):
    _inherit = 'project.issue'

    categoria = fields.Many2one(comodel_name="project.issue.category", string="Categoría", required=True, )
    subcategoria = fields.Many2one(comodel_name="project.issue.subcategory", string="SubCategoría", required=True, )


class Categoria(models.Model):
    _name = 'project.issue.category'
    name = fields.Char(string="Categoría")

class Subcategoria(models.Model):
     _name = 'project.issue.subcategory'
     name = fields.Char(string="SubCategoría")
     categoria_id = fields.Many2one('project.issue.category', string="Categoría")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: