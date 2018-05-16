# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _

class project_issue_uasb(models.Model):
    _inherit = 'project.issue'

    supercategoria = fields.Many2one(comodel_name="project.issue.supercategory", string="Categoría Usuario",  )
    categoria = fields.Many2one(comodel_name="project.issue.category", string="Categoría", required=True, )
    subcategoria = fields.Many2one(comodel_name="project.issue.subcategory", string="SubCategoría", required=True, )
    area = fields.Many2one(comodel_name="project.issue.area", string="Área", required=True, )
    group = fields.Char(string="Puesto de Trabajo:", related='user_id.group.name', readonly=True, store=True, )
    type = fields.Many2one(comodel_name="project.issue.type", string="Tipo Contacto", required=True, )
    tipo = fields.Many2one(comodel_name="project.issue.tipo", string="Tipo",  required=True,)
    state = fields.Selection(
        [
            ('Abierto', 'Abierto'),
            ('Pendiente', 'Pendiente'),
            ('Escalado', 'Escalado'),
            ('Resuelto', 'Resuelto'),
            ('Cerrado', 'Cerrado')
        ],
        'Estado',
        readonly=True,
    )

    @api.multi
    def signal_pendiente(self):
        self.write({'state': 'Pendiente'})
        return True

    @api.multi
    def signal_escalar(self):
        self.write({'state': 'Escalado'})
        return True

    @api.multi
    def signal_resuelto(self):
        self.write({'state': 'Resuelto'})
        return True

    @api.multi
    def signal_cerrado(self):
        self.write({'state': 'Cerrado'})
        return True

class SuperCategoria(models.Model):
    _name = 'project.issue.supercategory'
    name = fields.Char(string="Categoría Usuario")

class Categoria(models.Model):
    _name = 'project.issue.category'
    name = fields.Char(string="Categoría")
    supercategoria_id = fields.Many2one('project.issue.supercategory', string="Categoría de Usuario")

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


class IssueUsers(models.Model):
    _inherit = "res.users"

    group = fields.Many2one('project.issue.group', string="Grupo Técnico")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: